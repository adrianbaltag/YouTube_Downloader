from tkinter import *
from tkinter import filedialog
import shutil
import os
import time
from tkinter import messagebox
from moviepy.editor import VideoFileClip
from pytube import YouTube

# functions


# delete link from list and clear entry field
def delete_link():
    list.delete(0, "end")
    link_field.delete(0, 'end')

#  delete all videos in target folder


def del_videos():
    target = "/Users/adrianb-home-folder/Desktop/Youtube_saved"
    for video in os.listdir(target):
        if video.endswith('.mp4'):
            os.unlink(os.path.join(target, video))

# delete single video from traget folder


def del_video(event):
    target = "/Users/adrianb-home-folder/Desktop/video_download/"
    for video in os.listdir(target):
        messagebox.showinfo('deleting file:', video)
        os.unlink(os.path.join(target, video))
        time.sleep(2)
        messagebox.showinfo('file deleted')

#  delete selected video from list


def del_from_list():
    selected_index = list.curselection()
    if selected_index:
        list.delete(selected_index)

#  select path for downloadoading videos from youtube


def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

# download video from youtube


def download_file():
    get_link = link_field.get()
    value_link = list.insert(0, get_link)
    user_path = path_label.cget('text')
    screen.title('Downloading...👀')
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    shutil.move(mp4_video, user_path)
    screen.title('Download complete!👍')


# Tk application object created by instantiating Tk
screen = Tk()
title = screen.title('YouTube Downloader')
screen.iconbitmap('yt_icon.ico')
canvas = Canvas(screen, width=500, height=700, bg="#1a1a1a")
canvas.pack()

logo_img = PhotoImage(file='yt.png')
logo_img = logo_img.subsample(4, 4)
canvas.create_image(250, 80, image=logo_img)

link_field = Entry(screen, width=50, bg="#c92a2a", fg="#faeaea")
link_label = Label(screen, text="Enter Download Link:", font=("Poppins, 12"), bg="#1a1a1a", fg="#fff5f5")

path_label = Label(screen, text="Selected path for download...", padx=20, bg="#8d1d1d", fg="#faeaea", font=("Poppins, 8"))

select_btn = Button(screen, text='Select', command=select_path, padx=40, bg='#faeaea', fg='#651515', bd=4, font=("Poppins, 10"))
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 320, window=select_btn)
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 200, window=link_field)

download_btn = Button(screen, text="Download file", padx=19, bg='#faeaea', fg='#651515', bd=4, font=("Poppins, 10"), command=download_file)
canvas.create_window(250, 360, window=download_btn)

frame = Frame(canvas, width=450, height=50)
canvas.create_window(250, 520, window=frame)

my_scrollbar = Scrollbar(frame, orient=VERTICAL)
list = Listbox(frame, width=80, height=5, background='#8d1d1d', fg='white', yscrollcommand=my_scrollbar.set, selectmode=MULTIPLE)
my_scrollbar.config(command=list.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
list.pack()

btn_clear = Button(canvas, text="Clear", bg='white', fg='#651515', padx=20, command=delete_link, font=("Poppins, 12"), borderwidth=5)
canvas.create_window(130, 600, window=btn_clear)

btn_delete_all = Button(canvas, text="Delete All", bg='#faeaea', fg='#651515', padx=18, command=del_videos, font=("Poppins, 12"), borderwidth=5)
canvas.create_window(245, 600, window=btn_delete_all)

btn_delete = Button(canvas, text="Delete",  bg='#faeaea', fg='#651515', padx=18, command=del_from_list, font=("Poppins, 12"), borderwidth=5)
btn_delete.bind("<Button-1>", del_video)
canvas.create_window(360, 600, window=btn_delete)

btn_quit = Button(screen, text="Close App", font=('Poppins, 16'), command=screen.quit, bg='#faeaea', fg='#651515', padx=109, bd=5)
canvas.create_window(245, 670, window=btn_quit)

screen.mainloop()
