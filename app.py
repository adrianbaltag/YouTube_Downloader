from ast import And
from msilib.schema import ListBox
from struct import pack
from tkinter import *
from tkinter import filedialog
import tkinter
from tkinter import font
from turtle import color
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
# allows you to copy files/folder and move it
import shutil
import os
import time
from tkinter import messagebox

# functions
# clear btn input


def delete_link():
    list.delete(0, "end")
    link_field.delete(0, 'end')


# delete all_files from pc folder
def del_videos():
    target = "C:\\Users\\adria\\OneDrive\\Desktop\\video_download\\"
    for video in os.listdir(target):
        if video.endswith('.mp4'):
            # messagebox.showinfo('deleting file:', video)
            os.unlink(target + video)
            # time.sleep(2)
            # messagebox.showinfo('file deleted')

# DELETE SINGLE VIDEO


def del_video(event):
    target = "C:\\Users\\adria\\OneDrive\\Desktop\\video_download\\"
    for video in os.listdir(target):
        # if video.endswith('.mp4') != video.endswith('.mp4'):
        messagebox.showinfo('deleting file:', video)
        os.unlink(target + video)
        time.sleep(2)
        messagebox.showinfo('file deleted')
        # print(del_video)


# delete sigle video// what is highlited on click will become ANCHOR
def del_from_list():
    list.delete(ANCHOR)

    # allows user to select a path from the explorer


def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    global value_link
    global get_link
    global user_path
    global mp4_video
    # get user path
    get_link = link_field.get()
    # display user choice in listbox
    value_link = list.insert(0, get_link)

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

# ico file(favicon)
screen.iconbitmap('yt_icon.ico')
# set up GUI
canvas = Canvas(screen, width=500, height=700, bg="#1a1a1a")
canvas.pack()

# img-logo
logo_img = PhotoImage(file='yt.png')

# resize img
logo_img = logo_img.subsample(4, 4)

# set up img to be displayed on canvas
canvas.create_image(250, 80, image=logo_img)

# link field(widgets)
link_field = Entry(screen, width=50, bg="#c92a2a", fg="#faeaea")
link_label = Label(screen, text="Enter Download Link:", font=("Poppins, 12"), bg="#1a1a1a", fg="#fff5f5")

# select path for saving file
path_label = Label(screen, text="Select path for download", padx=20, bg="#8d1d1d", fg="#faeaea", font=("Poppins, 8"))

# btn select
select_btn = Button(screen, text='Select', command=select_path, padx=40, bg="#791919", fg="#faeaea", bd=4, font=("Poppins, 10"))

# add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 320, window=select_btn)

# add link widgets to window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 200, window=link_field)


# download btns
download_btn = Button(screen, text="Download file", padx=19, bg="#791919", fg="#faeaea", bd=4, font=("Poppins, 10"), command=download_file)  # , command=download_file --> for downloading the file
# add to canvas
canvas.create_window(250, 360, window=download_btn)

# frame
frame = Frame(canvas, width=450, height=50)
# add frame to canvas
canvas.create_window(250, 520, window=frame)

# scrollbar
my_scrollbar = Scrollbar(frame, orient=VERTICAL)
# listbox
list = Listbox(frame, width=80, height=5, background='#8d1d1d', fg='white', yscrollcommand=my_scrollbar.set, selectmode=MULTIPLE)
my_scrollbar.config(command=list.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
list.pack()

# btn interact with listbox
btn_clear = Button(canvas, text="Clear", bg='white', fg='#651515', padx=20, command=delete_link, font=("Poppins, 12"), borderwidth=5)
# add btn to canvas
canvas.create_window(130, 600, window=btn_clear)

btn_delete_all = Button(canvas, text="Delete All", bg='#faeaea', fg='#651515', padx=18, command=del_videos, font=("Poppins, 12"), borderwidth=5)
# add btn to canvas
canvas.create_window(245, 600, window=btn_delete_all)


# btn DELETE
btn_delete = Button(canvas, text="Delete",  bg='#faeaea', fg='#651515', padx=18, command=del_from_list, font=("Poppins, 12"), borderwidth=5)
# event listener --<Button-1> mouse_left_click
btn_delete.bind("<Button-1>", del_video)
# add btn to canvas
canvas.create_window(360, 600, window=btn_delete)

# btn quit app
btn_quit = Button(screen, text="Close App", font=('Poppins, 16'), command=screen.quit, bg="#791919", fg="#faeaea", padx=109, bd=5)
canvas.create_window(245, 670, window=btn_quit)
# btn_quit.pack(pady=1)
# run GUI
screen.mainloop()
