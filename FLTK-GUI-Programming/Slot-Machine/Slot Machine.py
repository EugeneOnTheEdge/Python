#!/usr/bin/python

from fltk import *
import random
import time

def mix(self):
	betAmount = int(BetInput.value())
	_cash = cash[0]
	wintimes = 0
	repetition = int(AutoRollInput.value())
	difficultyValue = int(DifficultySlider.value())
	cashDV = int(DifficultySlider.value())
	
	if betAmount <= 0:
		return
	if (_cash - betAmount) < 0:
		return
	if repetition <= 0:
		diffZero_ErrorHandler()
		return
	
	if difficultyValue < 0:
		mode = 'LOSE'
		difficultyValue = difficultyValue * -1
	elif difficultyValue > 0:
		mode = 'WIN'
	else:
		mode = 'NORMAL'
	
	toWin = range(1, difficultyValue+1)	
	getImg1 = random.choice(pics)
	chances = range(1, maxBound+1)
	
	for repeat in range(1,repetition+1):
		if mode != 'NORMAL':
			if mode == 'WIN':
				for x in range(2,4):
					getNumber = random.choice(chances)
					if getNumber in toWin:
						if x == 2:
							getImg2 = getImg1
						if x == 3:
							getImg3 = getImg1
					else:
						if x == 2:
							getImg2 = random.choice(pics)
						if x == 3:
							getImg3 = random.choice(pics)
				cashToGet = betAmount + betAmount * (0.05*(-(cashDV))+0.55)
				
			elif mode == 'LOSE':
				for x in range(2,4):
					getNumber = random.choice(chances)
					if getNumber in toWin:
						toPick = pics[:pics.index(getImg1)]
						
						for pic in pics[(pics.index(getImg1)+1):]:
							toPick.append(pic)
						
						if x == 2:
							getImg2 = random.choice(toPick)
						if x == 3:
							getImg3 = random.choice(toPick)
					else:
						if x == 2:
							getImg2 = random.choice(pics)
						if x == 3:
							getImg3 = random.choice(pics)
				cashToGet = betAmount + betAmount * ((-(cashDV))*10+10)
				
		else:
			getImg2 = random.choice(pics)
			getImg3 = random.choice(pics)
			cashToGet = betAmount + betAmount * 3
	
		if getImg1 == getImg2 == getImg3:
			print repeat,'<<< WON >>>'	
			wintimes += 1.0
			_cash += cashToGet
			
		else:
			print repeat
			_cash -= betAmount
	
	imgUI1.image(getImg1)
	imgUI2.image(getImg2)
	imgUI3.image(getImg3)
		
	imgUI1.redraw()
	imgUI2.redraw()
	imgUI3.redraw()
	
	#The next 2 lines of codes will have to do with GLOBAL-LOCAL VARIABLE thingy..
	cash[0] = _cash
	cashRefresh(_cash)		
	
	if _cash < 0:
		gameOver.show()
		
	print "Winning chance %.2f%%: %i WINS, %i REPs.\n\n\n\n\n\n" % ((wintimes/repetition)*100, wintimes, repetition)
		
def DifficultySlider_Listener(self):
	DifficultySlider.label("                                                                                                      ")
	difficultyValue = int(DifficultySlider.value())
	if difficultyValue < 0:
		mode = 'LOSE'
		difficultyValue *= -1
	elif difficultyValue > 0:
		mode = 'WIN'
	else:
		mode = 'NORMAL'
	if difficultyValue != 0:
		if mode == 'WIN':
			DifficultySlider.label( ( ("DIFFICULTY HACK: %.2f%% chance to "+mode+"!") % (difficultyValue/(maxBound*1.0) * 100) ) )
		else:
			DifficultySlider.label( ( ("DIFFICULTY HACK: %.2f%% more chance to "+mode+"!") % (difficultyValue/(maxBound*1.0) * 100) ) )
	else:
		DifficultySlider.label("Difficulty Hack: OFF")
        
def PullSlider_Listener(self):
    if PullSlider.value() == 1.0:
        mix()
        PullSlider.value(0.0)

def diffZero_ErrorHandler():
	aboveZero_win.show()
	AutoRollInput.value('1')

def cashRefresh(money):
	cash[0] = money
	cashBox.label("$ %.2f" % cash[0])
	
def close_diffZero(self):	
	aboveZero_win.hide()
def close_betZero(self):
	betZero.hide()
mode ='NORMAL'
difficultyValue = 0  
cash = [20.0]

window = Fl_Window(100,200,1080,720,"Slot Machine")
window.begin()

mBox = Fl_Box(390,-10,300,100,"MONEY")
mBox.labeltype(FL_ENGRAVED_LABEL)
cashBox = Fl_Box(390,20,300,100)
cashBox.align(FL_ALIGN_CENTER)
cashRefresh(cash[0])

pic1 = Fl_JPEG_Image('Mr Ark.jpg')
pic2 = Fl_JPEG_Image('doge.jpg')
pic3 = Fl_JPEG_Image('cat.jpg')
pic4 = Fl_JPEG_Image('harambe.jpg')
pic5 = Fl_JPEG_Image('ppap.jpg')
pic6 = Fl_JPEG_Image('trump.jpg')

y = 125

imgUI1 = Fl_Box(165,y,200,200)
imgUI2 = Fl_Box(420,y,200,200)
imgUI3 = Fl_Box(675,y,200,200)

AutoRollTextBox = Fl_Box(200,425,300,20,"Auto-Roll:")
AutoRollInput = Fl_Input(200,450,300,60,None)
AutoRollInput.value(str(1))

BetTextBox = Fl_Box(540,425,300,20,"Bet ($):")
BetInput = Fl_Input(540,450,300,60,None)
BetInput.value(str(2))

maxBound = 10
minBound = -(maxBound)
DifficultySlider = Fl_Slider(200,600,640,60, "Difficulty Hack: OFF")
DifficultySlider.bounds(minBound,maxBound)
DifficultySlider.type(FL_HOR_NICE_SLIDER)
DifficultySlider.value(0)

PullSlider = Fl_Return_Button(940,50,75,350, "PULL")
#PullSlider.type(FL_VERT_NICE_SLIDER)
PullSlider.callback(mix)
PullSlider.box(FL_PLASTIC_UP_BOX)

DifficultySlider.callback(DifficultySlider_Listener)
DifficultySlider.box(FL_PLASTIC_UP_BOX)
DifficultySlider.labeltype(FL_ENGRAVED_LABEL)

pics = [pic1,pic2,pic3,pic4,pic5,pic6]

imgUI1.image(random.choice(pics))
imgUI2.image(random.choice(pics))
imgUI3.image(random.choice(pics))
window.end()

aboveZero_win = Fl_Window(500,320,400,200,"Error")
aboveZero_win.begin()
closeBtn = Fl_Return_Button(250,135,100,30,"Alright!")
closeBtn.callback(close_diffZero)
errorText = Fl_Box(25,0,350,150,"Mate, you gotta enter the Auto-Roll value \nBIGGER THAN 0. I hope you haven't forgotten \nbout real #s..")
aboveZero_win.end()

betZero = Fl_Window(500,320,400,200,"Error")
betZero.begin()
errorText = Fl_Box(25,0,350,150,"Yo, how can you play without betting?!\n Check ur bet amount and \nuse ur logic, mate!")
closeBtn = Fl_Return_Button(250,135,100,30,"I will!")
betZero.end()
betZero.show()

noMoney = Fl_Window(500,320,400,200,"GAME OVER")
noMoney.begin()
errorText = Fl_Box(25,0,350,150,"Nope. Go home, lazy. \nYou wasted all ur money already. \nYes, go outside and get a job.")
closeBtn = Fl_Return_Button(100,145,200,30,"Oh shoot I'm poor now")
noMoney.end()
noMoney.show()
print "/!\DO NOT CLOSE THIS (TERMINAL) WINDOW AS IT WILL CLOSE THE MAIN PROGRAM AS WELL. /!\\\n\n"

window.show()
Fl.run()
