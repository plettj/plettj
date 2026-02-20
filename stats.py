from dotenv import load_dotenv

load_dotenv()

import datetime as dt
import os
import re

import requests

# * Inspired by https://github.com/Andrew6rant/Andrew6rant/blob/main/today.py
# * Written by AI.
# * Edited by me.

API = "https://api.github.com/graphql"

USER = os.environ["USER_NAME"]
TOKEN = os.environ["ACCESS_READ_TOKEN"]

HEADERS = {"Authorization": f"bearer {TOKEN}"}


def gql(query: str, variables: dict):
    r = requests.post(
        API, json={"query": query, "variables": variables}, headers=HEADERS, timeout=60
    )
    r.raise_for_status()
    data = r.json()
    if "errors" in data:
        raise RuntimeError(data["errors"])
    return data["data"]


def get_user_created_at():
    q = """
    query($login: String!) {
      user(login: $login) { createdAt }
    }
    """
    return gql(q, {"login": USER})["user"]["createdAt"]


def repo_counts():
    # "repos of my own"
    # "other repos contributed" -> repositoriesContributedTo (excludes your own if includeUserRepositories=false)
    q = """
    query($login: String!) {
      user(login: $login) {
        owned: repositories(ownerAffiliations: OWNER) { totalCount }
        contributed: repositoriesContributedTo(includeUserRepositories: false) { totalCount }
      }
    }
    """
    d = gql(q, {"login": USER})["user"]
    return int(d["owned"]["totalCount"]), int(d["contributed"]["totalCount"])


def search_count(query_str: str):
    q = """
    query($q: String!) {
      search(type: ISSUE, query: $q) { issueCount }
    }
    """
    return int(gql(q, {"q": query_str})["search"]["issueCount"])


def commit_total_by_year(created_at_iso: str) -> int:
    # Uses GitHub “contributions” commit count (fast + rate-limit friendly).
    created = dt.datetime.fromisoformat(created_at_iso.replace("Z", "+00:00"))
    now = dt.datetime.now(dt.timezone.utc)

    q = """
    query($login: String!, $from: DateTime!, $to: DateTime!) {
      user(login: $login) {
        contributionsCollection(from: $from, to: $to) {
          totalCommitContributions
        }
      }
    }
    """

    total = 0
    for year in range(created.year, now.year + 1):
        start = dt.datetime(year, 1, 1, tzinfo=dt.timezone.utc)
        end = dt.datetime(year + 1, 1, 1, tzinfo=dt.timezone.utc)

        if end <= created:
            continue
        if start < created:
            start = created
        if start >= now:
            break
        if end > now:
            end = now

        d = gql(q, {"login": USER, "from": start.isoformat(), "to": end.isoformat()})
        total += int(d["user"]["contributionsCollection"]["totalCommitContributions"])

    return total


def render_block(
    commits: int,
    owned_repos: int,
    contributed_repos: int,
    prs_created: int,
) -> str:
    return "\n".join(
        [
            f'          <p>Total commits <span class="dots">....</span> <span class="accent">{commits:,}</span></p>',
            f'          <p>Repos <span class="dots">............</span> <span class="accent">{owned_repos:,}</span> owned (<span class="accent">{owned_repos + contributed_repos:,}</span> contributed to)</p>',
            f'          <p>PRs <span class="dots">..............</span> <span class="accent">{prs_created:,}</span> created</p>',
        ]
    )


def replace_stats_block(svg_path: str, new_block: str):
    with open(svg_path, "r", encoding="utf-8") as f:
        s = f.read()

    pattern = r"<!-- stats:start -->(.*?)<!-- stats:end -->"
    repl = f"<!-- stats:start -->\n{new_block}\n          <!-- stats:end -->"
    out, n = re.subn(pattern, repl, s, flags=re.S)

    if n != 1:
        raise RuntimeError("Expected exactly one stats block in README.md")

    if out != s:
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(out)


def main():
    created_at = get_user_created_at()
    commits = commit_total_by_year(created_at)

    owned, contributed = repo_counts()
    prs_created = search_count(f"is:pr author:{USER}")

    block = render_block(commits, owned, contributed, prs_created)
    replace_stats_block("stats.svg", block)


if __name__ == "__main__":
    main()
