'''

***CS101 MINI PROJECT***
TOPIC: BRICK- BREAKER GAME
TEAM MEMBERS : SOMESH AGRAWAL, SUYASH MADALE , ARAV JADAV

'''


'''Coded by SUYASH MADALE'''
import pygame
import structure1
pygame.init()

sw = 800  # width of our screen
sh = 800	#height of our screen

bg = pygame.image.load('bgm.png')  # helps us to define our background image
win = pygame.display.set_mode((sw, sh)) # defininf the window of our pygame
pygame.display.set_caption("BRICK BREAKER") # setting the caption of our window


player = structure1.Player(sw/2 - 50, sh -100, 140, 20, (0,255,0)) # CREATING OUR Player(x-cor,y-cor,width,height,color_code)
ball = structure1.Ball(sw - 80, sh - 400, 20, 20, (255,0,0)) # CREATING OUR Ball(x-cor,y-cor,width,height,color_code)
 # will be used if we want top create multiple balls
score=0


clock = pygame.time.Clock() #setting the clock for the pygame


font = pygame.font.SysFont('comicsans', 50)# Specifying the font we are using in our game

# Helps to define the position of our brick in the starting of the  game
bricks = []
''' Defining the init function which will contain bricks stucture
of the game which will be shown on the screen.'''
def init():
    global bricks
    bricks = []  #list of all the bricks going to be used
    for i in range(6):
        for j in range(10):
            brick=structure1.Brick(10 + j * 79, 50 + i * 35, 70, 25,6-i,100*(6-i))#Brick(x-cordinate,y-cordinate,width,height,strngth,score associated with particular brick)
            brick.color_assign()#assign color of brick on the basis of strength
            bricks.append(brick)  # specifing the particular position of the brick


'''Coded by SOMESH AGRAWAL'''
def collision(ball): # checking the collision between the ball and the player
	if (ball.x >= player.x and ball.x <= player.x + player.w) or (ball.x + ball.w >= player.x and ball.x + ball.w <= player.x + player.w):
	    if ball.y + ball.h >= player.y and ball.y + ball.h <= player.y + player.h:
	        ball.yv *= -1
	        ball.y = player.y -ball.h -1
def collisionBB(ball): #Checking the collision between the ball and brick
	global score
	for brick in bricks:
	    for ball in balls:
	        if (ball.x >= brick.x and ball.x <= brick.x + brick.w) or ball.x + ball.w >= brick.x and ball.x + ball.w <= brick.x + brick.w:
	            if (ball.y >= brick.y and ball.y <= brick.y + brick.h) or ball.y + ball.h >= brick.y and ball.y + ball.h <= brick.y + brick.h:
		            	
		            ball.yv*=-1
		            if brick.strength==1:#deleting the brick if it's strength is at minimum
		            	brick.visible = False
		            else :
		            	brick.strength-=1 #reducing the strngth of brick evrytime it get hit
		            	brick.color_assign()#changing the color
	for brick in bricks: #destroy the brick if the ball had touch it
		if brick.visible == False:			
			score+=brick.score	#Incrementing the score  as soon as any brick is destroyed
			bricks.pop(bricks.index(brick))# deleting the brick
			           


def text_objects(text, font): #helps to create a text object and return a text surface and rectangle in return
    textSurface = font.render(text, True, (0,255,0))
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action):# creating a dynamic button which will change the color on hover and new function will start on clicking in that box
	global option
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x+w > mouse[0] > x and y+h > mouse[1] > y: #checking the hovering of mouse as well as clicking of the mouse button
	    pygame.draw.rect(win, ac,(x,y,w,h))

	    if click[0] == 1 :
	    	option=action
                  
	else:
	    pygame.draw.rect(win, ic,(x,y,w,h))

	smallText = pygame.font.SysFont("comicsansms",15)	#writing a small text inside the button
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	win.blit(textSurf, textRect)
    
name='name'
#Taking input from user to enter his name
def input_name():
	global name
	while 1:# helps to take the name from the user
		win.fill((255, 255, 255))

		text='Enter Your Name and press Enter'#taking the name of the user as an input
		font = pygame.font.SysFont(None, 48)
		img = font.render(text,True, (255,0,0))
		rect = img.get_rect()
		rect.topleft = (200, 40)
		win.blit(img, rect)
		for event in pygame.event.get():#check whether user has written the name and press enter
			if event.type == pygame.KEYDOWN:	
				if event.key == pygame.K_BACKSPACE:
					if len(name)>0: 
						name = name[:-1]
				elif event.key != pygame.K_RETURN:
					name+=event.unicode

				if event.key == pygame.K_RETURN:
					return
				
		#render name of the user on the screen
		img = font.render(name,True, (255,0,0))
		rect = img.get_rect()
		rect.topleft = (20, 80)
		win.blit(img, rect)
		pygame.display.update()

# Creating the main menu of the game , displaying various features such as play, exit, logs, and instrcuctions
def main_menu():
	win.blit(bg, (0,0))
	largeText = pygame.font.SysFont("freesansbold",95)
	TextSurf, TextRect = text_objects("Brick Breaker!!", largeText)
	TextRect.center = ((sw/2),(sh/2))
	win.blit(TextSurf, TextRect)	#define and print a text box for printing brick breaker game on the screen

#specifying four buttons that is GO, Instructions, performance , Quit for our game
	button("GO!",100,450,100,50,(0,150,0),(0,255,0),2)
	button("Instructions",250,450,100,50,(150,150,0),(255,255,0),3)
	button("Performance",400,450,100,50,(0,150,150),(0,255,255),4)
	
	button("Quit",550,450,100,50,(150,0,0),(255,0,0),5)

	pygame.display.update()	#updating the screen so that the changes accomdated can be seen on the screen
	clock.tick(15)
font_score=pygame.font.Font('freesansbold.ttf',50)




'''coded by ARAV JADAV'''

count=0
gamewon=0
''' This contain all the main game requirements
ie input name, ball structure.
here we move our paddle with the help of mouse.'''
def main_game(): #Main game which user will play
	global sw,sh,count,option,balls,score,stores

	while not count:
		input_name()
		init() # Create a brick array before the games gets started
		ball = structure1.Ball(sw - 80, sh - 400, 20, 20, (255,0,0))
		balls = [ball]
		count+=1
		score=0
		stores=0
		
	for ball in balls:
            
            ball.move(sw,sh) # movement of the balls
            if ball.y> sh:
            	option=7
            	balls.pop(0)
	player.move(sw,sh) 			#Movement of player in the using the mouse coordinates
	collision(ball) 			# check whether any collision has occur between ball and the player
	collisionBB(ball)			# check whether any collision has occur between ball and the brick
	if len(bricks)==0:
		option=7
		gamewon=1
		return
	redraw_Window() # Update and redraw the window everytime



#Coded by - SOMESH AGRAWAL

def pause_menu():	#it will only come when user presses P
	win.blit(bg, (0,0))
	largeText = pygame.font.SysFont("comicsansms",115)		#defining  a big text on the screen
	TextSurf, TextRect = text_objects("Game Paused", largeText)
	TextRect.center = ((sw/2),(sh/2))
	win.blit(TextSurf, TextRect)
	# buttons to navigate on different screen
	button("Continue",100,450,100,50,(0,150,0),(0,255,0),2)
	button("Quit",550,450,100,50,(150,0,0),(255,0,0),5)
	pygame.display.update()
	clock.tick(15)
per=0

'''
performance tab will show the old records of the players
A player starts playing by entering his name at the begining and 
when he finishes his game , his name and his score will be shown in the performance tab.
'''
def performance():
	global  text,per
	win.blit(bg, (0,0))
	largeText = pygame.font.SysFont("comicsansms",115)
	TextSurf, TextRect = text_objects("PERFORMANCE", largeText)
	TextRect.center = ((sw/2),(0.1*sh))
	win.blit(TextSurf, TextRect)
	
	pygame.draw.rect(win, (200,150,164), [0.1*sw, 0.20*sh, 0.8*sw, 0.60*sh])
	#specifying buttons to navigate between the screen
	try:
		if per==0:
			file=open("performance.txt",'r')
			mytext=file.read()
			mytext=mytext.splitlines()
			text=mytext
			file.close()
			per+=1
		for i in range(len(text)):
			smallText=pygame.font.SysFont("comicsansms",25)
			TextSurf, TextRect = text_objects(text[i],smallText)
			TextRect.topleft = ((sw*((i+14)//14)*(0.15)),((0.2+ (i%14+1)*0.028)*sh))
			win.blit(TextSurf, TextRect)
	except:
		print("File is not found")
	button("Back To Main",550,0.85*sh,100,50,(150,0,150),(255,0,255),1)
	pygame.display.update()
	clock.tick(15)

intext=0
'''
Intructions tab will give instructions to user on how to play the game.
for example:
Instructions regarding the buttons,
how game is basically designed, score alloted for each bricks etc.
'''
#coded by- SUYASH MADALE
def instructions():
	global intext, text #intext~input text(file is read only once.), text should be displayed only once on the screen
	win.blit(bg, (0,0))
	largeText = pygame.font.SysFont("comicsansms",90)#specifying the text object which has to be displayed on the screen
	TextSurf, TextRect = text_objects("INSTRUCTIONS", largeText)
	TextRect.center = ((sw/2),(0.1*sh))#defining th e text coordinates on the screen
	win.blit(TextSurf, TextRect)
	
	pygame.draw.rect(win, (200,150,164), [0.1*sw, 0.20*sh, 0.8*sw, 0.60*sh])
	
	if intext==0:#extracting the information present inside the file
		file=open("instructions.txt",'r')
		mytext=file.read()
		mytext=mytext.splitlines()
		text=mytext
		file.close()
		intext+=1
	for i in range(len(text)):#writing the text in form of paragraph on the page
		smallText=pygame.font.SysFont("comicsansms",25)
		TextSurf, TextRect = text_objects(text[i],smallText)
		TextRect.center = ((sw*(0.5)),((0.2+ (i+1)*0.035)*sh))
		win.blit(TextSurf, TextRect)
	#specifying buttons to navigate between the screen
	button("Back To Main",550,0.85*sh,100,50,(150,0,150),(255,0,255),1)
	pygame.display.update()
	clock.tick(15)

font_finalSc=pygame.font.Font('freesansbold.ttf',35)	#specfying the font type for score's font
stores=0

'''
When the player ends his game, Game over will be shown with is final score.
and his name and the score will be stored in performance.txt file and 
we can see it by clicking on the performance tab.
'''

#coded by - SOMESH AGRAWAL
def gameover():
	global font_finalSc,stores,per,gamewon	#stores is called so that text is not written multiple times in the file, while per is used to read the file performance .txt again,font_finalSc=font for final score
	win.blit(bg, (0,0))				# printing the image on the screen
	largeText = pygame.font.SysFont("comicsansms",115)	#defining and a text object and writing text on it
	if gamewon!=0:
		TextSurf, TextRect = text_objects("Game Won", largeText)
	else:
		TextSurf, TextRect = text_objects("Game over!!", largeText)
	TextRect.center = ((sw/2),(sh/5))
	win.blit(TextSurf, TextRect)
	#specifying buttons to navigate between the screen
	button("Main Menu",100,450,100,50,(0,150,0),(0,255,0),1)#creating a main menu button to reach the main menu as well as to quit the program
	button("Quit",550,450,100,50,(150,0,0),(255,0,0),5)
	scores=font_finalSc.render(name+"'s " +"Final: "+str(score),True,(255,255,0))#print the user name and it's score on the screen
	try:
		if stores==0:	#also storing the scores inside the fle for the future reference
			person={}
			person[name]=score
			file=open("performance.txt",'a')
			for x,y in person.items(): 
				store=x+' : '+str(y)+'\n'
				file.write(store)
			file.close()
			stores+=1
			per=0#specifying so that file should be read again while calling for performance folder
	except:
		print("File is not found")
	win.blit(scores,(100,300))
	pygame.display.update()
	clock.tick(15)

'''we are presenting our screen again
by using this function'''
def redraw_Window(): # at the end of the loop , new window is created for display shapes and images in pygame.
	global score,font_score
	win.blit(bg, (0,0)) # creates a background on the screen first
	player.draw(win) # Creata a Player(player) on ther screen
	for ball in balls: # display all the balls present in our screen
	    ball.draw(win)
	for b in bricks: # display all the bricks present on our screen
		b.draw(win)
	scores=font_score.render("SCORE:- "+str(score),True,(255,255,255))
	win.blit(scores,(20,20))
	pygame.display.update() # everytime window should be updated



'''using option value to change the screen between 
main menu, main game, instructions, pause menu, gameover'''
running=True
option=1 # defining the option to decide which screen to display
while running:
	if option==1:
		main_menu()
		count=0
	elif option==2:
		main_game()
	elif option==3:
		instructions()
	elif option==4:
		performance()
	elif option==5:
		running=False
	elif option==6:
		pause_menu()
	elif option==7:
		gameover()
	
	for event in pygame.event.get(): # necessary condition to check whether user has choosen the exit option or not
		if event.type == pygame.QUIT:	#Press P to pause the game and M to go to the main menu and e to exit the game
		    running = False
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_p and option==2:# this will work only if user is present at main_game
				option=6
			if event.key==pygame.K_e and option==2:
				option=5
			if event.key==pygame.K_m and (option==2 or option==7):# this will work only if user is present at main_game or the game is over for the user
				option=1
			
pygame.quit()
