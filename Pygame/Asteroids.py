#!/usr/bin/python
#All velocity units are in pixels/second

import pygame, random, math

class Asteroid(object):
	def __init__(self,angle,xPos,yPos):
		self.angle = angle
		self.xPos = xPos
		self.yPos = yPos
		self.xLength = 100
		self.yLength = 100 
		self.xVelocity = -(asteroidVelocity * math.sin(toRadian(self.angle)))
		self.yVelocity = -(asteroidVelocity * math.cos(toRadian(self.angle)))
		self.colour = ( random.randint(25,255), random.randint(25,255), random.randint(25,255) )
		self.size = random.randint(8,20)

class Meteor(object):
	def __init__(self):
		self.mSize = random.randint(50,100)
		self.mOriginalSize = self.mSize
		self.center = self.mSize/2
		self.xPos = random.randint(600,width-self.mSize)
		self.yPos = random.randint(0,height-self.mSize)
		self.xVelocity = random.randint(1,3)
		self.yVelocity = random.randint(1,3)
		if self.xPos <= width-self.mSize:
			self.yPos = random.randint(0,1)*(height-self.mSize)
		self.pic = pygame.image.load("meteor"+str(random.randint(1,3))+".png")
		self.pic = pygame.transform.scale(self.pic, (self.mSize,self.mSize))

class PowerUp(object):
	def __init__(self):
		self.size = 50
		self.img = random.choice(["freeze.png"])
		self.xPos = random.randint(600,width-self.size)
		self.yPos = random.randint(0,height-self.size)
		self.xVelocity = random.randint(1,3)
		self.yVelocity = random.randint(1,3)
		if self.xPos <= width-self.size:
			self.yPos = random.randint(0,1)*(height-self.size)
		self.addsHealth = 0
		self.addsFreeze = 0
		self.addsArmor = 0
		
		if self.img == "armor.png":
			self.addsArmor = 100
		elif self.img == "freeze.png":
			self.addsFreeze = 300 #5 seconds
		else:
			self.addsHealth = 100
		
		self.pic = pygame.image.load(self.img)
		self.pic = pygame.transform.scale(self.pic, (50,50))
		
def toRadian(degrees):
	return degrees * math.pi / 180.0
	
pygame.init()
width, height = 1250,900
size = [width,height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()
running = True

#Game Variables
asteroidVelocity = 20.0
health = 0
score = 0
speed = 7.5
freezetime = 0
deceleration = 0.980
acceleration = 0.035

#Drawables defining
ship = pygame.image.load("ship.png")
shipsize = 98
shipradius = shipsize/2
ship = pygame.transform.scale(ship, (shipsize,shipsize))
booster = pygame.image.load("booster.png")
healthFont = pygame.font.SysFont("monospace", 25)
asteroidFont = pygame.font.SysFont("monospace", 75)

addAngle = 0.0
xVelocity = 0.0
yVelocity = 0.0
relativeVelocity = 0.0

while running:
	while health > 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					addAngle = 4.0
				if event.key == pygame.K_RIGHT:
					addAngle = -4.0
				if event.key == pygame.K_UP:
					slowdown = False
					reverse = 1
				if event.key == pygame.K_DOWN:
					slowdown = False
					reverse = -1
					cruisecontrol = 'OFF'
					deceleration = 0.980
				if event.key == pygame.K_c:
					if cruisecontrol == 'OFF':
						cruisecontrol = 'ON'
						deceleration = 1.0
					else:
						cruisecontrol = 'OFF'
						deceleration = 0.980
						
				if event.key == pygame.K_SPACE:
					asteroids.append(Asteroid(angle,xPos,yPos))
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					addAngle = 0
				if event.key == pygame.K_RIGHT:
					addAngle = 0
				if event.key == pygame.K_UP:
					slowdown = True
				if event.key == pygame.K_DOWN:
					slowdown = True
		
		screen.fill( (0,0,0) )
		
		if len(meteors) == 0:
			meteorCount += 2
			for x in range(meteorCount):
				meteors.append(Meteor())
			for i in range(5):
				randnum = random.randint(1,3)
				_randnum = random.randint(1,3)
				if randnum == _randnum:
                                     powerups.append(PowerUp())
		if slowdown:
			relativeVelocity *= deceleration
		else:
			relativeVelocity += acceleration*speed*reverse
			if relativeVelocity > 15:
				relativeVelocity = 15
			elif relativeVelocity < -15:
				relativeVelocity = -15
					
		xPos += -(relativeVelocity * math.sin(toRadian(angle))) #radian
		yPos += -(relativeVelocity * math.cos(toRadian(angle)))
		angle += addAngle
		angle %= 360
		
		if relativeVelocity < 0:
			cruisecontrol = 'OFF'
			deceleration = 0.980
		
		for asteroid in asteroids:
			if (asteroid.xPos < 1250 and asteroid.xPos > 0) and (asteroid.yPos > 0 and asteroid.yPos < 800):
				pygame.draw.circle(screen, asteroid.colour, (asteroid.xPos,asteroid.yPos), asteroid.size)
				asteroid.xPos += asteroid.xVelocity
				asteroid.yPos += asteroid.yVelocity
			else:
				del asteroids[asteroids.index(asteroid)]
		
		if freezetime <= 0:
			for meteor in meteors:
				if meteor.yPos < 0 or meteor.yPos > height-meteor.mSize:
					meteor.yVelocity = -meteor.yVelocity
				if meteor.xPos < 0 or meteor.xPos > width-meteor.mSize:
					meteor.xVelocity = -meteor.xVelocity
				meteor.xPos += meteor.xVelocity
				meteor.yPos += meteor.yVelocity
				screen.blit(meteor.pic, (meteor.xPos,meteor.yPos))
		else:
			freezetime -= 1
			for meteor in meteors:
				screen.blit(meteor.pic, (meteor.xPos,meteor.yPos))
			
		for powerup in powerups:
			if powerup.yPos > height-powerup.size or powerup.yPos < 0+powerup.size:
				powerup.yVelocity = -powerup.yVelocity
			if powerup.xPos > width-powerup.size or powerup.xPos < 0+powerup.size:
				powerup.xVelocity = -powerup.xVelocity
			powerup.yPos += powerup.yVelocity
			powerup.xPos += powerup.xVelocity
			screen.blit(powerup.pic, (powerup.xPos, powerup.yPos))
			
		#Collision detection between ASTEROIDS and METEORS (ASTEROID IS BULLET, I should be renaming those, I know.)
		for asteroid in asteroids:
			for m in range(len(meteors)):
				try:
					distance = ((asteroid.xPos-(meteors[m].xPos+meteors[m].center))**2 + (asteroid.yPos-(meteors[m].yPos+meteors[m].center))**2)**0.5
					if asteroid.size + meteors[m].mSize/2 > distance:
						meteors[m].mSize -= asteroid.size
						del asteroids[asteroids.index(asteroid)]
						if meteors[m].mSize < 50:
							del meteors[m]
							score += meteors[m].mOriginalSize
						else:
							meteors[m].pic = pygame.transform.scale(meteors[m].pic, (meteors[m].mSize,meteors[m].mSize))
				except: #IndexError and ValueError
					pass
		
		#Collision detection between SHIP and METEORS
		for meteor in meteors:
			distance = ( (meteor.xPos-xPos)**2 + (meteor.yPos-yPos)**2 )**0.5
			
			if shipradius + meteor.mSize > distance:
				health -= meteor.mSize/5
				if int(health) > 0:
					meteors.remove(meteor)
		
		#Collision detection between SHIP and POWERUP
		for powerup in powerups:
			distance = ( (powerup.xPos-xPos)**2 + (powerup.yPos-yPos)**2 )**0.5
			
			if shipradius + powerup.size > distance:
				armor += powerup.addsArmor
				health += powerup.addsHealth
				freezetime = powerup.addsFreeze
				powerups.remove(powerup)

		if health > 100:
			health = 100
			
		rotatedShip = pygame.transform.rotate(ship, angle)
		rotatedRect = rotatedShip.get_rect()
		rotatedRect.center = (xPos,yPos)
		screen.blit(rotatedShip, rotatedRect)
		
		healthText = healthFont.render( ("Health: "+str(int(health))+"%"),1, (0,255,0) )
		armorText = healthFont.render( ("Armor: "+str(int(armor))+"%"),1, (0,255,0) )
		freezeText = healthFont.render( ("Freeze Time: %.1fs" % (freezetime/60.0)), 1, (0,255,0) )
		scoreText = healthFont.render( ("Score: "+str(score)+" pts"),1, (0,255,0) )
		_speed = relativeVelocity*60.0
		speedText = healthFont.render( ("Speed: %.1f pixels/sec" % _speed),1, (0,255,0) )
		headingText = healthFont.render( ("Heading: %i degrees" % angle), 1, (0,255,0) )
		ccText = healthFont.render( ("Cruise Ctrl: "+cruisecontrol), 1, (0,255,0) )
		screen.blit(ccText, (500,865))
		screen.blit(healthText, (0,0))
		screen.blit(freezeText, (800,0))
		screen.blit(armorText, (250,0))
		screen.blit(scoreText, (0,865))
		screen.blit(speedText, (800, 865))
		screen.blit(headingText, (450, 0))
		
		pygame.display.flip()
		clock.tick(60)
		
	while health <= 0:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					health = 100
		
		xPos = 400
		yPos = 400
		asteroids = []
		meteors = []
		powerups = []
		_health = ""
		slowdown = True
		cruisecontrol = 'OFF'
		meteorCount = 8
		angle = 0.0
		score = 0
		relativeVelocity = 0.0
		armor = 0
		
		asteroidText = asteroidFont.render('ASTEROIDS',1,(0,255,0))
		startText = healthFont.render('> Start <',1,(0,255,0))
		screen.blit(asteroidText, (425,250))
		screen.blit(startText, (525,400))

		pygame.display.flip()
		clock.tick(60)
