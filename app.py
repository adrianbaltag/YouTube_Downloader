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

# select path for saving file
path_label = Label(screen, text="Select path for download")
select_btn = Button(screen, text='Select')

# add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

# add link widgets to window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 200, window=link_field)

# download btns
download_btn = Button(screen, text="Download file")  # , command=download_file
# add to canvas
canvas.create_window(250, 390, window=download_btn)


# run GUI
screen.mainloop()
