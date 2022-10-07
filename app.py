from tkinter import *
from tkinter import filedialog
from turtle import color
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
# allows you to copy files/folder and move it
import shutil

# functions
# allows user to select a path from the explorer


def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget('text')
    screen.title('Downloading...👀')
    # download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()

    # move to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download complete!👍')


    # Tk application object created by instantiating Tk
screen = Tk()
title = screen.title('YouTube Downloader')
# set up GUI
canvas = Canvas(screen, width=500, height=500, bg="#1a1a1a")
canvas.pack()

# img-logo
logo_img = PhotoImage(file='yt.png')

# resize img
logo_img = logo_img.subsample(4, 4)

# set up img to be displayed on canvas
canvas.create_image(250, 80, image=logo_img)

# link field(widgets)
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download Link:", font="Lato, 15", bg="#1a1a1a", fg="#fff")

# select path for saving file
path_label = Label(screen, text="Select path for download", padx=20)
select_btn = Button(screen, text='Select', command=select_path, padx=40, bg='#c92a2a', fg='#fff5f5')

# add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

# add link widgets to window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 200, window=link_field)

# download btns
download_btn = Button(screen, text="Download file", padx=20, bg='#c92a2a', fg='#fff5f5', command=download_file)  # , command=download_file --> for downloading the file
# add to canvas
canvas.create_window(250, 390, window=download_btn)


# run GUI
screen.mainloop()
