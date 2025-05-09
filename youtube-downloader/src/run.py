# https://www.youtube.com/watch?v=n0fw88BMbno

# pip install pytubefix pydub

import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pydub import AudioSegment

def convert_to_format(input_file: str, output_format: str):
    """Convert the downloaded file to the desired format."""
    try:
        audio = AudioSegment.from_file(input_file)
        output_file = os.path.splitext(input_file)[0] + f".{output_format}"
        audio.export(output_file, format=output_format)
        os.remove(input_file)  # Remove the original file after conversion
        return output_file
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        return None

def download_video(url: str, format: str):
    """Download the video or audio from YouTube and convert if necessary."""
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Downloading: {yt.title}")

        if format == "mp4":
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path="downloads")
            print(f"Video downloaded successfully as MP4: {yt.title}.mp4")
        elif format in ["mp3", "wav"]:
            stream = yt.streams.filter(only_audio=True).first()
            audio_file = stream.download(output_path="downloads", filename=f"{yt.title}.mp4")
            output_file = convert_to_format(audio_file, format)
            if output_file:
                print(f"Audio downloaded and converted successfully as {format.upper()}: {output_file}")
        else:
            print("Unsupported format. Please choose mp4, mp3, or wav.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the YouTube Downloader!")
    url = input("Please enter the YouTube link: ").strip()
    print("Please choose the format:")
    print("1. MP4 (Video)")
    print("2. MP3 (Audio)")
    print("3. WAV (Audio)")
    choice = input("Enter the number corresponding to your choice: ").strip()

    format_map = {"1": "mp4", "2": "mp3", "3": "wav"}
    format = format_map.get(choice)

    if format:
        download_video(url, format)
    else:
        print("Invalid choice. Please run the script again and choose a valid option.")