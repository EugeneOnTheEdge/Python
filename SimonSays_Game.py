#!/usr/bin/python

from fltk import *
import random
import cPickle as IO

def btn_OnClick(self):
	global level, click, simonsaysBtns, userResponse, SimonIsSaying
	gameover = False
	redraw(None)
	print buttons.index(self),
	
	if not SimonIsSaying:
		if self != simonsaysBtns[int(click)]:
			print '\n\n',buttons.index(self), 'is not the same as', ('simonsaysBtns['+str(int(click))+']'), 'or', str(buttons.index(simonsaysBtns[int(click)]))
			gameover = True
		else:
			userResponse.append(self)
			click += 1
			
	if (not SimonIsSaying) and (len(userResponse) == len(simonsaysBtns)):
		level += 1
		click = 0
		startBtn.activate()
		userResponse = []
		SimonIsSaying = True
		print '\n====================='
		startBtn.color(FL_RED)
		statusBar.label('Correct!')
		
	if gameover:
		print '======GAME OVER======'
		statusBar.label('Game over! Nice try.')
		level = 1
		startBtn.activate()
		click = 0
		userResponse = []
		simonsaysBtns = []
		SimonIsSaying = True
		startBtn.color(FL_RED)
	
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
	
	redraw(None)
	
	if order < level:
		Fl.add_timeout(0.5, simonsays)
	else:
		SimonIsSaying = False
		order = 0
		statusBar.label('Waiting for your response...')
	
def start_OnClick(self):
	global _simon
	self.deactivate()
	statusBar.label('')
	self.color(FL_GRAY)
	SimonIsSaying = True
	levelBox.label(str(level))
	btn = random.choice(buttons)
	simonsaysBtns.append(btn)
	if level == 1:
		_simon = [] # _simon is basically the same as simonsaysBtns; except that it is a list of the ORDER of the pressed buttons.
	_simon.append(buttons.index(btn))
	print ("\n\n\n====== LEVEL %i ======\nSimon says:" % level), _simon
	print "\nYou've pressed:"
	redraw(None)
	Fl.add_timeout(1.5, simonsays)

def redraw(self):
	for wid in makeitreal:
		wid.redraw()
	
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
SimonIsSaying = True
originalColour = None
pressed = False

#Window begin
window = Fl_Double_Window( ((getWidth-windowW)/2), ((getHeight-windowH)/2), windowW, windowH, "Simon Says Simulator")
window.begin()
Fl.scheme('gtk+')
window.color(FL_BLACK)

greenBtn = Fl_Button(100,100,195,195)
greenBtn.color(FL_GREEN)
greenBtn.callback(btn_OnClick)

redBtn = Fl_Button(305,100,195,195)
redBtn.color(FL_RED)
redBtn.callback(btn_OnClick)

blueBtn = Fl_Button(100,305,195,195)
blueBtn.color(FL_BLUE)
blueBtn.callback(btn_OnClick)

yellowBtn = Fl_Button(305,305,195,195)
yellowBtn.color(FL_YELLOW)
yellowBtn.callback(btn_OnClick)

buttons = [greenBtn,redBtn,blueBtn,yellowBtn]

statusBar = Fl_Box(100,-150,400,400,'Press start button.')
statusBar.labelcolor(FL_WHITE)
statusBar.labelsize(20)

#Make-it-real moment comes next...
squareBox = Fl_Box(165,165,270,270)
squareBox.box(FL_BORDER_BOX)
squareBox.color(FL_BLACK)
squareBox.color2(FL_BLACK)

squareBox2 = Fl_Box(175,175,250,250)
squareBox2.box(FL_BORDER_BOX)
squareBox2.color(FL_GRAY)
squareBox2.color2(FL_GRAY)

squareBox3 = Fl_Box(180,180,240,106)
squareBox3.box(FL_BORDER_BOX)
squareBox3.color(FL_BLACK)
squareBox3.color2(FL_BLACK)

simonText = Fl_Box(180,185,240,106, "simon")
simonText.labelcolor(FL_GRAY)
simonText.labelsize(65)

startBtn = Fl_Button(287,320,25,25)
startBtn.box(FL_ROUND_UP_BOX)
startBtn.color(FL_RED)
startBtn.callback(start_OnClick)

startText = Fl_Box(280,295,40,25,"START")
startText.labelsize(14)

levelText = Fl_Box(200,325,60,40,'LEVEL')
bestText = Fl_Box(340,325,60,40,'BEST')

bestBox = Fl_Box(340,360,60,40, 'N/A')
bestBox.color(FL_BLACK)
bestBox.labelcolor(FL_WHITE)
bestBox.box(FL_BORDER_BOX)

levelBox = Fl_Box(200,360,60,40, str(level))
levelBox.color(FL_BLACK)
levelBox.labelcolor(FL_GREEN)
levelBox.box(FL_BORDER_BOX)

makeitreal = [squareBox,squareBox2,squareBox3,simonText,startBtn,startText,levelText,bestText,bestBox,levelBox]

#End of widget assignments

window.end()

window.show()
Fl.run()
