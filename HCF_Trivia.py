#!/usr/bin/python

from fltk import *
import cPickle as IO
import random

def start_onclick(self):
	startActivity.hide()
	nextQuestion()
	questionsActivity.show()
	
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
	if currentQuestion != questions:
		answersToQ = actualSets[actualKeys[currentQuestion]].keys()
		questionNum.label( ('QUESTION #'+str(currentQuestion+1)) )
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
	else:
		questionsActivity.hide()
		scoreBox.label(str(score))
		outofBox.label((' /'+str(questions)))
		scoreActivity.show()
		
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
	userAnswer = None

def cb(w):
	if nameInput.value() == '':
		startBtn.deactivate()
		print 'deactivated'
	else:
		startBtn.activate()
		print 'activated' 

def cb_repeat():
	b.do_callback()
			
#Variables
sets = {'In what city was Jesus born??': { 'Seattle': False, 'Vancouver': False, 'Bethlehem':True, 'Beijing':False } ,
		'What was the purpose of Jesus coming to Earth??': {'To die for us': True, 'To become rich and get rid of the kings at that time': False, 'To become well-known all over the internet': False, 'To kill all bad people on Earth': False },
		'Fill in the blank: "But I say unto you, Love your _________, ..." -Matthew 5:44': { 'girlfriend/boyfriend/hubby/wifey': False, 'parents': False, 'friends': False, 'enemies': True },
		'With 5 fish and 2 loaves of bread, how many people did Jesus feed??': { '1257 people': False, '53 people': False, '5000 people': True, '7 people': False },
		'How did Jesus die??': { 'He was crucified on the cross': True, 'He had a rickshaw accident': False, 'His girlfriend dumped him and he commited suicide later on': False, 'He had an uncurable brain and lung cancer, in addition to kidney failure and heart attack': False },
		'Fill in the blank: "For God so loved the world, he gave his one and only ______ (Jesus Christ),  \nthat whoever believes in him shall not perish but have eternal life. - John 3:16"': { 'son': True, '$100 bill': False, 'friend': False, 'self': False },
		'When was Hamber Christian Fellowship founded in??': { '1973': True, '2011': False, '1957': False, '2001': False },
		'Who is Jesus\' mother??': { 'Mary': True, 'Maria': False, 'Marie': False, 'Mario': False },
		'How old was Jesus when he died??': { '33-34 years old': True, 'in his mid 20s': False, '18-19 years old': False, '46-47 years old': False },
		'How many chapters and verses are there in the Bible??': { '1,189 chapters and 31,102 verses': True, '2,147 chapters and 48,294 verses': False, '827 chapters and 28,255 verses': False, '2,492 chapters and 52,001 verses': False },
		'How many disciples (kinda like students) did Jesus have??': { '12':True, '1':False, '27':False, '77': False },
		'Who, INDIRECTLY saying, planned Jesus\' death??': { 'God': True, 'The Romans, Jewish leaders, and Caiaphas': False, 'The Chinese and their communists': False, 'The programmer behind this game': False },
		'One of the answers was one Jesus\' disciples. Who was he??': { 'Matthew': True, 'Matthias': False, 'Mattias': False, 'Helmbrokatras': False },
		'What do B.C. and A.D. (like in the context of time, i.e. 100 B.C. or 2016 A.D.) stand for??': {'Before Christ (BC) and Anno Domini (AD, stands for \'In the year of the Lord\' in Latin)': True, 'Before Crocodiles (BC) and After Dinosaurs (AD)': False, 'Before Christianity (BC) and After Domination (AD)':False, 'Before Clapstain (BC) and After Drackobranka (AD)': False } 
		}
		
highscore = []	
keys = sets.keys()
userAnswer = None
_userAnswer = None
checked = False
actualSets = {}
questions = 5
btn_boxtype = FL_ROUND_UP_BOX
getWidth = Fl.w()
getHeight = Fl.h()
questionsActivityW = 1000
questionsActivityH = 680
currentQuestion = -1
possibleAns_label = []
score = 10

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

#-----------
try:
	database = open('hcf_trv.dat','r')
except:
	database = open('hcf_trv.dat','w')
	print '>>> NEW DATABASE HAS BEEN CREATED.'
	
startActivity = Fl_Window( ((getWidth-questionsActivityW)/2), ((getHeight-questionsActivityH)/2), questionsActivityW, questionsActivityH, "Hamber Christian Fellowship Trivia System")
startActivity.begin()
startActivity.color(fl_rgb_color(0,157,224))

b = Fl_Button(0,0,10,10)
b.callback(cb)

helloBox = Fl_Box(0,170,questionsActivityW,100,'Christian History\nTrivia')
helloBox.labelsize(70)
helloBox.labelcolor(FL_WHITE)

nameInput = Fl_Input(425,430,200,25,'Name: ')
nameInput.value('name')

startBtn = Fl_Button(100,485,800,60,"START")
startBtn.color(fl_rgb_color(0,110,180))
startBtn.labelcolor(FL_WHITE)
startBtn.box(btn_boxtype)
startBtn.callback(start_onclick)

startActivity.end()

scoreActivity = Fl_Window( ((getWidth-questionsActivityW)/2), ((getHeight-questionsActivityH)/2), questionsActivityW, questionsActivityH, "Hamber Christian Fellowship Trivia System")
scoreActivity.begin()
scoreActivity.color(fl_rgb_color(0,157,224))

titleBox = Fl_Box(0,50,questionsActivityW,100,'You scored:')
titleBox.labelsize(60)
titleBox.labelcolor(FL_WHITE)

scoreBox = Fl_Box(0,285,questionsActivityW,100)
scoreBox.labelsize(270)
scoreBox.labelcolor(FL_WHITE)

outofBox = Fl_Box(700,335,120,120,(' /'+str(questions)))
outofBox.labelsize(105)
outofBox.labelcolor(FL_WHITE)

scoreActivity.end()

questionsActivity = Fl_Window( ((getWidth-questionsActivityW)/2), ((getHeight-questionsActivityH)/2), questionsActivityW, questionsActivityH, "Hamber Christian Fellowship Trivia System")
questionsActivity.begin()

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

questionsActivity.end()
startActivity.show()

Fl.add_timeout(0.1,cb_repeat)
Fl.repeat_timeout(0.1,cb_repeat)
Fl.scheme('gtk+')
Fl.run()
