from pytube import YouTube  # Fix: Capital T in YouTube

video_url = input("Enter the URL of the YouTube video: ")

yt = YouTube(video_url)  # Fix: YouTube, not Youtube

stream = yt.streams.get_highest_resolution()

stream.download()  # Fix: download, not dowload

print("Download completed!")  # Fix: spelling of 'download'
