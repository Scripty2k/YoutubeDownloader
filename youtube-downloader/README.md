# YouTube Downloader

A simple Python script to download YouTube videos or audio in MP4, MP3, or WAV format. This script uses `pytubefix` for downloading and `pydub` for audio conversion.

---

## Features
- Download YouTube videos in **MP4** format.
- Download and convert YouTube audio to **MP3** or **WAV** format.
- Interactive terminal-based user interface.

---

## Requirements
1. Python 3.7 or higher
2. Required Python libraries:
   - `pytubefix`
   - `pydub`
3. FFmpeg (required for audio conversion):
   - Install FFmpeg on macOS:
     ```bash
     brew install ffmpeg
     ```

   - Install FFmpeg on Debian/Ubuntu based distro's:
     ```bash
     sudo pacman -S ffmpeg
     ```

   - Install FFmpeg on Fedora:
     ```bash
     sudo dnf install ffmpeg
     ```

   - Install FFmpeg on Arch Linux:
     ```bash
     sudo pacman -S ffmpeg
     ```



---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/YoutubeDownloader.git
   cd into YoutubeDownloader
   pip install pytubefix pydub
   cd YoutubeDownloader/youtube-downloader/src

## Usage
- 1. Once you did all the steps in installation, use this command: 'python3 run.py'
- 2. Enter a youtube link you want to download
- 3. Type 1, 2 or 3 to choose between different formats
- 4. Done downloading? Check the downloads folder!