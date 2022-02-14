# brightness_img_from_clipboard
# https://www.devdungeon.com/content/grab-image-clipboard-python-pillow
# https://www.geeksforgeeks.org/python-pil-imageenhance-color-and-imageenhance-contrast-method/

from PIL import Image, ImageEnhance
import time
# start ที่ดึงภาพจาก clipboard
# img = ImageGrab.grabclipboard()
# print('===PRINT===  ', img)
# filepath = r'C:\Pics\paste.png'
# img.save('paste.png')
# time.sleep(0.1)

############ PATH #############
import os

mainpath = os.getcwd()
subfolder = r'\Snips'
path = os.path.join(mainpath+subfolder)

############ send to clipboard #############
import win32clipboard as clip
from io import BytesIO

def send_to_clipboard(clip_type, data):
    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardData(clip_type, data)
    clip.CloseClipboard()
    print('sent to clipboard')

def Bright(filename=r'\p_temp.png'):
    time.sleep(0.06)
    image = Image.open(path+filename)
    # Image Enhancement
    enh_img = ImageEnhance.Brightness(image)
    # enh_img.enhance(1.2).save('new.jpg')
    new_img = enh_img.enhance(1.2)
    output = BytesIO()
    new_img.convert('RGB').save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()

    send_to_clipboard(clip.CF_DIB, data)

# Save the image to disk
# img.save('paste.png')
# img.save('new.jpg')
