from pytube import YouTube

url = input("Enter your YouTube URL: ")
yt =  YouTube(url)

# filters all available qualitys
videos = yt.streams.filter(progressive=True, file_extension='mp4')

# list of all yt qualitys
resolutions =  {
    "144p": 144,
    "240p": 240,
    "360p": 360,
    "480p": 480,
    "720p": 720,
    "1080p": 1080,
    "2160p": 2160,
    "2880p":  2880,
    "4320p": 4320,
}

# always trying to use maximum quality
video = max(videos, key=lambda video: resolutions.get(video.resolution,0))

video.download(r"YOUR SAVING PATH") #Paste it like this C:\Users\Example\Example1


#@INFO:
#       Yt-Downloader coded by | !MeinCtutSehrWeh#4014

#       Work for Botnet | https://botnet.at 

#       Please mention me, when using this Code!
#@INFO:
