# This program is based on code from inventwithpython.com
import random
import sys
import math

cardinalDirections=['west','north','east','south']
difficulty=1

#Functions
def helpText():
	print('\n\nDragonQuest is a text based game created by Kyle Zufelt in Python.\n\
In this first chapter of the game, the user finds themselves on an island,\n\
and must find a way to escape to a larger nearby island before they run\n\
out of energy. The game combines elements of survivalism and memory.\n\
The player may interact with the software by typing simple phrases,\n\
for example "walk north" or "search body". The grid of the map is a\n\
square with a random number of cells to a side, generated each time the\n\
game starts. At any time during the game, the player may type "help" to\n\
re-display this message, or "quit" to quit.')

def recognizeAction():
	global boatFinished
	print('\nWhat do you do?')
	action = input()
	action = action.lower()
	actionVerb=action.split(' ',3)
	if (actionVerb[0]=='walk' or actionVerb[0]=='run' or actionVerb[0]=='hike' or actionVerb[0]=='head' or actionVerb[0]=='swim' or actionVerb[0]=='launch' or actionVerb[0]=='go') and len(actionVerb)>1:
		Walk(actionVerb[1])
	elif (warpCheat==1 and actionVerb[0]=='warp' and len(actionVerb)>2):
		Warp(actionVerb[1],actionVerb[2])
	elif (actionVerb[0]=='help'):
		helpText()
	elif (actionVerb[0]=='talk'):
		print('There is no one to talk to but the sand and the trees.')
	elif (actionVerb[0]=='hunt'):
		print('There are no animals to be seen, and the trees certainly don\'t look appetizing.')
	elif (actionVerb[0]=='dig'):
		print('Although the sandy ground would be easy to dig through, you are less interested\nin buried treasure, and more interested in getting off this island alive.')
	elif (actionVerb[0]=='eat' or actionVerb[0]=='taste'):
		eat(actionVerb[1])
	elif (actionVerb[0]=='fix' or actionVerb[0]=='work' or actionVerb[0]=='complete' or actionVerb[0]=='finish') and checkInventory('rock')==0 and playerLocation==Challenge2 and boatFinished==0:
		print('Your hands will not be of much use against this hard wood.\nBetter find something hard and sharp.')
	elif (actionVerb[0]=='fix' or actionVerb[0]=='work' or actionVerb[0]=='complete' or actionVerb[0]=='finish' or actionVerb[0]=='build' or actionVerb[0]=='cut' or actionVerb[0]=='make') and checkInventory('rock')==1 and playerLocation==Challenge2 and boatFinished==0:
		print('You quickly carve out the remaining features necessary to complete the boat.\nIt is hard work, but fortunately you are building on the work of others.\nAs you finish, you use the rock to break a branch off another tree to use\nas a crude paddle. You place the paddle in the hollow of the log,\nand discard the chipped and fractured rock.\nNow all you need to do is LIFT the boat and carry it to the right beach,\nbut walking with the boat will be harder than walking by yourself.')
		checkEnergy()
		boatFinished=1
		removeItem('rock')
	elif (actionVerb[0]=='search' or actionVerb[0]=='look' or actionVerb[0]=='check' or actionVerb[0]=='open' or actionVerb[0]=='get' or actionVerb[0]=='pick' or actionVerb[0]=='lift') and len(actionVerb)>1:
		checkItem(actionVerb[1])
	elif (actionVerb[0]=='drop'):
		print('There\'s no use in dropping anything that might be of use.')
	elif (actionVerb[0]=='quit' or actionVerb[0]=='exit'):
		sys.exit()
	elif (actionVerb[0]=='cheat' and len(actionVerb)>1):
		cheatCode(actionVerb[1])
	else:
		print('Command not recognized.')

def Warp(X,Y):
	global playerLocation
	playerLocation=[int(X),int(Y)]
	if mapCheat==1:
		printMap()

def cheatCode(cheat):
	if cheat=='map':
		global mapCheat
		if mapCheat==0:
			mapCheat=1
			print('Map cheat activated.')
		elif mapCheat==1:
			mapCheat=0
			print('Map cheat deactivated.')
	elif cheat=='warp':
		global warpCheat
		if warpCheat==0:
			warpCheat=1
			print('Warp cheat activated.')
		elif warpCheat==1:
			warpCheat=0
			print('Warp cheat deactivated.')
	else:
		print('Cheat code not recognized.')

def printMap():
	if mapCheat==1:
		columnNumber=1
		rowNumber=mapSize
		for i in range(0,2*mapSize+2):#Row iterator
			mapRow=''
			for j in range(0,2*mapSize+2):#Column iterator
				if (j==0 and i%2!=0 and i<2*mapSize+1):
					mapRow+=str(rowNumber)
					rowNumber-=1
				elif (i==2*mapSize+1 and j%2==0 and j>1):
					mapRow+=str(columnNumber)
					columnNumber+=1
				elif i%2==0:
					mapRow+='-'
				elif j%2!=0:
					mapRow+='|'
				elif (i==2*(mapSize-playerLocation[1])+1 and j==2*(playerLocation[0])):
					mapRow+='X'
				elif (i==2*(mapSize-Challenge1[1])+1 and j==2*(Challenge1[0])):
					mapRow+='F'
				elif (i==2*(mapSize-Challenge2[1])+1 and j==2*(Challenge2[0])):
					mapRow+='B'
				elif (i==2*(mapSize-Challenge3[1])+1 and j==2*(Challenge3[0])):
					mapRow+='R'
				else:
					mapRow+=' '
			print(mapRow)
	else:
		for i in range(0,2*mapSize):
			mapRow=''
			if i%2==0:
				for j in range(0,2*mapSize):#Column iterator
					explored=0
					for x in playerExplored:
						if j%2==0 and ([j//2+1,mapSize-i/2+1]==x or [j//2+1,mapSize-i/2]==x or [j//2,mapSize-i/2+1]==x or [j//2,mapSize-i/2]==x):
							explored=1
						elif j%2!=0 and ([j//2+1,mapSize-i/2+1]==x or [j//2+1,mapSize-i/2]==x):
							explored=1
					if explored==1:
						mapRow+="-"
					else:
						mapRow+=" "
				print(mapRow)
			else:
				for j in range(0,2*mapSize):
					explored=0
					for x in playerExplored:
						if j%2==0 and ([j//2+1,mapSize-i//2]==x or [j//2,mapSize-i//2]==x):
							explored=1
					if explored==1:
						mapRow+="|"
					elif j%2!=0 and [j//2+1,mapSize-i//2]==playerLocation[:]:
						mapRow+="X"
					else:
						mapRow+=" "
				print(mapRow)



def Walk(direction):
	global playerLocation
	global previousLocation
	previousLocation=playerLocation[:]
	direction = direction.lower()
	if (direction != 'north' and direction != 'south' and direction != 'west' and direction != 'east'):
		print(str(direction) + ' is not a valid direction.')
	elif (direction == 'north' and playerLocation[1]<mapSize):
		print('You head north.')
		playerLocation[1]=playerLocation[1]+1
		checkLocation()
		checkEnergy()
		if checkInventory('boat')==1:
			checkEnergy()
	elif (direction == 'south' and playerLocation[1]>1):
		print('You head south.')
		playerLocation[1]=playerLocation[1]-1
		checkLocation()
		checkEnergy()
		if checkInventory('boat')==1:
			checkEnergy()
	elif (direction == 'west' and playerLocation[0]>1):
		print('You head west.')
		playerLocation[0]=playerLocation[0]-1
		checkLocation()
		checkEnergy()
		if checkInventory('boat')==1:
			checkEnergy()
	elif (direction == 'east' and playerLocation[0]<mapSize):
		print('You head east.')
		playerLocation[0]=playerLocation[0]+1
		checkLocation()
		checkEnergy()
		if checkInventory('boat')==1:
			checkEnergy()
	elif (direction == 'east' and playerLocation[0]==mapSize and checkInventory('boat')!=1) or (direction == 'south' and playerLocation[1]==1 and checkInventory('boat')!=1) or (direction == 'north' and playerLocation[1]==mapSize and checkInventory('boat')!=1) or (direction == 'west' and playerLocation[0]==1 and checkInventory('boat')!=1):
		print('You wade into the surf, but as you look into the water you see that it is\nteeming with jellyfish. To swim into the ocean would be suicide, even if you\nhad the strength to reach land. Dejected, you turn back to the beach,\nand hope that something on this island will help you escape.')
	elif (direction != cardinalDirections[victoryBeach] and checkInventory('boat')==1):
		print('Your tiny boat would not be of much use for a voyage into open waters. No,\nunless there was another island within sight, it would be better to just die\nhere where someone might eventually find your body.')
	elif (direction == cardinalDirections[victoryBeach] and checkInventory('boat')==1):
		print('You step into the boat, and begin paddling towards the distant island.\n\nYOU WIN\n\nYou had ' + str(playerEnergy) + ' steps left until you died.\n\nEnd Chapter I')
		if int(difficulty)==1:
			print('For a further challenge, see if you can beat the game on hard.')
		if int(difficulty)==2:
			print('Congratulations on beating the game on hard!\nFor a further challenge, see if you can figure out the cheat options built into the game.')
		global victory
		victory=1
	else:
		print('You cannot go ' + str(direction) + '.')
	if mapCheat==1:
		printMap()

def checkInventory(item):
	for x in inventory[:]:
		if x==item:
			return 1
	return 0

def checkItem(item):
	global Challenge1
	if (item=='inventory' and len(inventory)>0):
		print('You currently have the following items:\n')
		for x in inventory[:]:
			print(x)
	elif (item=='inventory' and len(inventory)==0):
		print('You have nothing with you but your clothes and your dry wit.')
	elif (item=='map'):
		printMap()
	elif (item=='body' and playerLocation==Challenge1 and checkInventory('berries')==0):
		print('You find a cluster of BERRIES in the dead man\'s pouch. The question is, since\n\
this man is cleary dead, would eating these berries give you much needed\n\
energy, or sap your remaining strength?\nYou add the BERRIES to your INVENTORY.')
		inventory.append('berries')
		Challenge1=[0,0]
	elif (playerLocation==Challenge3 and checkInventory('rock')==0):
		print('You pick up the rock, and even though you know it wouldn\'t be of any\nuse against a dragon, you feel a little more safe.\nYou add the ROCK to your INVENTORY.')
		inventory.append('rock')
	elif (item=='boat' or item=='canoe') and playerLocation==Challenge2 and boatFinished==1 and checkInventory('boat')==0:
		print('You lift the boat, and pray that the correct beach isn\'t too far away.\n')
		inventory.append('boat')
	elif (item=='boat' and playerLocation==Challenge2 and boatFinished==0 and checkInventory('boat')==0):
		print('No use moving the boat now. It is too heavy to be practical until you can finish carving it.\n')
	else:
		print('You find nothing worth taking with you.')

def eat(item):
	global playerEnergy
	if item=="body" and (playerLocation==Challenge2 or playerLocation==Challenge1):
		print('The village elders have the power to take you from your home, starve you, and\n\
inflict all manner of punishment on your body, but you are more than flesh\n\
and blood and bone. It would take much more than the demands of your body, or\n\
even the transitory demands of a mind enfeebled by hunger, to make you perform\n\
that depraved act.')
	elif checkInventory('berries')==1:
		number = random.randint(0,playerEnergy)
		if number<10:
			playerEnergy+=10
			print('Not bad. You certainly don\'t feel poisoned. If anything, you feel at least\nmarginally stronger.')
			removeItem('berries')
		else:
			print('\n"I don\'t feel so good."')
			input()
			print('You vomit on the sandy ground, and reflect on what a stupid experiment this\n\
was. In another situation, you may have recovered from this poison, but in\n\
your weakened state you no longer have the energy to continue, and you collapse\n\
in a piteous heap.\n\nGAME OVER')
			global victory
			victory=1

def removeItem(item):
	global inventory
	for x in range(len(inventory)):
		if inventory[x]==item:
			inventory[x:x+1]=[]
			return 0
	print('Error removing ' + item + ' from inventory.')
	

def checkEnergy():
	global playerEnergy
	playerEnergy-=1
	if (playerEnergy<1):
		print('Exhausted, you collapse where you stand. If you can\'t defeat the heat, and your own thirst and hunger, what chance would have stood against the dragon?\nThis thought provides you little comfort as you fade out of consciousness.\n\nGAME OVER')
		global victory
		victory=1
	elif (playerEnergy==5):
		print("Your thirst is becoming unbearable. Each step is a struggle, and if you\ndon't find a way off this island soon, you may become a permanent\nfixture.")
	elif (playerEnergy==10):
		print("The heat is beginning to take it's toll on you. You notice that you have\nstopped sweating, which is bad since since you certainly haven't stopped\nworking.")
	elif (playerEnergy==20):
		print("You stumble as you take a step forward.\nYour aching body has been complaining with each step, but it is becoming\nmore difficult to ignore.")
	elif (playerEnergy==30):
		print("You are so thirsty you consider drinking the surrounding seawater.\nYou know this would only worsen your condition, and quickly abandon the\nidea. Hopefully the next island has a fresh water source. . .")

def checkLocation():
	global playerExplored
	playerExplored.append(playerLocation[:])
	if (victoryBeach==0 and playerLocation[0]==1 and previousLocation[0]!=1) or (victoryBeach==1 and playerLocation[1]==mapSize and previousLocation[1]!=mapSize) or (victoryBeach==2 and playerLocation[0]==mapSize and previousLocation[0]!=mapSize):
		print('You can barely make out the outline of what appears to be a larger island\nacross the ocean.')
	elif (playerLocation[0]==1 and playerLocation[1]==1) or (playerLocation[0]==1 and playerLocation[1]==mapSize) or (playerLocation[0]==mapSize and playerLocation[1]==1) or (playerLocation[0]==mapSize and playerLocation[1]==mapSize):
		if (playerLocation!=previousLocation):
			print('You are at the corner of this oddly square-shaped island.')
	elif (playerLocation[0]==mapSize or playerLocation[0]==1 or playerLocation[1]==1 or playerLocation[1]==mapSize):
		if (previousLocation[0]!=mapSize and previousLocation[0]!=1 and previousLocation[1]!=1 and previousLocation[1]!=mapSize):
			print("You are back on the beach.")
	elif (playerLocation[0]<mapSize and playerLocation[0]>1 and playerLocation[1]>1 and playerLocation[1]<mapSize):
		if (previousLocation[0]==mapSize or playerLocation[0]==1 or previousLocation[1]==1 or previousLocation[1]==mapSize):
			print("You walk into the dense jungle.")
	if (playerLocation[0]==Challenge1[0] and playerLocation[1]==Challenge1[1] and checkInventory('berries')==0):
		print('Lying on the ground in front of you is the partially decayed body of a man you\n\
recognize only vaguely as being from your same village. He must have been\n\
"recruited" earlier. Perhaps he left something behind that could help you,\n\
but you hesitate to search his body.')
	elif (playerLocation[0]==Challenge2[0] and playerLocation[1]==Challenge2[1] and boatFinished==0):
		print('You walk into a clearing, and to your amazement you see a tree felled\n\
to the ground, and nearly completely carved out to form a passable canoe.\n\
If you could finish this BOAT and move it to the beach you need to launch\n\
from, you would be saved. You notice a body lying nearby, with the fragments\n\
of a rock that was clearly used on the log. A quick inspection tells you that\n\
this rock is of no more use, but if you could find another before you run out\n\
of energy, you could get on to the next impossible task.')
	elif (playerLocation[0]==Challenge2[0] and playerLocation[1]==Challenge2[1] and boatFinished==1 and checkInventory('boat')==0):
		print('The boat is lying there, just waiting for someone to carry it to the\nbeach and pilot it to the next island.')
	elif (playerLocation==Challenge3 and checkInventory('rock')==0):
		print('Half buried in the sand is a sharp ROCK.\nThis may be useful as a weapon or a tool.')
	else:
		flavorText()

def flavorText():
	textNumber=random.randint(1,50)
	if (textNumber==1):
		print('It is eerily quiet. Growing up in the islands, you are accustomed to a\n\
cacophony of sound from birds, monkeys, all sorts of delicious animals. Frankly,\
you don\'t care if the lack of animals animals is because of a dragon, the\n\
previous contestants, the elders, or simply because they are all suddenly\n\
giving you the silent treatment, you just wish that something would make\n\
some noise.\n"Yaaah!", you shout at the top of your lungs, and immediately\n\
feel foolish.')
	if (textNumber==2):
		print('Wait, did I remember to put out my cooking fire before I got kidnapped?\nNot that it really matters at this point. . .')
	if (textNumber==3):
		print('"Who picks these village elders anyways?" you grumble.')
	if (textNumber==4):
		print('If you actually manage to kill the dragon, they\'d better have a\n\
particularly attractive island girl waiting for you when you get back.\n\
Surprisingly, the idea is the happiest one you\'ve had all day.')
	if (textNumber==5):
		print('You stop for a moment to itch your left ear. Ears are weird, you realize.')

def generateMap():
	global Challenge1
	global Challenge2
	global Challenge3
	#Generate Challenge 1 (body+berries)
	overlap=1
	while overlap==1:
		number = random.randint(1, mapSize)
		Challenge1[0]=number
		number = random.randint(1, mapSize)
		Challenge1[1]=number
		if (Challenge1[0]!=playerLocation[0] or Challenge1[1]!=playerLocation[1]):
			overlap=0
	#Generate Challenge 2 (boat)
	overlap=1
	while overlap==1:
		number = random.randint(2, mapSize-1)
		Challenge2[0]=number
		number = random.randint(2, mapSize-1)
		Challenge2[1]=number
		if (Challenge2[0]!=playerLocation[0] or Challenge2[1]!=playerLocation[1]):
			if (Challenge2[0]!=Challenge1[0] or Challenge2[1]!=Challenge1[1]):
				overlap=0
	#Generate Challenge 3 (rock)
	overlap=1
	while overlap==1:
		number = random.randint(1, mapSize)
		Challenge3[0]=number
		number = random.randint(1, mapSize)
		Challenge3[1]=number
		if (Challenge3[0]!=playerLocation[0] or Challenge3[1]!=playerLocation[1]):
			if (Challenge3[0]!=Challenge1[0] or Challenge3[1]!=Challenge1[1]):
				if (Challenge3[0]!=Challenge2[0] or Challenge3[1]!=Challenge2[1]):
					overlap=0
	if mapCheat==1:
		printMap()

def gameBody():
	print('You wake up on the beach, with the sun shining down on your bruised face.\n\n"Where am I?"\n\n(Press Enter to advance text.)')
	input()
	print('Slowly, memory returns. You were taken from your hut late at night by the\n\
village elders. Seems there has been a dragon upsetting the local order of\n\
things, and it is time someone took care of it. You are not the first to be\n\
"recruited" for this task, and the fact that none of your predecessors have\n\
returned does not seem like a good sign. The village elders tied you up and\n\
brought you several days from home to this deserted island. Before they knocked\n\
you unconscious and cut your bonds, they told you that your first task is to\n\
travel to a nearby island, where you will find a relic of some sort to help you\n\
in your quest. They gave you a MAP to keep track of where you have been, but no\n\
food or drink. You place the MAP in your conspicuously empty INVENTORY.\n\n')
	input()
	print('"Sure, no problem! All I have to do is figure out WHERE this island is, and then\
find a way to get there without drowning or starving to death in the process?\n\
Oh, and then kill a fiery flying god of destruction? Don\'t worry about me, I\n\
do this all the time! I\'ll be back in time for dinner."\n\
As you struggle to your feet, your growling stomach points out that you always\n\
resort to sarcastic humor when you are scared.\n\
"Shut up."\n\
No further smart remarks from your bowels.\nWell, that\'s sorted then. No point in delaying the inevitable any further.\n\
You turn north, putting the ocean to your back.\nAhead of you lies jungle, and to either side of you the beach stretches away.')
	while (victory!=1):
		recognizeAction()




#Main body of code
print('\n\t\tDragonQuest\n\tChapter I - An Unwilling Recruit')
menuOption=0
while int(menuOption)!=4: 
	print('\nMenu\n\t1 - Start Game\n\t2 - Set difficulty\n\t3 - How to play\n\t4 - Exit Game')
	menuOption=input()
	if int(menuOption)==3:
		helpText()
	elif int(menuOption)==2:
		difficulty=0
		while int(difficulty)!=1 and int(difficulty)!=2:
			print('\n\nDifficulty Levels\n\t1 - Normal (Default)\n\t2 - Hard')
			difficulty=input()
	elif int(menuOption)==1:
		mapCheat=0#Initialize cheat options
		warpCheat=0
		victory=0
		inventory=['map']
		boatFinished=0
		Challenge1=[0,0]
		Challenge2=[0,0]
		Challenge3=[0,0]
		mapSize=random.randint(5,8) #Length of the square map
		victoryBeach=random.randint(0,2)
		playerLocation=[random.randint(2,mapSize-1),1]
		previousLocation=playerLocation[:]
		playerExplored=[]
		playerExplored.append(playerLocation[:])
		if (int(difficulty)<2):
			playerEnergy=pow(mapSize,2)
		elif (int(difficulty)==2):
			playerEnergy=pow(mapSize,2)-2*mapSize
		generateMap()
		gameBody()
	





