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
			timeShow.label("0%.3f" % (modSecond))
		else:
			timeShow.label("%.3f" % (modSecond))
	else:
		if modSecond < 10:
			if minute < 10:
				timeShow.label("0%i:0%.3f" % (minute,modSecond))
			else: 
				timeShow.label("%i:0%.3f" % (minute,modSecond))
		else:))))+66
			if minute < 10:
				timeShow.label("0%i:%.3f" % (minute,modSecond))
			else: 
				timeShow.label("%i:%.3f" % (minute,modSecond))
	second += interval
	time[0] = minute
	time[1] = second
	startBtn.shortcut(None)
	stopBtn.shortcut(FL_Enter)
	secondAnalog.value(second%60)
	secondAnalog.color(FL_BLACK)
	Fl.repeat_timeout(interval,loop)

def stopTime(self):
	Fl.remove_timeout(loop)
	stopBtn.shortcut(None)
	startBtn.shortcut(FL_Enter)
	started[0] = False
	second = time[1]
	minute = int(second/60)
	_second = second%60
	if minute < 1:
		if _second < 10:
			timeShow.label("0%.3f" % (_second))
		else:
			timeShow.label("%.3f" % (_second))
	else:
		if _second < 10:
			if minute < 10:
				timeShow.label("0%i:0%.3f" % (minute,_second))
			else: 
				timeShow.label("%i:0%.3f" % (minute,_second))
		else:
			if minute < 10:
				timeShow.label("0%i:%.3f" % (minute,_second))
			else: 
				timeShow.label("%i:%.3f" % (minute,_second))
	secondAnalog.value(0)
	secondAnalog.color(self.labelcolor())
	currentLap = lap[0]
	lapList[currentLap] = str("%.3f" % second)
	lapBrowser.add(('Lap '+str(currentLap)+': '+lapList[currentLap]+'s'))
	lap[0] = currentLap + 1

def resetTime(self):
	time[0] = 0
	time[1] = 0
	timeShow.label("0%.3f" % time[1])
	started[0] = False
	secondAnalog.value(0)
	secondAnalog.color(self.labelcolor())

def lapBrowser_onClick(self):
	value = lapBrowser.text(lapBrowser.value()).split(': ')[1]
	value = value[:len(value)-1]
	secondAnalog.color(FL_BLACK)
	secondAnalog.value(float(value))
	timeShow.label(value)
	
started = [False]
time = [0,0.00] # min , sec
accumulatedTimes = []
watch = [0]
interval = 0.001
lap = [1]
lapList = {}

w = Fl_Double_Window(100,100,1000,700,"STOPWATCH")
w.begin()
w.color(fl_rgb_color(30,30,30))

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
timeShow.label('00.000')
timeShow.labelsize(60)
timeShow.labelcolor(FL_WHITE)
timeShow.align(FL_ALIGN_CENTER)

startBtn = Fl_Button(115,580,70,40,"START")
startBtn.callback(startTime)
startBtn.labelcolor(FL_GREEN)
startBtn.box(FL_NO_BOX)
startBtn.shortcut(FL_Enter)

resetBtn = Fl_Button(265,580,70,40,"RESET")
resetBtn.box(FL_NO_BOX)
resetBtn.callback(resetTime)
resetBtn.labelcolor(FL_WHITE)
resetBtn.shortcut('r')

stopBtn = Fl_Button(415,580,70,40,"STOP")
stopBtn.callback(stopTime)
stopBtn.labelcolor(FL_RED)
stopBtn.box(FL_NO_BOX)

lapBrowser = Fl_Hold_Browser(575,70, 360, 550)
lapBrowser.color(FL_WHITE)
lapBrowser.callback(lapBrowser_onClick)

w.end()
w.show()

Fl.run()
