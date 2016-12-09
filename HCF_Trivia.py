#!/usr/bin/python

from fltk import *
import cPickle as IO
import random

def start_onclick(self):
	global currentQuestion, possibleAns_label

	currentQuestion += 1
	answersToQ = actualSets[actualKeys[currentQuestion]].keys()
	questionNum.label( ('QUESTION #'+str(currentQuestion)) )
	questionBox.label(actualKeys[currentQuestion])
	possibleAns_label = []
	
	for ans in range(len(answersToQ)):
		answer = random.choice(answersToQ)
		getALocation = answersToQ.index(answer)
		del answersToQ[getALocation]
		possibleAns_label.append(answer)
		
	for ans in possibleAns_label:
		answers[possibleAns_label.index(ans)].label(ans)
		answers[possibleAns_label.index(ans)].redraw()
		
def answer_onclick(self):
	global userAnswer, checked, _userAnswer
	
	for button in answers:
		button.value(0)
		button.redraw()
	
	userAnswer = actualSets[questionBox.label()][self.label()]
	_userAnswer = self

	self.value(1)
	self.color2(fl_rgb_color(0,168,150))

def nextQuestion():
	global currentQuestion, possibleAns_label

	currentQuestion += 1
	answersToQ = actualSets[actualKeys[currentQuestion]].keys()
	questionNum.label( ('QUESTION #'+str(currentQuestion)) )
	questionBox.label(actualKeys[currentQuestion])
	questionNum.color(fl_rgb_color(0,168,150))
	possibleAns_label = []
	
	for ans in range(len(answersToQ)):
		answer = random.choice(answersToQ)
		getALocation = answersToQ.index(answer)
		del answersToQ[getALocation]
		possibleAns_label.append(answer)
		
	for ans in possibleAns_label:
		answers[possibleAns_label.index(ans)].label(ans)
		answers[possibleAns_label.index(ans)].value(0)
		answers[possibleAns_label.index(ans)].redraw()
		
def check_or_next_onclick(self):
	global userAnswer, score, checked
	
	if not checked:
		if userAnswer is True: #I know I can do <code> if userAnswer: </code>, but I'm english-nifing the code here!
			score += 1
			questionNum.label('Yay, you got it riteee!')
			questionNum.color(fl_rgb_color(122,184,0))
			_userAnswer.color2(fl_rgb_color(122,184,0))
		else:
			questionNum.label('Aiya, that was wrong..')
			questionNum.color(fl_rgb_color(237,123,6))
			_userAnswer.color2(fl_rgb_color(237,123,6))
		_userAnswer.redraw()
		checked = True
		self.label('NEXT QUESTION')
	else:
		checked = False
		nextQuestion()
	print currentQuestion
	userAnswer = None

#Variables
sets = {'In what city was Jesus born??': { 'Seattle': False, 'Vancouver': False, 'Jerusalem':True, 'Beijing':False } ,
		'What was the purpose of Jesus coming to Earth??': {'To die for us': True, 'To become rich and get rid of the kings at that time': False, 'To become well-known all over the internet': False, 'To kill all bad people on Earth': False },
		'Fill in the blank: "But I say unto you, Love your _________, ..." -Matthew 5:44': { 'girlfriend/boyfriend/hubby/wifey': False, 'parents': False, 'friends': False, 'enemies': True },
		'With 5 fish and 2 loaves of bread, how many people did Jesus feed??': { '1000 people': False, '2500 people': False, '5000 people': True, '7500 people': False },
		'How did Jesus die??': { 'He was crucified on the cross': True, 'He had a rickshaw accident': False, 'His girlfriend dumped him and he commited suicide later on': False, 'He had an uncurable brain and lung cancer, in addition to kidney failure and heart attack': False },
		'Fill in the blank: "For God so loved the world, he gave his one and only ______ (Jesus Christ),  \nthat whoever believes in him shall not perish but have eternal life. - John 3:16"': { 'son': True, '$100 bill': False, 'friend': False, 'self': False }
		}
keys = sets.keys()
userAnswer = None
_userAnswer = None
checked = False
actualSets = {}
questions = 4
btn_boxtype = FL_ROUND_UP_BOX
getWidth = Fl.w()
getHeight = Fl.h()
windowW = 1000
windowH = 680
currentQuestion = 0
possibleAns_label = []
score = 0

for numofquestions in range(questions):
	getQuestion = random.choice(keys)
	getQLocation = keys.index(getQuestion)
	del keys[getQLocation]
	actualSets[getQuestion] = sets[getQuestion]

_actualKeys = actualSets.keys()
actualKeys = []

for count in range(len(_actualKeys)):
	question = random.choice(_actualKeys)
	getQLocation = _actualKeys.index(question)
	del _actualKeys[getQLocation]
	actualKeys.append(question)

print actualKeys

#-----------

startActivity = Fl_Window( ((getWidth-windowW)/2), ((getHeight-windowH)/2), windowW, windowH, "Hamber Christian Fellowship Trivia System")
startActivity.begin()

startBtn = Fl_Button(100,485,800,60,"START")
startBtn.color(fl_rgb_color(0,168,150))

startActivity.end()
window = Fl_Window( ((getWidth-windowW)/2), ((getHeight-windowH)/2), windowW, windowH, "Hamber Christian Fellowship Trivia System")
window.begin()

questionNum = Fl_Box(0,0,1000,150, ("QUESTION #"))
questionNum.box(FL_FLAT_BOX)
questionNum.color(fl_rgb_color(0,168,150))
questionNum.labelsize(45)
questionNum.labelcolor(FL_WHITE)

questionBox = Fl_Box(100,95,800,200,'QUESTION GOES HERE')

nextQ = Fl_Button(800,605,175,50,"CHECK ANSWER")
nextQ.box(btn_boxtype)
nextQ.color(fl_rgb_color(166,228,26))
nextQ.labelcolor(FL_WHITE)
nextQ.callback(check_or_next_onclick)

answer1 = Fl_Button(100,245,800,60,"ANSWER 1")
answer1.box(btn_boxtype)
answer1.callback(answer_onclick)

answer2 = Fl_Button(100,325,800,60,"ANSWER 2")
answer2.box(btn_boxtype)
answer2.callback(answer_onclick)

answer3 = Fl_Button(100,405,800,60,"ANSWER 3")
answer3.box(btn_boxtype)
answer3.callback(answer_onclick)

answer4 = Fl_Button(100,485,800,60,"ANSWER 4")
answer4.box(btn_boxtype)
answer4.callback(answer_onclick)

answers = [answer1,answer2,answer3,answer4]

window.end()

start_onclick(None)

window.show()

Fl.scheme('gtk+')
Fl.run()	
