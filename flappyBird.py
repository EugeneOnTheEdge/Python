#!/usr/bin/python

from fltk import *

def gravity():
	global velocity
	global getY
	global window
	global gameStarted
	
	velocity = velocity - (acceleration*refreshRate)
	displacement = velocity * refreshRate
	getY -= int(displacement)
	if getY + int(displacement) >= windowH:
		Fl.remove_timeout(gravity)
		gameStarted = False
	else:
		window.begin()
		clear = Fl_Button(0,0,800,600)
		clear.color(fl_rgb_color(192,192,192))
		bird = Fl_Box(370,getY,60,50)
		bird.image(_bird)
		bird.redraw()
		window.redraw()
		window.end()
		Fl.repeat_timeout(refreshRate,gravity)
	
def fly(self):
	global gameStarted
	global getY
	global velocity
	if not gameStarted:
		gameStarted = True
		getY = 275
		Fl.add_timeout(refreshRate,gravity)
		velocity = 300	
	else:
		velocity = 300
		 
#Window setup
getWidth = Fl.w()
getHeight = Fl.h()
windowW = 800
windowH = 600

#Game setup
_bird = Fl_PNG_Image('flappybird.png')
_bird = _bird.copy(60,50)
acceleration = 800 # pixel/(s^2)
velocity = 0 # pixel/s
FPS = 25
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
