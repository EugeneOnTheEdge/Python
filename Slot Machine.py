#!/usr/bin/python

from fltk import *
import random
import time

def mix(self):
	wintimes = 0
	repetition = int(repInput.value())
	difficultyValue = int(DifficultySlider.value())
	
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
		else:
			getImg2 = random.choice(pics)
			getImg3 = random.choice(pics)
	
		if getImg1 == getImg2 == getImg3:
			print repeat,'>>> WON <<<'
			wintimes += 1.0
		else:
			print repeat
	
	print "Winning chance %.3f%%: %i WINS, %i REPs.\n\n\n\n\n\n" % ((wintimes/repetition)*100, wintimes, repetition)
	
	imgUI1.image(getImg1)
	imgUI2.image(getImg2)
	imgUI3.image(getImg3)
		
	imgUI1.redraw()
	imgUI2.redraw()
	imgUI3.redraw()	
		
def DifficultySlider_Listener(self):
	DifficultySlider.label("                                                                                      ")
	difficultyValue = int(DifficultySlider.value())
	if difficultyValue < 0:
		mode = 'LOSE'
		difficultyValue *= -1
	elif difficultyValue > 0:
		mode = 'WIN'
	else:
		mode = 'NORMAL'
	if difficultyValue != 0:
		DifficultySlider.label( ( ("Difficulty: %1.2f%% chance to "+mode+"!") % (difficultyValue/(maxBound*1.0) * 100) ) )
	else:
		DifficultySlider.label("Difficulty: NORMAL")
        
def PullSlider_Listener(self):
    if PullSlider.value() == 1.0:
        mix()
        PullSlider.value(0.0)

mode ='NORMAL'
difficultyValue = 0  
window = Fl_Window(100,200,1080,720,"Slot Machine")
window.begin()

pic1 = Fl_JPEG_Image('Mr Ark.jpg')
pic2 = Fl_JPEG_Image('doge.jpg')
pic3 = Fl_JPEG_Image('cat.jpg')
pic4 = Fl_JPEG_Image('harambe.jpg')
pic5 = Fl_JPEG_Image('ppap.jpg')
pic6 = Fl_JPEG_Image('trump.jpg')

y = 125

imgUI1 = Fl_Button(165,y,200,200)
imgUI2 = Fl_Button(420,y,200,200)
imgUI3 = Fl_Button(675,y,200,200)

repInput = Fl_Input(300,450,600,60,"Auto-Roll Reps:")
repInput.value(str(1))

maxBound = 10
minBound = -10
DifficultySlider = Fl_Slider(200,600,640,60, "DIFFICULTY")
DifficultySlider.bounds(minBound,maxBound)
DifficultySlider.type(FL_HOR_NICE_SLIDER)
DifficultySlider.value(0)

PullSlider = Fl_Return_Button(940,50,75,350, "PULL")
#PullSlider.type(FL_VERT_NICE_SLIDER)
PullSlider.callback(mix)

DifficultySlider.callback(DifficultySlider_Listener)

pics = [pic1,pic2,pic3,pic4,pic5,pic6]

imgUI1.image(random.choice(pics))
imgUI2.image(random.choice(pics))
imgUI3.image(random.choice(pics))

window.end()
window.show()
Fl.run()
