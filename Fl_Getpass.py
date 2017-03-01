#!/usr/bin/python

from fltk import *

class Fl_Getpass_Input(Fl_Input):
	def __init__(self,x,y,w,h,label=None,mask='*'):
		Fl_Input.__init__(self,x,y,w,h,label)
		self.timeout_added = False
		self.trueValue = ''
		self.prevKey = None
		self.x = x
		self.y = y
		self.mask = mask
		self.timerange = 0
		self.refresh()
		
	def refresh(self):
		self.getKey = Fl.event_text()
		self.getKeyCode = Fl.event_key()
		self.keyboard_is_pressed = bool(Fl.get_key(self.getKeyCode))
		self.maskValue = ''
		self.timerange = self.timerange % 3
		
		if self.keyboard_is_pressed:
			if self.getKeyCode == 65288: #if backspace is pressed:
				self.trueValue = self.trueValue[:len(self.trueValue)-1]
			else:
				self.prevKey = self.getKey
				self.trueValue += self.getKey
				print self.getKeyCode
		
		for k in range(len(self.trueValue)):
			self.maskValue += self.mask
		self.value(self.maskValue)
		
		if self.timeout_added:
			Fl.repeat_timeout(0.05,self.refresh)
		else:
			self.timeout_added = True
			Fl.add_timeout(0.05,self.refresh)
	
	def __repr__(self):
		return ('Fl_Getpass_Input at '+str(self.x)+', '+str(self.y)+'.')

if __name__ == '__main__':
	window = Fl_Double_Window(100,100,1080,607,'FL_GETPASS_INPUT')
	window.begin()
	
	getpassinput = Fl_Getpass_Input(200,100,500,40,'Password: ','x')
	button = Fl_Button(300,200,100,30,'Button')
	
	Fl.event_x(250)
	Fl.event_y(20)
	window.end()
	
	window.show()
	Fl.run()

