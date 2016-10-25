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
		else:
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
	secondAnalog.color2(secondAnalogC[0])
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
	secondAnalog.value(60)
	secondAnalog.color2(self.labelcolor())

def lapBrowser_onClick(self):
	value = lapBrowser.text(lapBrowser.value()).split(': ')[1]
	value = value[:len(value)-1]
	secondAnalog.color(FL_BLACK)
	secondAnalog.value(float(value))
	timeShow.label(value)

def prefBtn_onClick(self):
	settings.show()

def saveBtn(self):
	f = open('sw.dat','w')
	f.write( ('%s %s %s \n30 30 30\n' % (int(dialColour.r()*255),int(dialColour.g()*255),int(dialColour.b()*255))) )
	f.close()
	secondAnalogC[0] = fl_rgb_color( int(dialColour.r()*255),int(dialColour.g()*255),int(dialColour.b()*255) )
	secondAnalog.value(60)
	secondAnalog.color2(secondAnalogC[0])
	secondAnalog.redraw()
	bg_secAnalog.redraw()
	timeShow.redraw()
	
try:
	f = open('sw.dat','r')
except IOError:
	f = open('sw.dat','w')
	f.write('0 255 0 \n30 30 30 \n')
	f.close()
	f = open('sw.dat','r')
	
dialC = f.readline().split(' ')
winC = f.readline().split(' ')
f.close()

started = [False]
time = [0,0.00] # min , sec
accumulatedTimes = []
watch = [0]
interval = 0.01
lap = [1]
lapList = {}
secondAnalogC = [fl_rgb_color(int(dialC[0]), int(dialC[1]), int(dialC[2]))]

w = Fl_Double_Window(100,100,1000,700,"STOPWATCH")
w.begin()
w.color(fl_rgb_color(int(winC[0]),int(winC[1]),int(winC[2])))

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

prefBtn = Fl_Button(685, 580, 150, 40, "PREFERENCES")
prefBtn.box(FL_PLASTIC_UP_BOX)
prefBtn.callback(prefBtn_onClick)

lapBrowser = Fl_Hold_Browser(575,70, 360, 440)
lapBrowser.color(FL_WHITE)
lapBrowser.callback(lapBrowser_onClick)

w.end()
w.show()

settings = Fl_Window(350,250,500,350, "Preferences")
settings.begin()
settings.color(fl_rgb_color(30,30,30))

dialColour = Fl_Color_Chooser(100,100,300,150, "Dial Colour")
dialColour.labelcolor(FL_WHITE)
dialColour.rgb(float(dialC[0])/255, float(dialC[1])/255, float(dialC[2])/255)

savePrefBtn = Fl_Button(200,275,100,50, "SAVE")
savePrefBtn.box(FL_NO_BOX)
savePrefBtn.labelcolor(FL_GREEN)
savePrefBtn.callback(saveBtn)

settings.end()
Fl.run()
