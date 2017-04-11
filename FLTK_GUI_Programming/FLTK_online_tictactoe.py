#!/usr/bin/python

import socket
from fltk import *

class TicTacToe_btn(Fl_Button):
	def __init__(self,x,y,w,h,label=''):
		Fl_Button.__init__(self,x,y,w,h,label)
		self.x_location = x/w
		self.y_location = y/h
		self.array_location = len(buttons)+1
		self.callback(self.buttons_onClick)
		self.labelsize(130)

	def buttons_onClick(self, widget):
		widget.label(XO_me)
		widget.labelcolor(FL_BLUE)
		waitingBox.label("Waiting for your partner's turn...")
		waitingBox.show()
		if server:
			s.sendto(str(buttons.index(widget)), address)
		else:
			s.sendto(str(buttons.index(widget)), (host,port))
		for b in buttons:
			b.deactivate()
			
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
		for b in buttons:
			b.deactivate()
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
	for b in buttons:
		if b.label() == '':
			b.activate()

def onResponse_listener(fd):
	global address, knownAddress
	response = s.recvfrom(1024) #gets you (data, address) from client
	address = response[1]
	data = response[0]
	if data == 'There\'s currently a running session of Tic-Tac-Toe at this IP address. Sorry, no cheaters here! \n*You didn\'t expect this, did ya?? lmao':
		fl_alert(data)
		tictactoe.hide()
	else:
		data = int(data)
	if knownAddress is None:
		knownAddress = response[1][0]
		waitingBox.label('IT\'S YOUR TURN!')
		waitingBox.redraw()
		Fl.add_timeout(1.0, switchturn)
		buttons[data].label(XO_partner)
		buttons[data].redraw()
	else:
		if address[0] != knownAddress:
			s.sendto('There\'s currently a running session of Tic-Tac-Toe at this IP address. Sorry, no cheaters here! \n*You didn\'t expect this, did ya?? lmao', address) 
		else:
			waitingBox.label('IT\'S YOUR TURN!')
			waitingBox.redraw()
			Fl.add_timeout(1.0, switchturn)
			buttons[data].label(XO_partner)
			buttons[data].redraw()

def winCheck():
	buttons_2ndlevel = []
	for b in buttons:
		if b.label() != '':
			WhosBoxIsIt = b.label()
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
nextBtn.shortcut()
connectionDetails.end()

tictactoe = Fl_Window(center(600),center(600,'height'),600,600,'Tic-Tac-Toe')
tictactoe.begin()
for x in range(-1,gridsize+2):
	for y in range(-1,gridsize+2):
		buttons.append(TicTacToe_btn(x*200,y*200,200,200))
waitingBox = Fl_Box(0,0,600,600,"Waiting for your partner's turn...")
waitingBox.labelsize(30)
tictactoe.end()

whostarts.show()
Fl.run()
