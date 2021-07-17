from pytube import Playlist, YouTube
import time
import logging

logging.basicConfig(filename="/home/pico/YT_Downloader/log.txt")

list = Playlist(input("playlist URL: "))
only_sound = input("audio only y/n: ")
if only_sound == "y":
    only_sound = True
else:
    only_sound = False

print(f'Downloading: {list.title}')
#for video in list.videos:
#    try:
#        print(f"downloading {video.title}...")
#        video.streams.filter(only_audio=only_sound).first().download()
#    except:
#        print(f"Error {video.title}")
#        f = open(f"{video.title}.txt", "w+")
#        f.close()
#    time.sleep(2)
for url in list.video_urls:
    try:
        yt = YouTube(url)
    except:
        logging.warning(f'Video {url} is unavaialable, skipping.')
    else:
        print(f'Downloading video: {url}')
        try:
            yt.streams.filter(only_audio=only_sound).first().download()
        except:
            logging.warning(f"Error while downloading video:{url}")
    time.sleep(2)