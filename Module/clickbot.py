# clickbot matching.py
# http://cons-robotics.com/API/matching.py # save as matching.py

import numpy as np
import cv2
import pyautogui as pg
import time
import os

from PIL import Image, ImageGrab

mainpath = os.getcwd()
# print('mainpath:   ', mainpath)
subfolder = r'\Snips'
path = os.path.join(mainpath+subfolder)

def Screenshot(filename=r'\screen.jpg'):
	im = np.array(pg.screenshot(path+filename))
	#print(im)
	# return im

def ClickBOT(readarrow=r'\arrow1.jpg', readscreen=r'\screen.jpg', savetemp=r'\p_temp.png', process='new'):
    # copy-เมาส์จะไปชี่เหนือ arrow ณ slip คลิ๊กขวา-เลือก-copy
	# arrow-เมาส์จะไปชื้ที่ arrow
	img = Screenshot() #path pass
	time.sleep(0.06)
	img_temp = cv2.imread(path+readarrow)	#read image
	# read image
	template = cv2.cvtColor(img_temp, cv2.COLOR_BGR2GRAY) #convert to gray image

	screen = cv2.imread(path+readscreen,cv2.IMREAD_GRAYSCALE)

	result = cv2.matchTemplate(template,screen, cv2.TM_CCOEFF_NORMED)

	#print(result)

	loc = np.where(result >=0.7) #checking location that's matched

	#print(loc)

	pos_arrow = []
	pos_copy = []

	for pt in zip(*loc):
		#print(pt)
		pos_arrow.append((pt[1]+10,pt[0]+10)) # pos = (371,24)	# for Windows resolution
		pos_copy.append((pt[1]+10,pt[0]+10-75))
		#pos = ((pt[1]/2) +10,(pt[0]/2)+10)			# for Mac		

	# for pt in zip(*loc):
    # 	#print(pt)
	# 	pos = (pt[1]+10,pt[0]+10) # pos = (371,24)	# for Windows resolution
	# 	#pos = ((pt[1]/2) +10,(pt[0]/2)+10)			# for Mac
	# 	position.append(pos)
	time.sleep(0.06)
	if process == 'new':
		try:
			pg.click(pos_copy[0], clicks=1, button='left')
			time.sleep(0.06)
			pg.click(pos_copy[0], clicks=1, button='right')
			# print('POSITION:  ', pos_copy[0])
			pg.typewrite(['down', 'down', 'enter'], interval=0.06)
			time.sleep(0.06)
			img = ImageGrab.grabclipboard()
			img.save(path+savetemp)
			print('OK new')
			# Bright(addr, page='1')
		except Exception as e: #Exception คือรายละเอียดของ error
			print('ERROR new',e)
	elif process == 'page2':
		try:
			pg.click(pos_arrow[0], clicks=1)
			# print('POSITION:  ', pos_arrow[0])
			time.sleep(0.06)
			pg.click(pos_copy[0], clicks=1, button='left')
			time.sleep(0.06)
			pg.click(pos_copy[0], clicks=1, button='right')
			# print('POSITION:  ', pos_copy[0])
			pg.typewrite(['down', 'down', 'enter'], interval=0.06)
			time.sleep(0.06)
			img = ImageGrab.grabclipboard()
			img.save(path+savetemp)
			print('OK page2')
			# Bright(addr, page='2')
		except Exception as e: #Exception คือรายละเอียดของ error
			print('ERROR page2',e)


	# print('POSITION:  ', position)
	# pg.click(position[0], clicks=2, interval=0.1)
	# pg.doubleClick(position[0])
	# pg.click()
	'''
	Screen picture show image processing result that the highest matching rate
	with the most dense white spot.
	# cv2.imshow('img',result)  
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	'''
# print(ClickBOT(path+r'\arrow1.jpg', 'copy'))
# print(ClickBOT(path+r'\arrow1.jpg', 'page2'))
# frequency error:
	# not the same size -> set code to resize picture
	# picture not contrast

# แกน y ให้ลดลง 550 จากตำแหน่ง right.jpg