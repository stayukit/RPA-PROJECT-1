import tkinter as tk
from tkinter import messagebox
from Module.setting import SaveScreen, Pos_Crop, Check_Image
from Module.clickbot import ClickBOT # ClickBot, path
from Module.brightness import Bright # Bright, send_to_clipboard
from Module.rwcsv import Write, Read
from Module.Tesseract import OCR
from Module.clipboard import CopyLabel

root = tk.Tk()
root.title('WIANG YONG V0.1')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("270x135+1100+0")
root.wm_attributes("-topmost", 1)

############### Function ##################

copy_text = 'Status'
# CopyLabel(event,text=''))
# ใช้ bind คู่กับ lambda เกิด error if text[0] == '|': string index out of range
# def CopyLabel(event=None, text=copy_text):
# 	print('test:  ',text)
# 	if text[0] == '|':
# 		ppc.copy(text[1:])
# 		print('Copied')
# 	elif text[0] != '|':
# 		print('None None')
# 		pass
# LB.bind('<Double-Button-1>', Copy)

# bot-copy-savefile
	# open-enhance(bright)-clipboard
	# open-ocr-getdata-show

def Matching(key): # new, page2
	global copy_text
	print(key)
    # BOT-COPY-SAVE กดปุ่ม new จะทำการเลื่อนเม้าส์ไป click copy
	ClickBOT(process=key)
	# ปรับภาพให้สว่าง ลง clipboard
	Bright()
	# OCR-เมื่อ bot ทำงานแล้ว save ภาพสลิป จะไปดึงตัวเลขมา
	# print('PATH:', mainpath+r'\Module\p_temp.png')
	# อ่าน OCR แล้วดึงค่าออกมาใส่เป็นข้อความ
	data = OCR()
	if key == 'new':
		Write(data=data)
		if data != 'None':
			copy_text = '|  {} บาท'.format(data)			
			status.config(text=copy_text[1:])
		elif data == 'None':
			copy_text = ''
			status.config(text='None')
	elif key == 'page2':
		data1 = Read()
		if data1 != 'None' and data != 'None':
			total = float(data) + float(data1)
			copy_text = '|  {} + {} = {} บาท'.format(data, data1, total)
			status.config(text=copy_text[1:])
		elif data1 == 'None' or data == 'None':
			copy_text = ''
			status.config(text='None')
			
def AboutMenu(menu):
	global copy_text
	if menu == 'name':
		copy_text = '|Stayu Kitmonkonpaisan'
	elif menu == 'email':
		copy_text = '|stayu.kitm@gmail.com'
	status.config(text=copy_text[1:])
	
def showBox():
	SaveScreen()
	status.config(text='')
	msgbox = messagebox.askyesno('เพื่อเริ่มตั้งค่าสัญลักษณ์ลูกศรขวา (ด้านล่าง Slip T9)', 'ชี้เม้าส์ไปที่กึ่งกลางลูกศรขวา และ Enter เพื่อบันทึก "ใช่"')
	# print(msgbox, type(msgbox))
	global copy_text
	copy_text = ''
	if msgbox == True:
		Pos_Crop() # get postion and crop
		status.config(text='Status: OK')
		
#################################

# Menu
bg_color = '#116562'
mainmenu = tk.Menu(root)
root.config(bg=bg_color, menu=mainmenu)
root.wm_attributes('-transparentcolor', '#116562') # default#0f0f0f  '#26a69a'
filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Reset **ต้องเปิดหน้า Slip ก่อนกดปุ่มนี้**', command=showBox) ## ตั้งค่าใหม่ ##
mainmenu.add_cascade(label='File', menu=filemenu)
filemenu1 = tk.Menu(mainmenu, tearoff=0)
filemenu1.add_command(label='Developer', command=lambda: AboutMenu('name'))
filemenu1.add_command(label='Contact Email', command=lambda: AboutMenu('email'))
mainmenu.add_cascade(label='About', menu=filemenu1)
#Create Label
# my_label = Label(root, text="Customer", font=("Helvetica", 20))
# my_label.pack(pady=20)

# create stringvar
#my_text = StringVar()
#my_text.set("This is Label 2")

# Create Entry Box
# my_entry = Entry(root, 
# 	font=("Helvetica", 20),
# 	bd=0, 
# 	width=15)

# textvariable=my_text
# Insert into entry box
# my_entry.insert(0, "Time Stamp")
# my_entry.config(state="readonly")

# my_entry.pack(pady=20)
# https://stackoverflow.com/questions/46827674/threading-two-functions-inside-a-method-of-a-class-python
# def runMatching(id):
# 	if id == 1:
# 		t1=threading.Thread(target=Matching, args=['new']).start()
# 		t1.join()
# 	elif id == 2:
# 		t2=threading.Thread(target=Matching, args=['page2']).start()
# 		t2.join()

BT_FRAME = tk.Frame(root, bg=bg_color)
BT_FRAME.pack(pady = 25)
BT1 = tk.Button(BT_FRAME, text='Slip ใหม่', command=lambda: Matching('new'))
BT2 = tk.Button(BT_FRAME, text='หน้า2', command=lambda: Matching('page2'))
BT1.grid(row=0, column=0, ipadx=20, ipady=7, padx=10)
BT2.grid(row=0, column=1, ipadx=25, ipady=7, padx=15)


def CheckStatus():
	global copy_text
	copy_text = ''
	if Check_Image():
		status.config(text='Status: OK')
	else:
		status.config(text='กรุณากดตั้งค่าที่ File > Reset ในการเปิดใช้ครั้งแรก')

status = tk.Label(root, text='', bd=1, relief=tk.SUNKEN, anchor='e')
status.pack(fill='x', side=tk.BOTTOM, ipady=2)
status.bind('<Double-Button-1>', lambda event: CopyLabel(event,text=copy_text))
# status.bind('<Double-Button-1>', CopyLabel)

CheckStatus()

root.mainloop()
