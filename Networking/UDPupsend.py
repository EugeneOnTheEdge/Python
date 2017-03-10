#!/usr/bin/python
#CLIENT-send udp (User Datagram Protocol)

#NETWORKING 1

'''
	UDP: 'Fire-and-Forget' method
		When you send packets to the internet and it fails, it will not re-send the packets again.
		TCP will resend the packets until they get to the internet.
		In other words, TCP is easier to code, UDP is harder. UDP is lower-level (computer/hardware based).
	CHECK USED PORTS BY YOUR COMPUTER:
	$ netstat -pant
	
	CHECK YOUR IP ADDRESS:
	$ ip addr
	
'''

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creating a connection that can go out of our computer
#AF_INET: Address Family Internet, SOCK_DGRAM: UDP; SOCK_STREAM: TCP
#A socket obj represents one endpoint of a connection

host = sys.argv[1] #Address to send info; string
port = int(sys.argv[2]) #Port to send info; integer

line = raw_input() #send only once === blocking

#for line in sys.stdin: #sys.stdin is the keyboard  send many lines separated by ctrl+d
s.sendto(line,(host,port))
