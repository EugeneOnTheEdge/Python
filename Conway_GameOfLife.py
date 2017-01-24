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
        self.box(FL_FLAT_BOX)
    
    def onClick(self,widget):
        if self.alive:
            self.alive = False
            self.color(FL_GRAY)
        else:
            self.alive = True
            self.color(FL_BLUE)
        self.redraw()
        print self, "Alive:", self.alive
    def __repr__(self):
        return 'Button at '+str((self.x-100)/10)+', '+str(self.y/10)

def simulate(widget):
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
					
				if buttons_2d[y][buttons_2d[y].index(x)-1].alive: 
					x.alive_around += 1
				if buttons_2d[y][buttons_2d[y].index(x)+1].alive: 
					x.alive_around += 1
					
				if buttons_2d[y+1][buttons_2d[y].index(x)-1].alive: 
					x.alive_around += 1
				if buttons_2d[y+1][buttons_2d[y].index(x)].alive: 
					x.alive_around += 1
				if buttons_2d[y+1][buttons_2d[y].index(x)+1].alive: 
					x.alive_around += 1
			except:
				pass
				
			if not x.alive:
				if x.alive_around == 3:
					x.next_alive = True
				else:
					x.next_alive = False
			else:
				if x.alive_around < 2 or x.alive_around > 3:
					x.next_alive = False
				else:
					x.next_alive = True
	refresh()
			
def refresh():
	for y in range(len(buttons_2d)):
		for x in buttons_2d[y]:
			if x.next_alive:
				x.color(FL_BLUE)
			else:
				x.color(FL_GRAY)
			x.alive = x.next_alive
			x.redraw()
			
window = Fl_Window(100,100,800,600,'Conway\'s Game of Life')
window.begin()

simulateBtn = Fl_Return_Button(13,100,75,30,'Simulate')
simulateBtn.callback(simulate)
buttons_2d = []
pixelSize = 10
FPS = 30

for y in range(0,600,pixelSize):
    dimension = []
    for x in range(100,800,pixelSize):
        dimension.append(Pixel(x,y,pixelSize,pixelSize))
    buttons_2d.append(dimension)
window.end()

print buttons_2d
window.show()
Fl.run()
