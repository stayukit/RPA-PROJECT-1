# Reset setting: screenshot_position_crop

import pyautogui as pg
from PIL import Image
import os

mainpath = os.getcwd()
# print('mainpath:   ', mainpath)
subfolder = r'\Snips'
path = os.path.join(mainpath+subfolder)

def SaveScreen(filename=r'\screen.jpg'):
    pg.screenshot(path+filename)
    return filename

def Pos_Crop(filename=r'\screen.jpg'):
    pos = pg.position()
    im = Image.open(path+filename)

    left = pos.x-15
    top = pos.y-15
    right = pos.x+15
    bottom = pos.y+15
    imcrop = im.crop((left, top, right, bottom))
    immirror = imcrop.transpose(Image.FLIP_LEFT_RIGHT)
    # imcrop.show()
    imcrop.save(path + r'\arrow1.jpg')
    immirror.save(path + r'\arrow2.jpg')

def Check_Image():
    subdir = os.listdir(path)
    if 'arrow1.jpg' and 'arrow2.jpg' in subdir:
        # status.config(text="Status: OK")
        return True
    else:
        return False