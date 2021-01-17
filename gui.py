import functions
from summarize import summarize
from functions import *
from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build
import key
import functions
import requests
import json
from tkinter import * 
import tkinter as tk

VIDEO_ID = ''
summary = ''

def submit():
    url = txtfld.get()
    print("The url is: " + url)

    url_var.set("")
    VIDEO_ID = get_yt_video_id(url)
    summary = summarize(VIDEO_ID)
    t = Text(wrap=WORD)
    lbl2=Label(window, text=summary, fg='black', font=("Helvetica", 12),wraplength=650,justify=CENTER,anchor=CENTER)
    lbl2.grid(row=4, column=1)

def returnUrl():
    return VIDEO_ID

window=tk.Tk()
url_var = tk.StringVar()



lbl=Label(window, text="Enter your YouTube URL link:", fg='black', font=("Helvetica", 16),anchor=CENTER)
#lbl.place(x=60, y=50)
lbl.grid(row=0, column=1)
txtfld=tk.Entry(window, textvariable = url_var, text="Submit", bd=5)
#txtfld.place(x=80, y=150)
txtfld.grid(row=2, column=1)
btn = Button(window, text="Transcriptify!", fg='black', command=submit,anchor=CENTER)
#btn.place(x=80, y=100)
btn.grid(row=3, column=1)
window.title('Scriptr')
window.geometry("800x600+10+10")
window.mainloop()


