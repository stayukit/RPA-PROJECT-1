# tesseract.py
import pytesseract as pt
import cv2
import os
import time

mainpath = os.getcwd()
# print('mainpath:   ', mainpath)
subfolder = r'\Snips'
path = os.path.join(mainpath+subfolder)
subdir = os.listdir(path)

def PosQR(filename=r'\p_temp.png'):
    # detectQR = 'None'
    img = cv2.imread(path+filename)
    decoder = cv2.QRCodeDetector()
    # data, points, _ = decoder.detectAndDecode(img)
    data, points, _ = decoder.detectAndDecode(img)

    size = img.shape # shape (1145, 284, 3)
    # print('shape', img.shape)
    # print(data, type(data))
    if points is not None:
        pos = points.tolist()[0]
        # print(type(points),points) # numpy array
        # .tolist() [[[101.0, 473.0], [182.0, 473.0], [182.0, 554.0], [101.0, 554.0]]]
        # print(type(points.tolist()[0][1][1]), points.tolist()[0][1][1])
        # io = CropSlip(pos, size=size)
        top = pos[0][1] - ((pos[2][1] - pos[0][1])*1.15) # y ความสูง 1.15 เท่าของ qr
        right = size[1]
        bottom = pos[0][1] # 473
        imcrop = img[int(top):int(bottom), 0:right]
        # cv2.imshow("cropped", imcrop)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return imcrop

def check(data):
	# if text in str(data):
	net = 'None'
	for i in data:
		# print(i)
		if 'Nettotal' in i:
			print('Net total? ', i)
			if ',' in i:
				net = i.split(':')[-1].replace(',','.')
			elif ',' not in i:
				net = i.split(':')[-1]
			print(net)
			# st = format(net, '.2f')			
			if 'Nettotal' in net:
				net = net.replace('Nettotal', '')
			break
	
	print('Net:', net, type(net))
	return net # str	
	# else:
	# 	print('None')
	# 	return 'None'

def OCR(filename=r'\p_temp.png'):
	im = PosQR(filename=filename)
	text = pt.image_to_string(im,lang='eng+tha')
	clean_to_list = text.replace('\n\n', '\n').replace(' ','').split('\n')
	# print(text)
	# print('\n\n=====================\n\n')
	print(clean_to_list, type(clean_to_list))
	# print('\n\n=====================\n\n')
	time.sleep(0.06)
	get = check(data=clean_to_list)
	return get


# check(list)
# OCR()
# from PIL import Image
# import pytesseract as pt
# print(pt.image_to_string(Image.open('book2.jpg'))
# https://stackoverflow.com/questions/65030321/how-to-make-my-tesseract-ocr-conversion-code-run-faster
# https://stackoverflow.com/questions/58948775/is-it-possible-to-extract-text-from-specific-portion-of-image-using-pytesseract
# https://stackoverflow.com/questions/70061664/how-to-a-draw-a-specific-region-in-image-with-mouse-and-extract-that-text-with-p
# https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python
