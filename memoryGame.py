#!/usr/bin/python

from fltk import *
import random

def btn_onClick(self):
	self.labeltype(FL_NORMAL_LABEL)
	global previousClick
	global clicked
	if previousClick:
		if self.label() in clicked:
			unlocked.append(self.label())
		else:
			clicked = []
		previousClick = False
		print unlocked
	else:
		clicked.append(self.label())
		previousClick = True
	
#Window setup
getWidth = Fl.w()
getHeight = Fl.h()
windowW = 800
windowH = 600

unlocked = []
numbers = range(1,9)
buttons = []
btnLabel = []
clicked = []
previousClick = False

window = Fl_Window( ((getWidth-windowW)/2), ((getHeight-windowH)/2), windowW, windowH, "Memoraiz Dis!")
window.begin()

for row in range(4):
	for column in range(4):
		btn = Fl_Button(column*100+200, row*100+100, 100,100)
	
		btn.labeltype(FL_NO_LABEL)
		btn.callback(btn_onClick)
		buttons.append(btn)

for num in numbers:
	for k in range(2):
		getRandBtn = random.choice(buttons)
		while getRandBtn in btnLabel:
			getRandBtn = random.choice(buttons)
		if getRandBtn not in btnLabel:
			btnLabel.append(getRandBtn)
			getRandBtn.label(str(num))
window.end()

window.show()
Fl.run()
