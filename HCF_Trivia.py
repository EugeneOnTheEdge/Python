#!/usr/bin/python

from fltk import *
import cPickle as IO
import random

def start_onclick(self):
	global userName, currentQuestion
	currentQuestion = -1
	if anonBtn.value() == 0:
		userName = nameInput.value().lstrip().rstrip()
	else:
		userName = anonBtn.label()
	startActivity.hide()
	nextQuestion()
	questionsActivity.show()
	anonBtn.value(0)
	nameInput.activate()
	nameInput.value('')
	Fl.remove_timeout(check_name_value)
	
def anon_onclick(self):
	global userName
	if self.value() == 0:
		userName = self.label()
		self.value(1)
		self.color2(FL_RED)
		nameInput.deactivate()
	else:
		userName = nameInput.value()
		self.value(0)
		nameInput.activate()
		
def answer_onclick(self,arg2=None):
	global userAnswer, checked, _userAnswer
	
	for button in answers:
		button.value(0)
		button.redraw()
	
	userAnswer = actualSets[questionBox.label()][self.label()]
	_userAnswer = self

	self.value(1)
	self.color2(fl_rgb_color(0,168,150))

def nextQuestion():
	global currentQuestion, possibleAns_label, highscore, tries
	currentQuestion += 1
	tries = 0
	for ansBtn in answers:
		ansBtn.callback(answer_onclick)
		ansBtn.color(fl_rgb_color(192,192,192))
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
		if score >= 5:
			if score >= 8:
				restartBtn.label('YEEEEEE, HOW MANY CANDEE CANES DO I GETTTT???!!')
			else:
				restartBtn.label('YEE, HOW MANY CANDY CANE(S) DO I GET??!')
		else:
			restartBtn.label('AIYA, DO I STILL MA CANDY CANE(S) MATE?!')
		_score = 'not the highest'
		for name in highscore:
			if score > highscore[name]:
				_highscore = {}
				_highscore[userName] = score
				_score = 'the highest'
			elif score == highscore[name]:
				_score = 'same as the heighest'
		if _score is 'the highest':
			highscore = _highscore
		elif _score is 'same as the heighest':
			highscore[userName] = score
		database = open('hcf_trv.dat','w')
		IO.dump(highscore,database)
		database.close()
		questionsActivity.hide()
		scoreBox.labelcolor(FL_GREEN)
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
			checked = True
			_userAnswer.redraw()
			self.label('NEXT QUESTION')
			for answerBtn in answers:
				answerBtn.callback(do_nothing,True) #Refer to the next function defined in the code.
		elif userAnswer is False:
			questionNum.label('Aiya, that was wrong..')
			questionNum.color(fl_rgb_color(237,123,6))
			_userAnswer.color2(fl_rgb_color(237,123,6))
			checked = True
			_userAnswer.redraw()
			self.label('NEXT QUESTION')
			for answerBtn in answers:
				if actualSets[actualKeys[currentQuestion]][answerBtn.label()]:
					answerBtn.color(fl_rgb_color(40,180,115))
					answerBtn.redraw()
				answerBtn.callback(do_nothing,False) #Refer to the next function defined in the code.
	else:
		checked = False
		nextQuestion()
	userAnswer = None

def do_nothing(self,answer):
	global tries
	if answer is True: #again, just English-nifying the code here..
		pass
	else:
		tries += 1
		if tries == 1:
			msg = "Hey, cheatin' by changing answer\n ain't allowed!"
		elif tries == 2:
			msg = "Mate, I told ya not to cheat! \nFYI, Cheating is a sin!"
		else:
			msg = "I hate--no, I LOVE ya, mate!\n*Christians aren't supposed to hate each other.*"
		questionNum.label(msg)
	
def check_name_value():
	global userName
	if anonBtn.value() == 1:
		startBtn.color(fl_rgb_color(76,176,80))
		startBtn.activate()
		startBtn.label('START as Anonymous')
	else:
		if nameInput.value().lstrip() == '':
			startBtn.color(fl_rgb_color(243,66,33))
			startBtn.deactivate()
			startBtn.label("Enter your name / if you prefer to be anonymous")
		else:
			startBtn.color(fl_rgb_color(76,176,80))
			startBtn.activate()
			startBtn.label(('START as '+nameInput.value().lstrip().rstrip()))
	startBtn.redraw()
	Fl.repeat_timeout(0.07,check_name_value)

def refresh():
	global userName, keys, userAnswer, _userAnswer, checked, actualSets, score, possibleAns_label, actualKeys, _actualKeys, highscore
	userName = None
	keys = sets.keys()
	userAnswer = None
	_userAnswer = None
	checked = False
	actualSets = {}
	score = 0
	possibleAns_label = []
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
	
	highscoreBrowser.clear()
	for name in highscore:
		if name != '':
			highscoreBrowser.add((name+':  '+str(highscore[name])))

def restart(self):
	if score >= 5:
		if score >= 8:
			restartBtn.label('YEEEEEEEEE, HOW MANY CANDEE CANES DO I GETTTT???!!')
			msg = 'Yeee, '+userName+', you earned yourself 3 candy canes!!'
		else:
			restartBtn.label('YEE, DO I GET ANY CANDY CANESSS??!')
			msg = 'Of course, '+userName+', you deserve 2 candy canes!!'
	else:
		restartBtn.label('AIYA, DO I STILL GET MA CANDY CANE(S) MATE?!')
		msg = 'It\'s okay, you still you get a candy cane! Well, you can always try again later!'
	restartBtn.redraw()
	fl_alert(msg)
	refresh()
	scoreActivity.hide()
	Fl.add_timeout(0.1,check_name_value)
	startActivity.show()

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
		'What do B.C. and A.D. (like in the context of time, i.e. 100 B.C. or 2016 A.D.) stand for??': {'Before Christ (BC) and Anno Domini (AD, stands for \'In the year of the Lord\' in Latin)': True, 'Before Crocodiles (BC) and After Dinosaurs (AD)': False, 'Before Christianity (BC) and After Domination (AD)':False, 'Before Clapstain (BC) and After Drackobranka (AD)': False }, 
		'What\'s the last book in the Bible called??': {'Revelation':True, 'Genesis':False, 'Glorify':False, 'The Next Coming':False },
		'What did the small David kill the giant, strong Goliath with??': {'A sling and a rock':True, 'Words of love':False, 'His badass martial art skills':False, 'A foot-long sword made of hardened metal':False },\
		'What is the true meaning of Emmanuel??': { 'God with us':True, 'I am one of God\'s children':False, 'The power of God to the fullest':False, 'God reigns on every nation through the ages and every generation, from the nothingness to the end of time.':False },
		'What is the LONGest chapter in the Bible??': {'Psalm 119':True, 'Matthew 52':False, 'Merkandras 2':False, 'Psalm 117':False },
		'What is the SHORTest chapter in the Bible??': {'Psalm 117':True, 'Psalm 119':False, 'Exodus 42':False, 'Psalm 207':False },
		'What is (/are) the key(s) points that differentiate(s) Christianity from other religions??': {'Revenge evil with kindness; love our enemies':False, 'Our God died, rose again on the 3rd day, and was ascended to heaven':False, 'Anyone who believes in the name of Jesus Christ will be saved, no matter what':False, 'All of the other options':True }
		}

print (str(len(sets.keys())) + ' questions.')
userName = None
keys = sets.keys()
userAnswer = None
_userAnswer = None
checked = False
actualSets = {}
score = 0
currentQuestion = -1
possibleAns_label = []
questions = 10
tries = 0
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

#Default properties

btn_boxtype = FL_ROUND_UP_BOX
getWidth = Fl.w()
getHeight = Fl.h()
questionsActivityW = 1000
questionsActivityH = 680

#-----------
try:
	database = open('hcf_trv.dat','r')
	highscore = IO.load(database)
except:
	database = open('hcf_trv.dat','w')
	highscore = {'':0}
	print '>>> NEW DATABASE HAS BEEN CREATED.'
database.close()

#-------------------
startActivity = Fl_Window( ((getWidth-questionsActivityW-250)/2), ((getHeight-questionsActivityH)/2)+10, questionsActivityW+250, questionsActivityH, "Hamber Christian Fellowship Trivia System")
startActivity.begin()
startActivity.color(fl_rgb_color(0,157,224))

helloBox = Fl_Box(0,170,questionsActivityW-30,300,'Christianity Trivia')
helloBox.labelsize(80)
helloBox.labelcolor(FL_WHITE)

tBox = Fl_Box(-10,50,questionsActivityW-40,100,'FREE CANDY CANE(s)!!')
tBox.labelcolor(fl_rgb_color(255,255,255))
tBox.labelsize(75)
tBox2 = Fl_Box(0,80,questionsActivityW-30,200,'Base reward = 1 candy cane (for just answering the questions)\nGet at least 5 questions right = 2 candy canes\nGet at least 8 questions right = 3 candy canes')
tBox2.labelsize(25)

highscoreBrowser = Fl_Browser(910,140,300,450)
highscoreBrowser.color(fl_rgb_color(0,157,224))
for name in highscore:
	if name != '':
		highscoreBrowser.add((name+':  '+str(highscore[name])))
		
highscore_textbox = Fl_Box(910,75,300,60,"HIGHSCOREs")
highscore_textbox.labelsize(45)
highscore_textbox.box(FL_FLAT_BOX)
highscore_textbox.color(fl_rgb_color(0,157,224))

nameInput = Fl_Input(350,430,145,25,'Name: ')
nameInput.value('')
anonBtn = Fl_Button(505,430,100,25,'Anonymous')
anonBtn.callback(anon_onclick)

startBtn = Fl_Return_Button(70,485,800,100,"Enter your name / if you prefer to be anonymous")
startBtn.color(fl_rgb_color(0,110,180))
startBtn.labelcolor(FL_WHITE)
startBtn.box(btn_boxtype)
startBtn.labelsize(22)
startBtn.callback(start_onclick)

startActivity.end()
#------------------
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

restartBtn = Fl_Button(150,540,questionsActivityH,60)
restartBtn.callback(restart)
restartBtn.box(FL_ROUND_UP_BOX)

scoreActivity.end()
#------------------
questionsActivity = Fl_Window( ((getWidth-questionsActivityW)/2), ((getHeight-questionsActivityH)/2), questionsActivityW, questionsActivityH, "Hamber Christian Fellowship Trivia System")
questionsActivity.begin()

questionNum = Fl_Box(0,0,1000,150, ("QUESTION #"))
questionNum.box(FL_FLAT_BOX)
questionNum.color(fl_rgb_color(0,168,150))
questionNum.labelsize(40)
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

Fl.add_timeout(0.05,check_name_value)
Fl.scheme('gtk+')
Fl.run()
