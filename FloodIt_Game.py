#!/usr/bin/python

from fltk import *
import random
class Pixels(Fl_Button):
	def __init__(self, x, y, w, h):
		Fl_Button.__init__(self, x, y, w, h)
		self.color(random.choice(colours))
		self.connected = False
		self.box(FL_THIN_DOWN_BOX)
		self.x_index = (x-50)/pixelSize
		self.y_index = (y-50)/pixelSize
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
				if grid_2d[button.y_index][button.x_index-1].connected and grid_2d[button.y_index][button.x_index-1].color() == button.color():
					button.connected = True
				if grid_2d[button.y_index-1][button.x_index].connected and grid_2d[button.y_index-1][button.x_index].color() == button.color():
					button.connected = True
				if grid_2d[button.y_index][button.x_index+1].connected and grid_2d[button.y_index][button.x_index+1].color() == button.color():
					button.connected = True
				if grid_2d[button.y_index+1][button.x_index].connected and grid_2d[button.y_index+1][button.x_index].color() == button.color():
					button.connected = True
			except:
				pass
			if button.connected:
				button.color(colour)
				button.redraw()
			
colours = [FL_RED, FL_BLUE, FL_GREEN, FL_YELLOW, FL_GRAY]
pixelSize = 35
grid_2d = []
dimension = []
score = 0

window = Fl_Double_Window(100,100,720,750,'Flood It!')
window.begin()

for y in range(50,(50+(pixelSize*15)),pixelSize):
	for x in range(50,(150+(pixelSize*15)), pixelSize):
		dimension.append(Pixels(x,y,pixelSize,pixelSize))
	grid_2d.append(dimension)
	toAppend = []

grid_2d[0][0].connected = True
refresh(grid_2d[0][0].color())

scoreBox = Fl_Box(0,650,720,50,str(score))
scoreBox.labelsize(40)
window.end()

window.show()
Fl.run()
