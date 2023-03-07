from fileinput import filename
from pytube import YouTube

link = input("Set our video link:\n")
format = input("What format you want: (1 - mp3) (2 - mp4)\n")
yt = YouTube(link)

def mp3():
    downloader.download(filename="YTBaudio.mp3")
def mp4():
    downloader.download(filename="YTBvideo.mp4")

downloader = yt.streams.get_highest_resolution()    
print("Download please wait")

if format == "1":
    mp3()
else:
    mp4()

print("finish")
print(f"Check the result at {filename}")