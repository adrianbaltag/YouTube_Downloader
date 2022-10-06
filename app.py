from tkinter import *
from tkinter import filedialog

# Tk application object created by instantiating Tk
screen = Tk()
title = screen.title('YouTube Downloader')
# set up GUI
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# img-logo
logo_img = PhotoImage(file='yt.png')
# resize img
logo_img = logo_img.subsample(4, 4)
# set up img to be displayed on canvas
canvas.create_image(250, 80, image=logo_img)

# run GUI
screen.mainloop()
