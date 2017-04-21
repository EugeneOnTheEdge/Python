#!/usr/bin/python

import socket
from fltk import *

class TicTacToe_btn(Fl_Button):
	def __init__(self,x,y,w,h,label=''):
		Fl_Button.__init__(self,x,y,w,h,label)
		self.x_location = x/w
		self.y_location = y/h
		self.callback(self.buttons_onClick)
		self.labelsize(130)

	def buttons_onClick(self, widget):
		print self
		widget.label(XO_me)
		widget.labelcolor(FL_BLUE)
		waitingBox.label("Waiting for your partner's turn...")
		waitingBox.show()
		for x in buttons:
			if widget in x:
				b = str(buttons.index(x))+' '+str(x.index(widget))
		win = winCheck()
		if not win:
			if server:
				s.sendto(b, address)
			else:
				s.sendto(b, (host,port))
			for bx in buttons:
				for by in bx:
					by.deactivate()
	
	def __repr__(self):
		return ('Button at '+str(self.x_location)+' '+str(self.y_location))
			
def center(length,wh='width'):
	if wh == 'width':
		return (Fl.w()-length)/2
	else:
		return (Fl.h()-length)/2
			
def whostarts_selection_onClick(widget):
	global host, server
	if widget.label() == 'Partner':
		host = '0.0.0.0'
		server = True
		tictactoe.label(tictactoe.label()+' SERVER')
		hostInput.value(host)
		hostInput.deactivate()
	whostarts.hide()
	connectionDetails.show()

def connection_confirm_onClick(widget):
	global host, port, XO_me, XO_partner
	host = hostInput.value()
	port = int(portInput.value())
	if server:
		s.bind( (host,port) )
		for bx in buttons:
			for by in bx:
				by.deactivate()
		waitingBox.label("Your partner's goin first..")
		waitingBox.show()
		XO_me = 'O'
		XO_partner = 'X'
	else:
		XO_me = 'X'
		XO_partner = 'O'
		waitingBox.hide()
	connectionDetails.hide()
	tictactoe.show()

def switchturn():
	waitingBox.hide()
	for bx in buttons:
		for by in bx:
			if by.label() == '':
				by.activate()

def onResponse_listener(fd):
	global address, knownAddress
	response = s.recvfrom(1024) #gets you (data, address) from client
	address = response[1]
	data = response[0]
	if data == 'There\'s currently a running session of Tic-Tac-Toe at this IP address. Sorry, no cheaters here! \n*You didn\'t expect this, did ya?? lmao':
		fl_alert(data)
		tictactoe.hide()
	elif data == 'win':
		fl_alert('You lost...')
	else:
		data = data.split()
		x = int(data[0])
		y = int(data[1])
	if knownAddress is None:
		knownAddress = response[1][0]
		waitingBox.label('IT\'S YOUR TURN!')
		waitingBox.redraw()
		Fl.add_timeout(1.0, switchturn)
		buttons[x][y].label(XO_partner)
		buttons[x][y].redraw()
	else:
		if address[0] != knownAddress:
			s.sendto('There\'s currently a running session of Tic-Tac-Toe at this IP address. Sorry, no cheaters here! \n*You didn\'t expect this, did ya?? lmao', address) 
		else:
			waitingBox.label('IT\'S YOUR TURN!')
			waitingBox.redraw()
			Fl.add_timeout(1.0, switchturn)
			buttons[x][y].label(XO_partner)
			buttons[x][y].redraw()
	winCheck()
	
def winCheck():
	win = None
	for x in buttons:
		score = 0
		for btn in x:
			if btn.label() == XO_me:
				score += 1
		if score == 3:
			win = True
	
	if not win:
		for y in range(len(buttons[0])):
			score = 0
			for x in buttons:
				if x[y].label() == XO_me:
					score += 1
			if score == 3:
				win = True
				
	if buttons[1][1].label() == XO_me and buttons[2][2].label() == XO_me and buttons[3][3].label() == XO_me:
		win = True
	if buttons[3][1].label() == XO_me and buttons[2][2].label() == XO_me and buttons[1][3].label() == XO_me:
		win = True
		
	if win:
		fl_alert('You WIN!')
		if server:
			s.sendto('win', address)
		else:
			s.sendto('win', (host,port))
			
			'''if btn.label() == XO_me:
				buttonsAround = [ buttons[btn.x_location-1][btn.y_location-1], buttons[btn.x_location][btn.y_location-1], buttons[btn.x_location+1][btn.y_location-1],
								  buttons[btn.x_location-1][btn.y_location], buttons[btn.x_location+1][btn.y_location],
								  buttons[btn.x_location-1][btn.y_location+1], buttons[btn.x_location][btn.y_location+1], buttons[btn.x_location+1][btn.y_location+1] ]
				
				buttons_2ndlevel = [ button for button in buttonsAround if button.label() == XO_me]
				
				#CONTINUE FROM HERE
				for b in buttons_2ndlevel:
					opposite_yDifference = (btn.y_location - b.y_location) * (-2)
					opposite_xDifference = (btn.x_location - b.x_location) * (-2)
					
					print '>>>',buttons[b.x_location+opposite_xDifference][b.y_location+opposite_yDifference]
					
					if buttons[b.x_location+opposite_xDifference][b.y_location+opposite_yDifference].label() == XO_me:
						fl_alert('WIN')'''
	return win
								  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
fileDescriptor = s.fileno()
Fl.add_fd(fileDescriptor, onResponse_listener)
host = None
port = None
XO_me = None
server = None
XO_partner = None
address = None
knownAddress = None
gridsize = 3
buttons = []

whostarts = Fl_Window(center(500),center(150,'height'),500,150,"Let's start!")
whostarts.begin()
whostartsBox = Fl_Box(0,0,500,75,'Who starts first??')
partnerBtn = Fl_Button(0,100,250,50,"Partner")
meBtn = Fl_Button(250,100,250,50,"Me")
partnerBtn.callback(whostarts_selection_onClick)
meBtn.callback(whostarts_selection_onClick)
whostarts.end()

connectionDetails = Fl_Window(center(500),center(150,'height'),500,150,"I need more info..")
connectionDetails.begin()
connectionDetailsBox = Fl_Box(0,0,500,75,'Please enter connection details.')
hostInput = Fl_Input(100,75,150,30,"HOST: ")
portInput = Fl_Input(325,75,80,30,"PORT: ")
nextBtn = Fl_Button(420,75,30,30,'>')
nextBtn.box(FL_ROUND_UP_BOX)
nextBtn.callback(connection_confirm_onClick)
nextBtn.shortcut(FL_Enter)
connectionDetails.end()

tictactoe = Fl_Window(center(600),center(600,'height'),600,600,'Tic-Tac-Toe')
tictactoe.begin()

for x in range(-1,gridsize+2):
	_buttons = []
	for y in range(-1,gridsize+2):
		_buttons.append(TicTacToe_btn(x*200,y*200,200,200))
	buttons.append(_buttons)

waitingBox = Fl_Box(0,0,600,600,"Waiting for your partner's turn...")
waitingBox.labelsize(30)
tictactoe.end()

whostarts.show()
winCheck()
Fl.run()
