#!/usr/bin/python

from fltk import *
import random
import cPickle as IO

def btn_OnClick(self):
	global level, click, simonsaysBtns
	
	if not SimonIsSaying:
		if simonsaysBtns[int(click)] != buttons.index(self):
			level = 1
			click = 0
			startBtn.activate()
			simonsaysBtns = []
		else:
			click += 1
			
	if click == len(simonsaysBtns):
		click = 0
		level += 1
		startBtn.activate()

def simonsays():
	global pressed, originalColour, click, SimonIsSaying, order, level

	print order
	if not pressed:
		originalColour = simonsaysBtns[order].color()
		simonsaysBtns[order].color(FL_WHITE)
		pressed = True
		click += 0.5
		simonsaysBtns[order].redraw()
	else:
		simonsaysBtns[order].color(originalColour)
		simonsaysBtns[order].redraw()
		pressed = False
		click += 0.5
		order += 1
	
	if order < level:
		Fl.add_timeout(0.5, simonsays)
	else:
		SimonIsSaying = False
		click = 0
		order = 0
	
def start_OnClick(self):
	self.deactivate()
	SimonIsSaying = True
	btn = random.choice(buttons)
	simonsaysBtns.append(btn)
	Fl.add_timeout(0.5, simonsays)
	
	
#Window setup
getWidth = Fl.w()
getHeight = Fl.h()
windowW = 600
windowH = 600

#Game Variables
level = 1
click = 0
order = 0
simonsaysBtns = []
SimonIsSaying = False
pressed = False
originalColour = None

#Window begin
window = Fl_Double_Window( ((getWidth-windowW)/2), ((getHeight-windowH)/2), windowW, windowH, "Simon Says")
window.begin()
Fl.scheme('gtk+')
window.color(FL_BLACK)

greenBtn = Fl_Button(100,100,200,200)
greenBtn.color(FL_GREEN)
greenBtn.callback(btn_OnClick)

redBtn = Fl_Button(300,100,200,200)
redBtn.color(FL_RED)
redBtn.callback(btn_OnClick)

blueBtn = Fl_Button(100,300,200,200)
blueBtn.color(FL_BLUE)
blueBtn.callback(btn_OnClick)

yellowBtn = Fl_Button(300,300,200,200)
yellowBtn.color(FL_YELLOW)
yellowBtn.callback(btn_OnClick)

buttons = [greenBtn,redBtn,blueBtn,yellowBtn]

startBtn = Fl_Button(510,510,75,75,"Start")
startBtn.box(FL_ROUND_UP_BOX)
startBtn.color(FL_GREEN)
startBtn.callback(start_OnClick)
window.end()
#Window end

window.show()
Fl.run()
