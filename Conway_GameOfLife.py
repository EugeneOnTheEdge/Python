#!/usr/bin/python

from fltk import *

#CONWAY's GAME OF LIFE RULES:
'''
1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
'''

class Pixel(Fl_Button):
	count = 0
	def __init__(self, x, y, w, h):
		Fl_Button.__init__(self, x, y, w, h)
		self.x = x
		self.y = y
		self.alive = False
		self.callback(self.onClick)
		self.alive_around = 0
		self.box(FL_THIN_DOWN_BOX)
    
	def onClick(self,widget):
		global currentAlive
		if self.alive:
			if not Fl.event_key(FL_SHIFT):
				self.alive = False
				self.color(FL_GRAY)
				currentAlive -= 1
		else:
			self.alive = True
			self.color(FL_BLUE)
			currentAlive += 1
		self.redraw()
		currentAliveBox.label('Alive: '+str(currentAlive)+' /'+str(pixelCount)+' ( %.3f%% )' % (currentAlive/pixelCount*100) )
		if currentAlive > 0:
			simulateBtn.activate()
			resetBtn.activate()
		else:
			simulateBtn.deactivate()
			resetBtn.deactivate()
		print self
	def __repr__(self):
		return 'Button at '+str((self.x)/pixelSize)+', '+str(self.y/pixelSize)

def simulate_listener(widget):
	global currentAlive, borderline
	currentAlive = 0
	stopBtn.activate()
	widget.deactivate()
	resetBtn.deactivate()
	
	for y in range(len(buttons_2d)):
		for x in buttons_2d[y]:
			x.alive_around = 0
			try:
				if buttons_2d[y-1][buttons_2d[y].index(x)-1].alive: 
					x.alive_around += 1
				if buttons_2d[y-1][buttons_2d[y].index(x)].alive: 
					x.alive_around += 1
				if buttons_2d[y-1][buttons_2d[y].index(x)+1].alive: 
					x.alive_around += 1
				#---
				if buttons_2d[y][buttons_2d[y].index(x)-1].alive: 
					x.alive_around += 1
				if buttons_2d[y][buttons_2d[y].index(x)+1].alive: 
					x.alive_around += 1
				#---
				if buttons_2d[y+1][buttons_2d[y].index(x)-1].alive: 
					x.alive_around += 1
				if buttons_2d[y+1][buttons_2d[y].index(x)].alive: 
					x.alive_around += 1
				if buttons_2d[y+1][buttons_2d[y].index(x)+1].alive: 
					x.alive_around += 1
			except:
				x.next_alive = False
				borderline = True
			
			if not borderline:	
				if not x.alive:
					if x.alive_around == 3:
						x.next_alive = True
					else:
						x.next_alive = False
				else:
					currentAlive += 1
					if x.alive_around < 2 or x.alive_around > 3:
						x.next_alive = False
					else:
						x.next_alive = True
			borderline = False
	refresh()
		
def refresh(reset=0):
	global generations, currentAlive
	generations += 1
	resetBtn.deactivate()
	for y in range(len(buttons_2d)):
		for x in buttons_2d[y]:
			if x.next_alive:
				x.color(FL_BLUE)
			else:
				x.color(FL_GRAY)
			x.alive = x.next_alive
			x.redraw()
	generationsBox.label('Generations: '+str(generations-reset))
	currentAliveBox.label('Alive: '+str(currentAlive)+' /'+str(pixelCount)+' ( %.3f%% )' % (currentAlive/pixelCount*100) )
	if currentAlive == 0 and reset != 1:
		stopBtn.do_callback()
	else:
		Fl.add_timeout((1.0/FPS),simulate_listener,simulateBtn)
	
def stop_listener(widget):
	global generations, currentAlive
	generations = 0
	widget.deactivate()
	resetBtn.activate()
	Fl.remove_timeout(simulate_listener)
	if currentAlive > 0:
		simulateBtn.activate()
		resetBtn.activate()
	else:
		simulateBtn.deactivate()
		resetBtn.deactivate()

def reset_listener(widget):
	global currentAlive,generations
	currentAlive = 0
	generations = 0
	for y in range(len(buttons_2d)):
		for x in buttons_2d[y]:
			x.alive = False
			x.next_alive = False
	refresh(1)
	
window = Fl_Double_Window(100,100,1080,607,'Conway\'s Game of Life')
window.begin()

simulateBtn = Fl_Button(25,20,110,35,'SIMULATE')
simulateBtn.callback(simulate_listener)
simulateBtn.box(FL_ROUND_UP_BOX)
simulateBtn.deactivate()
simulateBtn.shortcut(FL_F)

stopBtn = Fl_Button(160,20,110,35,'STOP')
stopBtn.deactivate()
stopBtn.callback(stop_listener)
stopBtn.box(FL_ROUND_UP_BOX)

resetBtn = Fl_Button(700,20,110,35,'RESET')
resetBtn.deactivate()
resetBtn.callback(reset_listener)
resetBtn.box(FL_ROUND_UP_BOX)

generationsBox = Fl_Box(275,20,170,35, 'Generations: 0')

buttons_2d = []
pixelSize = 17
FPS = 50
generations = 0
currentAlive = 0
borderline = False
for y in range(80,600,pixelSize):
    dimension = []
    for x in range(0,1080,pixelSize):
        dimension.append(Pixel(x,y,pixelSize,pixelSize))
    buttons_2d.append(dimension)

pixelCount = len(buttons_2d)*len(buttons_2d[0])*1.0
currentAliveBox = Fl_Box(470,20,200,35,('Alive: '+str(currentAlive)+' /'+str(pixelCount)+' ( %.3f%% )' % (currentAlive/pixelCount*100) ))
window.end()

window.show()
Fl.run()
