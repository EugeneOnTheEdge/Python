#!/usr/bin/python

import socket
from fltk import *

def whostarts_selection_onClick(widget):
	global host
	if widget.label() == 'Partner':
		host = '0.0.0.0'
		hostInput.value(host)
		hostInput.deactivate()
	whostarts.hide()
	connectionDetails.show()

def connection_confirm_onClick(widget):
	global host, port
	host = hostInput.value()
	port = int(portInput.value())
	if host == '0.0.0.0':
		s.bind( (host,port) )
	connectionDetails.hide()

def buttons_onClick(widget):
	if host == 'Partner':
		pass #wait for partner
	
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
host = None
port = None
gridsize = 3
buttons = []

whostarts = Fl_Window(500,500,500,150,"Let's start!")
whostarts.begin()
whostartsBox = Fl_Box(0,0,500,75,'Who starts first??')
partnerBtn = Fl_Button(0,100,250,50,"Partner")
meBtn = Fl_Button(250,100,250,50,"Me")
partnerBtn.callback(whostarts_selection_onClick)
meBtn.callback(whostarts_selection_onClick)
whostarts.end()

connectionDetails = Fl_Window(500,500,500,150,"I need more info..")
connectionDetails.begin()
connectionDetailsBox = Fl_Box(0,0,500,75,'Please enter connection details.')
hostInput = Fl_Input(100,75,150,30,"HOST: ")
portInput = Fl_Input(325,75,80,30,"PORT: ")
nextBtn = Fl_Button(420,75,30,30,'>')
nextBtn.box(FL_ROUND_UP_BOX)
nextBtn.callback(connection_confirm_onClick)
connectionDetails.end()

tictactoe = Fl_Window(100,100,600,600,'Tic-Tac-Toe')
tictactoe.begin()
for count in range((gridsize+2)**2):
	if count-(gridsize+2) < 0:
		buttons.append(Fl_Button(count-1*200,
tictactoe.end()

whostarts.show()
Fl.run()
