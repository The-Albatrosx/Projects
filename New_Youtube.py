from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import sys

#video_url = input("Enter the URL of the YouTube video: ").strip()
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
#url= "https://www.youtube.com/watch?v=Vguglo8px3Y"
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
from pytube import YouTube

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

