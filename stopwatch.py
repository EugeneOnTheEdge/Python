#!/usr/bin/python

from fltk import *
import time as _time
from decimal import *

def loop():
	startBtn.do_callback()
	
def startTime(self):
	if not started[0]:
		watch[0]=_time.time()
		started[0] = True	
	second = time[1]
	minute = int(second/60)
	modSecond = second%60
	if minute < 1:
		if modSecond < 10:
			timeShow.label("0%.2f" % (modSecond))
		else:
			timeShow.label("%.2f" % (modSecond))
	else:
		if modSecond < 10:
			if minute < 10:
				timeShow.label("0%i:0%.2f" % (minute,modSecond))
			else: 
				timeShow.label("%i:0%.2f" % (minute,modSecond))
		else:
			if minute < 10:
				timeShow.label("0%i:%.2f" % (minute,modSecond))
			else: 
				timeShow.label("%i:%.2f" % (minute,modSecond))
	second += 0.03
	time[0] = minute
	time[1] = second
	startBtn.shortcut(None)
	stopBtn.shortcut(FL_Enter)
	secondAnalog.value(second%60)
	secondAnalog.color(FL_BLACK)
	Fl.repeat_timeout(0.03,loop)

def stopTime(self):
	Fl.remove_timeout(loop)
	stopBtn.shortcut(None)
	startBtn.shortcut(FL_Enter)
	started[0] = False
	second = time[1]
	minute = int(second/60)
	second = second%60
	if minute < 1:
		if second < 10:
			timeShow.label("0%.2f" % (second))
		else:
			timeShow.label("%.2f" % (second))
	else:
		if second < 10:
			if minute < 10:
				timeShow.label("0%i:0%.2f" % (minute,second))
			else: 
				timeShow.label("%i:0%.2f" % (minute,second))
		else:
			if minute < 10:
				timeShow.label("0%i:%.2f" % (minute,second))
			else: 
				timeShow.label("%i:%.2f" % (minute,second))
	secondAnalog.value(0)
	secondAnalog.color(self.labelcolor())

def resetTime(self):
	time[0] = 0
	time[1] = 0
	timeShow.label("%i:%.2f" % (time[0],time[1]))
	started[0] = False
	secondAnalog.value(0)
	secondAnalog.color(self.labelcolor())
	
started = [False]
time = [0,0.00] # min , sec
accumulatedTimes = []
watch = [0]

w = Fl_Window(100,100,600,700,"STOPWATCH")
w.begin()
w.color(fl_rgb_color(5,5,5))

secondAnalog = Fl_Dial(85,70,420,420)
secondAnalog.color2(FL_GREEN)
secondAnalog.type(FL_FILL_DIAL)
secondAnalog.angles(0,360)
secondAnalog.bounds(0,60)
secondAnalog.color(FL_BLACK)

bg_secAnalog = Fl_Dial(95,80,400,400)
bg_secAnalog.color(FL_BLACK)
bg_secAnalog.type(FL_FILL_DIAL)

cover = Fl_Button(0,0,600,510)
cover.box(FL_NO_BOX)

timeShow = Fl_Box(0,230,600,100)
timeShow.label("0%i:0%.2f" % (time[0],time[1]))
timeShow.labelsize(60)
timeShow.labelcolor(FL_WHITE)
timeShow.align(FL_ALIGN_CENTER)

startBtn = Fl_Button(115,550,70,40,"START")
startBtn.callback(startTime)
startBtn.labelcolor(FL_GREEN)
startBtn.box(FL_NO_BOX)
startBtn.shortcut(FL_Enter)

resetBtn = Fl_Button(265,550,70,40,"RESET")
resetBtn.box(FL_NO_BOX)
resetBtn.callback(resetTime)
resetBtn.labelcolor(FL_WHITE)

stopBtn = Fl_Button(415,550,70,40,"STOP")
stopBtn.callback(stopTime)
stopBtn.labelcolor(FL_RED)
stopBtn.box(FL_NO_BOX)


w.end()

w.show()
Fl.run()
