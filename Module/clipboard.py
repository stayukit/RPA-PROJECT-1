import pyperclip as ppc

def CopyLabel(event=None, text=''):
    # print('test:  ',text)
	if text[0] == '|':
		ppc.copy(text[1:])
		print('Copied')
	elif text[0] != '|':
		print('None None')
		pass