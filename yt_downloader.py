from pytube import YouTube
from tkinter import *

root = Tk()
root.geometry('400x200')

text = StringVar()
text.set("Paste link disini untuk video")
label1 = Label(root, text="   ========== Youtube Dowloader ==========   ")
label1.pack()

def download_video(link):
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').desc().first().download()
    e.delete(0, END)
    e.insert(0, "Video Berhasil Di download")
    
e = Entry(root, width=50, bd=5, textvariable= text)
e.pack(side=TOP, pady=30)

btn1 = Button(root, text="Download Video", command=lambda: download_video(e.get()), bd=5, bg='green', fg='white', activeforeground='white', activebackground='black')
btn1.pack()

root.mainloop()


