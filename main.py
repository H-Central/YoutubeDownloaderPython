from fileinput import filename
from pytube import YouTube

link = input("Set our video link:\n")
yt = YouTube(link)

def mp3():
    return yt.streams.filter(file_extension='mp3').get_highest_resolution()
def mp4():
    return yt.streams.filter(file_extension='mp4').get_highest_resolution()
    
filename = "YTB"
while True:
    format = input("What format you want: (1 - mp3) (2 - mp4)\n")
    match format:
        case "mp3":
            downloader = mp3()
            filename += "audio.mp3"
        case "mp4":
            downloader = mp4()
            filename += "video.mp4"
        case other:
            print("Bad format")
            continue
    print("Download is starting... Please wait")
    downloader.download(filename=filename)
    break

print("finish")
print(f"Check the result at {filename}")
