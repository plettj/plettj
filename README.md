<!--
# HOW TO SCREEN-RECORD THE VIDEOS

On Windows, search for Snipping Tool. Hit the video icon, and don't forgot to save when you're done!

# HOW TO MAKE `.gif` FILES OUT OF `.mp4` FILES

1. Use an online `ffmpeg` emulator like [this one](https://ffmpeg.wide.video/), or make sure it's installed on your system.
2. Run the following commands, replacing EXAMPLE with your file.

```sh
ffmpeg -i EXAMPLE_showcase.mp4 -vf "fps=20,scale=-1:240:flags=lanczos,palettegen" -y palette.png

ffmpeg -i EXAMPLE_showcase.mp4 -i palette.png -filter_complex "fps=20,scale=-1:240:flags=lanczos[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=5" -loop 0 EXAMPLE_showcase.gif
```
-->

![On Stage Headshot - Josiah Plett](/images/On_Stage_Headshot.jpg)

<p align="center">
<a href="https://plett.dev/about">Entrepreneur</a> <strong>|</strong> 
<a href="https://plett.fun/">Game Developer</a> <strong>|</strong> <a href="https://old.plett.dev/More/media-features">3x Guinness World Record Breaker</a> <strong>|</strong> 
<a href="https://plett.dev/photography">Photographer</a>
</p>

---

[plett.fun](https://plett.fun/) is where you can play 18 of my games.

[plett.dev](https://plett.dev/) is my personal website.

I'm currently full-stack at [Maxima AI](https://www.maxima.ai/) and former CTO at [Portage Labs](https://www.portagelabs.io/). Contact me on [Linkedin](https://www.linkedin.com/in/josiahplett/) or at _jlplett_ at _uwaterloo_ dot _ca_ if you'd like to reach out.

---

Click on the GIFs to go to their websites.

<p float="left" align="center">
<a href="https://plett.fun/pentris"><img src="https://github.com/plettj/plettj/blob/main/showcase_videos/pentris_showcase.gif" alt="Pentris Showcase Video" height="140px"/></a>
<a href="https://www.coolmathgames.com/0-split-second"><img src="https://github.com/plettj/SplitSecond/blob/main/youtube/split_second_showcase_2.gif" alt="Split Second Showcase Video" height="140px"/></a>
<a href="https://plettdev.itch.io/snake-2"><img src="https://github.com/plettj/lofi_ghost/blob/main/display_files/snake_2_showcase.gif" alt="Snake 2 Showcase Video" height="140px"/></a>
<a href="https://plettdev.itch.io/lo-fi-ghost"><img src="https://github.com/plettj/lofi_ghost/blob/main/display_files/lofi_ghost_showcase.gif" alt="Lo-fi Ghost Showcase Video" height="140px"/></a>
<a href="https://old.plett.dev/More/game-of-life"><img src="https://github.com/plettj/plettj/blob/main/showcase_videos/game_of_life_showcase_1.gif" alt="Conway's Game of Life Showcase Video" height="140px"/></a>
<a href="https://pixelexplorer.surge.sh/"><img src="https://github.com/plettj/Pixel-Explorer/blob/master/display_assets/pixel_explorer_showcase.gif" alt="Pixel Explorer Showcase Video" height="140px"/></a>
<a href="https://plettdev.itch.io/flippyfloor"><img src="https://github.com/plettj/plettj/blob/main/showcase_videos/flippy_floor_showcase.gif" alt="Flippy Floor Showcase Video" height="140px"/></a>
<a href="https://spacegolf.surge.sh/"><img src="https://github.com/plettj/plettj/blob/main/showcase_videos/space_golf_showcase.gif" alt="Space Golf Showcase Video" height="140px"/></a>
<a href="https://devpost.com/software/split-second"><img src="https://github.com/plettj/plettj/blob/main/showcase_videos/split_second_v1_showcase.gif" alt="Split Second V1 Showcase Video" height="140px"/></a>
<a href="https://analysisboard.surge.sh/"><img src="https://github.com/plettj/plettj/blob/main/showcase_videos/chess_analysis_showcase.gif" alt="Chess Analysis Board Showcase Video" height="140px"/></a>
</p>

---

<details><summary> How to make those little <code>GIF</code>s </summary><br />

Instructions exist so I don't keep forgetting. :-]

1. Record the video.
   a. On Windows, search for "Snipping Tool," hit the video icon, and record. Don't forget to save afterwards.
2. Use an online `ffmpeg` emulator like [this one](https://ffmpeg.wide.video/), or make sure it's installed on your system to...
3. Run the following commands, replacing EXAMPLE with your file.

```sh
ffmpeg -i EXAMPLE_showcase.mp4 -vf "fps=20,scale=-1:240:flags=lanczos,palettegen" -y palette.png

ffmpeg -i EXAMPLE_showcase.mp4 -i palette.png -filter_complex "fps=20,scale=-1:240:flags=lanczos[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=5" -loop 0 EXAMPLE_showcase.gif
```

</details>
