#!/usr/bin/python

from fltk import *

def gravity():
	global velocity
	global bird
	global getY
	global window
	
	velocity = velocity - (acceleration*refreshRate)
	displacement = velocity * refreshRate
	getY += int(displacement)
	window.begin()
	bird = Fl_Box(370,getY,60,50)
	bird.image(_bird)
	bird.redraw()
	window.end()
	Fl.repeat_timeout(refreshRate,gravity)
	
def fly(self):
	global gameStarted
	global velocity
	if not gameStarted:
		gameStarted = True
		Fl.add_timeout(refreshRate,gravity)
	else:
		velocity = 20
		 
#Window setup
getWidth = Fl.w()
getHeight = Fl.h()
windowW = 800
windowH = 600

#Game setup
_bird = Fl_PNG_Image('flappybird.png')
_bird = _bird.copy(60,50)
acceleration = 9.8 # m/(s^2)
velocity = 0 # m/s
FPS = 30
refreshRate = 1.0/FPS
gameStarted = False

#GameWindow Begin
window = Fl_Double_Window( ((getWidth-windowW)/2), ((getHeight-windowH)/2), windowW, windowH, "Flappy Burd")
window.begin()

btn = Fl_Button(0,0,5,5)
btn.box(FL_NO_BOX)
btn.callback(fly)
btn.shortcut(FL_ENTER)

bird = Fl_Box(370,275,60,50)
bird.image(_bird)
bird.redraw()
getY = bird.y()

window.end()
#GameWindow End

window.show()
Fl.run()
