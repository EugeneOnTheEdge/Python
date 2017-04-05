#!/usr/bin/python
#FLTK GUI CHAT SERVER by /EugeneOnTheEdge

import socket, random
from fltk import *

def send_onClick(widget):
	data = textInput.value()
	s.sendto(data, dataAddr[1])
	chatBrowser.add('You: '+data)
	textInput.value('')

def onReceive(fd):
	global dataAddr
	(data, addr) = s.recvfrom(bufferSize)
	dataAddr = (data,addr)
	sender = addr[0]
	if sender in contacts:
		sender = contacts[sender]
	chatBrowser.add(sender+': '+data)
	sendBtn.activate()
	
contacts = {'192.168.3.5': 'Silvy'}

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP
fileDescriptor = s.fileno()
dataAddr = None
bufferSize = 1024
host = '0.0.0.0'
port = 8755 #random.randint(1025,10000)
s.bind( (host,port) )

mainActivity = Fl_Window(300,300,400,822,"Chat server")
mainActivity.begin()

statusBox = Fl_Box(0,0,400,40)
statusBox.label('Waiting for the first message at '+str(port))

chatBrowser = Fl_Browser(0,40,400,710)
Fl.add_fd(fileDescriptor, onReceive)

textInput = Fl_Input(0,770,300,50)

sendBtn = Fl_Return_Button(320,770,80,50,"SEND")
sendBtn.callback(send_onClick)
sendBtn.deactivate()

mainActivity.end()

mainActivity.show()
Fl.run()
