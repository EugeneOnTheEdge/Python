#!/usr/bin/python

from fltk import *
import random
import cPickle as IO

def btn_OnClick(self):
	global level, click, simonsaysBtns, userResponse, SimonIsSaying
	gameover = False
	print buttons.index(self),
	
	if not SimonIsSaying:
		if self != simonsaysBtns[int(click)]:
			print '\n\n',buttons.index(self), 'is not the same as', ('simonsaysBtns['+str(int(click))+']'), 'or', str(buttons.index(simonsaysBtns[int(click)]))
			gameover = True
		else:
			userResponse.append(self)
			click += 1
			
	if len(userResponse) == len(simonsaysBtns):
		level += 1
		click = 0
		startBtn.activate()
		userResponse = []
		SimonIsSaying = False
		print '\n====================='
		
	if gameover:
		print '======GAME OVER======'
		level = 1
		startBtn.activate()
		click = 0
		userResponse = []
		simonsaysBtns = []
		SimonIsSaying = False

def simonsays():
	global pressed, originalColour, SimonIsSaying, order, level

	if not pressed:
		originalColour = simonsaysBtns[order].color()
		simonsaysBtns[order].color(FL_WHITE)
		pressed = True
		simonsaysBtns[order].redraw()
	else:
		simonsaysBtns[order].color(originalColour)
		simonsaysBtns[order].redraw()
		pressed = False
		order += 1
	
	if order < level:
		Fl.add_timeout(0.5, simonsays)
	else:
		SimonIsSaying = False
		order = 0
	
def start_OnClick(self):
	global _simon
	self.deactivate()
	SimonIsSaying = True
	btn = random.choice(buttons)
	simonsaysBtns.append(btn)
	if level == 1:
		_simon = [] # _simon is basically the same as simonsaysBtns; except that it is a list of the ORDER of the pressed buttons.
	_simon.append(buttons.index(btn))
	print ("\n\n\n====== LEVEL %i ======\nSimon says:" % level), _simon
	print "\nYou've pressed:"
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
_simon = []
userResponse = []
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
