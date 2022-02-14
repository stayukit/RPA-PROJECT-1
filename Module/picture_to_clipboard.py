# https://clay-atlas.com/us/blog/2020/10/30/python-en-pillow-screenshot-copy-clipboard/

# If you are using pywin32 in the first time,
# you need to use the following command to install:
# sudo pip3 install pywin32

# start coding
# -*- coding: utf-8 -*-
# from tkinter import Image
import win32clipboard as clip
# import win32con
from io import BytesIO
from PIL import Image
# from PIL import ImageGrab


# First, import the module we need. ImageGrab() is a function to take the screenshot in Pillow.
# And win32clipboard can make us to copy the image to our clipboard.

# image = ImageGrab.grab()

# Use key a to screenshot so that we put the captured full-screen image into the variable image.
# Remember this is stored in RGB format, if you want to use a module to display such as OpenCV,
# you need to convert it to BGR.


### Copy to clipboard ###

def send_to_clipboard(clip_type, data):
    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardData(clip_type, data)
    clip.CloseClipboard()

filepath = 'new.jpg'
image = Image.open(filepath)

output = BytesIO()
image.convert('RGB').save(output, 'BMP')
data = output.getvalue()[14:]
output.close()

# send_to_clipboard(win32con.CF_DIB, data)
send_to_clipboard(clip.CF_DIB, data)


# It should be noted here that after OpenClipboard(), emptyClipboard() should be used to empty the clipboard.
# Otherwise, if something is stored in the original clipboard, an error will occur in our program.

# After running the above program, find a place to paste it and you can see our screenshot.