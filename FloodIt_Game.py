#!/usr/bin/python

from fltk import *
import random

class Pixels(Fl_Button):
	def __init__(self, x, y, w, h, border=False):
		Fl_Button.__init__(self, x, y, w, h)
		self.connected = False
		self.box(FL_THIN_DOWN_BOX)
		self.x_index = (x-startX)/pixelSize
		self.y_index = (y-startY)/pixelSize
		if border:
			self.color(FL_BLACK)
		else:
			self.color(random.choice(colours))
			self.callback(self.onClick)
		
	def onClick(self,widget):
		global score
		print self, '| Connected:', self.connected
		refresh(self.color())
		score += 1
		scoreBox.label(str(score))
		
	def __repr__(self):
		return ('Button at '+str(self.x_index)+', '+str(self.y_index))
        
def refresh(colour):
	for yList in grid_2d:
		for button in yList:
			try:
				if grid_2d[button.y_index][button.x_index-1].connected and grid_2d[button.y_index][button.x_index-1].color() == button.color(): button.connected = True
				if grid_2d[button.y_index-1][button.x_index].connected and grid_2d[button.y_index-1][button.x_index].color() == button.color(): button.connected = True
				if grid_2d[button.y_index][button.x_index+1].connected and grid_2d[button.y_index][button.x_index+1].color() == button.color(): button.connected = True
				if grid_2d[button.y_index+1][button.x_index].connected and grid_2d[button.y_index+1][button.x_index].color() == button.color(): button.connected = True
			except:
				pass
			if button.connected:
				button.color(colour)
				button.redraw()

#Positions and Sizing
pixelSize = 40
gridsize = 13
window_W = 720
window_H = 750
startX = (window_W - (pixelSize*gridsize))/2
startY = (window_H - (pixelSize*gridsize))/2 - 50
colours = [FL_RED, FL_BLUE, FL_GREEN, FL_YELLOW, FL_CYAN]

grid_2d = []
dimension = []
score = 0

window = Fl_Double_Window(100,100,720,750,'Flood It!')
window.begin()

for y in range(startY,(startY+(pixelSize*gridsize)),pixelSize):
	for x in range(startX,(startX+(pixelSize*gridsize)), pixelSize):
		dimension.append(Pixels(x,y,pixelSize,pixelSize))
	grid_2d.append(dimension)
	dimension = []

grid_2d[0][0].connected = True
refresh(grid_2d[0][0].color())

scoreBox = Fl_Box(0,650,720,50,str(score))
scoreBox.labelsize(40)
window.end()

window.show()
Fl.run()
