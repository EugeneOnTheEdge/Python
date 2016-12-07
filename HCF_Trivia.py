#!/usr/bin/python

from fltk import *
import cPickle as IO
import random

def nextQ(self):
	pass
	
#Variables
sets = {'In what city was Jesus born??': [ ['Seattle',0], ['Vancouver',0], ['Jerusalem',1], ['Beijing',0] ] ,
		'What was the purpose of Jesus coming to Earth??': [ ['To die for us',1], ['To become rich and get rid of the kings at that time',0], ['To become well-known all over the internet',0], ['To kill all bad people on Earth',0] ],
		'Fill in the blank: "But I say unto you, Love your _________, ..." -Matthew 5:44': [ ['girlfriend/boyfriend/hubby/wifey',0], ['parents',0], ['friends',0], ['enemies',1] ],
		'With 5 fish and 2 loaves of bread, how many people did Jesus feed??': [ ['1000 people',0], ['2500 people',0], ['5000 people', 0], ['7500 people', 1] ],
		'How did Jesus die??': [ ['He was crucified on the cross',1], ['He had a rickshaw accident',0], ['His girlfriend dumped him and commited suicide later on',0], ['He had an uncurable brain and lung cancer, in addition to kidney failure and heart attack',0] ],
		}
keys = sets.keys()
actualSets = {}
questions = 3
getWidth = Fl.w()
getHeight = Fl.h()
windowW = 800
windowH = 600

for numofquestions in range(questions):
	getQuestion = keys.pop(keys.index(random.choice(keys)))
	actualSets[getQuestion] = sets[getQuestion]

#-----------

window = Fl_Window( ((getWidth-windowW)/2), ((getHeight-windowH)/2), windowW, windowH, "Simon Says Simulator")
window.begin()

questionBox = Fl_Box(100,50,400,200,'QUESTION GOES HERE')
window.end()

window.show()
Fl.run()	
