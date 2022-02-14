import os

mainpath = os.getcwd()
subfolder = r'\Snips'
path = os.path.join(mainpath+subfolder)

def Write(data, filename=r'\d_temp.txt'):
	with open(path+filename,'w',newline='') as f:
		# 'a'=append, 'w'=write 
		# fw = csv.writer(f)
		# fw.writerow(data) # row ไม่มี s จะบันทึกแยกเป็น cell ไปทางขวา
								  # rows จะเขียนทีละหลายบรรทัด
		f.write(data)

def Read(filename=r'\d_temp.txt'):
	with open(path+filename, 'r',newline='') as f:
		# fr = csv.reader(f)
		# alldata = list(fr)
		alldata = f.read()

	return alldata