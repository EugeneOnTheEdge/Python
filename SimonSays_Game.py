#!/usr/bin/python

from fltk import *
import random

def btnOnClick(self):
	if not SimonIsSaying:
		print buttons.index(self)

def simonsays(counts):
	pressed = True
	SimonIsSaying = True
	
	for click in range(counts):
		btn = random.choice(buttons)
		getColour = btn.color()
		simonsaysBtns.append(buttons.index(btn)) #Appends the order of a clicked button
		btn.color(FL_WHITE)
		btn.color(getColour)
	
		print simonsaysBtns
		
#Window setup
getWidth = Fl.w()
getHeight = Fl.h()
windowW = 500
windowH = 500

#Game Variables
level = 0
simonsaysBtns = []
SimonIsSaying = False
pressed = False

#Window begin
window = Fl_Double_Window( ((getWidth-windowW)/2), ((getHeight-windowH)/2), windowW, windowH, "Simon Says")
window.begin()
Fl.scheme('gtk+')
window.color(FL_BLACK)

greenBtn = Fl_Button(50,50,200,200)
greenBtn.color(FL_GREEN)
greenBtn.callback(btnOnClick)

redBtn = Fl_Button(250,50,200,200)
redBtn.color(FL_RED)
redBtn.callback(btnOnClick)

blueBtn = Fl_Button(50,250,200,200)
blueBtn.color(FL_BLUE)
blueBtn.callback(btnOnClick)

yellowBtn = Fl_Button(250,250,200,200)
yellowBtn.color(FL_YELLOW)
yellowBtn.callback(btnOnClick)

buttons = [greenBtn,redBtn,blueBtn,yellowBtn]

simonsays(5)
window.end()
#Window end

window.show()
Fl.run()
