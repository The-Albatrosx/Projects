from pytube import YouTube
from pytube.exceptions import VideoUnavailable


url = input("Enter the URL of the YouTube video: ").strip()

try:
    yt = YouTube(url)
    print(f"Video title: {yt.title}")

    stream = yt.streams.get_highest_resolution()
    print("Downloading...")
    stream.download()
    print("Download completed!")

except VideoUnavailable:
    print("This video is unavailable.")
except Exception as e:
    print("An error occurred:", e)



