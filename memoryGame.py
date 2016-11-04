#!/usr/bin/python

from fltk import *
import random

def btn_onClick(self):
	global previousClick, nextPreviousClick, clicked
	if nextPreviousClick:
		refresh()
		nextPreviousClick = False
	self.labeltype(FL_NORMAL_LABEL)
	print self.label(), clicked
	
	if not previousClick:
		previousClick = True
		clicked.append(self.label())
	else:
		previousClick = False
		nextPreviousClick = True
		if self.label() in clicked:
			unlocked.append(self.label())
		clicked = []
	
def refresh():
	global unlocked, buttons
	for btn in buttons:
		if btn.label() in unlocked:
			btn.labeltype(FL_NORMAL_LABEL)
		else:
			btn.labeltype(FL_NO_LABEL)
		btn.redraw()
			
#Window setup
getWidth = Fl.w()
getHeight = Fl.h()
windowW = 800
windowH = 600

unlocked = []
numbers = (range(1,9))*2
buttons = []
btnLabel = []
clicked = []
previousClick = False
nextPreviousClick = False

window = Fl_Window( ((getWidth-windowW)/2), ((getHeight-windowH)/2), windowW, windowH, "Memoraiz Dis!")
window.begin()

for row in range(4):
	for column in range(4):
		btn = Fl_Button(column*100+200, row*100+100, 100,100)
	
		btn.labeltype(FL_NO_LABEL)
		label = random.choice(numbers)
		numbers.remove(label)
		btn.label(str(label))
		btn.labeltype(FL_NO_LABEL)
		btn.labelsize(25)
		btn.callback(btn_onClick)
		buttons.append(btn)

window.end()

window.show()
Fl.run()
