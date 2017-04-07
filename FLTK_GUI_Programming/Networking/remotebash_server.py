#!/usr/bin/python
#Server-side

import subprocess, socket, random

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = '0.0.0.0'
port = random.randint(1025,10001)

print "Server on port",port
s.bind( (host,port) )

while True:
     (data,addr) = s.recvfrom(1024)
     print '\n\n'
     print addr[0],'>',data
     if data[0] == '$':
          terminal = subprocess.Popen(data[1:], universal_newlines=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          data = terminal.stdout.read()
          retcode = terminal.wait()
     s.sendto(data, addr)
     print data
