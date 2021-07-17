from logging import error
from pytube import YouTube as YT
import os

dir = input("enter dir")

os.chdir(dir)

while(True):
    link = input("enter youtube link, 'exit' to close': ")
    if link == "exit":
        break

    try:
        vid = YT(link)
        mp4files = vid.streams.filter(file_extension="mp4", progressive=True).order_by("resolution")
        mp4files.last().download()

        print(vid.title + " done")  
    except:
        print("link error")
    