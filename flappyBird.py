#!/usr/bin/python

from fltk import *

#Window setup
getWidth = Fl.w()
getHeight = Fl.h()
windowW = 800
windowH = 600

#Game setup
acceleration = 9.8 #m/(s^2)

window = Fl_Window( ((getWidth-windowW)/2), ((getHeight-windowH)/2), windowW, windowH, "Flappy Burd")
window.begin()

window.end()

Fl.run()
