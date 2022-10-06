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

# link field(widgets)
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download Link:", font="Lato, 15")

# add link widgets to window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 200, window=link_field)


# run GUI
screen.mainloop()
