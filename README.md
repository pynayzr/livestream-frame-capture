![pylivecap logo](https://github.com/pynayzr/livestream-frame-capture/blob/master/README/logo.png)

## pylivecap

Capture image from Internet live streaming such as YouTube, Twitch, Dailymotion
...etc

## Pre-requirements

Please install these package before using pylivecap

* ffmpeg

```bash
// Ubuntu
sudo apt-get install ffmpeg

// ArchLinux
sudo pacman -S ffmpeg

// macOS
brew install ffmpeg
```

## How To Use

```python
>>> import pylivecap
>>> YOUTUBE_LIVESTREAM = 'https://www.youtube.com/watch?v=zjGR32QyTkQ'

# Capture YouTube livestream to `/tmp/out.jpg`
>>> pylivecap.safe_capture(YOUTUBE_LIVESTREAM, '/tmp/out.jpg')

# Setting Video Quality to 360p
>>> pylivecap.safe_capture(YOUTUBE_LIVESTREAM, '/tmp/out.jpg', pbylivecap.VideoQuality.Q360)

# Faster capture without checking
>>> pylivecap.capture(YOUTUBE_LIVESTREAM, '/tmp/out.jpg')
```

## Video Quality Options

* BEST
* WORST
* Q1080
* Q720
* Q320
* Q240
* Q144
