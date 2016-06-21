#!/usr/bin/python

letters = [ str(num-ord('A')+1)+' - '+chr(num) for num in range(ord('A'),ord('Z')+1) ]

for i in letters:
         print i
