from tkinter import *
from pytube import YouTube as YT
import os

os.chdir("downloads")

def Download():
    info.configure(text="processing...")
    
    try:
        vid = YT(linkInputBox.get())
        mp4files = vid.streams.filter(file_extension="mp4", progressive=True).order_by("resolution")
        mp4files.last().download()
        info.configure(text="done!")
    except:
        info.configure(text="error!")
        
root = Tk()

frame = Frame(root, padx=50, pady=50)
frame.pack()

linkInputBox = Entry(frame, width=50)
linkInputBox.pack()

downloadButton = Button(frame, text="Download", command=Download)
downloadButton.pack()

info = Label(frame, text="enter link")
info.pack()

root.mainloop()