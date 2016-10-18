#!/usr/bin/python

from fltk import *

def loop():
	startBtn.do_callback()
	
def startTime(self):
	second = time[1]
	minute = int(second/60)
	timeShow.label("%i:%.2f s" % (minute,second%60))
	second += 0.01
	time[0] = minute
	time[1] = second
	Fl.repeat_timeout(0.01,loop)
		
def stopTime(self):
	Fl.remove_timeout(loop)

def resetTime(self):
	time[0] = 0
	time[1] = 0
	timeShow.label("%i:%.2f s" % (time[0],time[1]))
	
started = False
time = [0,0.00] # min , sec

w = Fl_Window(100,100,700,350,"STOPWATCH")
w.begin()

timeShow = Fl_Box(0,70,700,100)
timeShow.label("%i:%.2f s" % (time[0],time[1]))
timeShow.labelsize(75)
timeShow.align(FL_ALIGN_CENTER)

startBtn = Fl_Return_Button(250,220,100,40,"Start")
startBtn.callback(startTime)
stopBtn = Fl_Button(350,220,100,40,"Stop")
stopBtn.callback(stopTime)
resetBtn = Fl_Button(300,270,100,40,"RESET")
resetBtn.callback(resetTime)

startBtn.box(FL_PLASTIC_UP_BOX)
stopBtn.box(FL_PLASTIC_UP_BOX)
resetBtn.box(FL_PLASTIC_UP_BOX)
w.end()

w.show()
Fl.run()
