import pygame
import time
import random
from PIL import Image
import operator, itertools
pygame.init()

res_width = 800
res_height = 600
fencer1_width = 246

#colordefine(R,G,B)
black = (0,0,0)
white = (255,255,255)
red = (200, 0, 0)
bright_red = (255,0,0)
grey = (100,100,100)
dark_grey = (50,50,50)
yellow = (255,255,0)
p1points = 0
p2points = 0
pause= False
AI_level = random.randrange(1,3)
gameDisplay = pygame.display.set_mode((res_width,res_height))
pygame.display.set_caption('SwordFighter')
clock = pygame.time.Clock()




fencer_1Img = pygame.image.load('fencer_1.png')

fencer_1_attackImg = pygame.image.load('fencer_1_attack.png')
fencer_2Img = pygame.image.load('fencer_2.png')
fencer_2_attackImg = pygame.image.load('fencer_2_attack.png')
fencer_1_parryImg = pygame.image.load('fencer_1_parry.png')
fencer_2_parryImg = pygame.image.load('fencer_2_parry.png')
intro_background = pygame.image.load('intro_background.png')
background = pygame.image.load('background_arena.png')
how_to_playImg = pygame.image.load('how_to_play.png')
#postiopning the background; in the future grab image dimentions
BGx = -1 * (1018 - res_width) / 2  #bg width hard coded
BGy = -1 * (1024 - res_height - 20) / 2 #bg height hard coded



def fencer_1(x,y):
    gameDisplay.blit(fencer_1Img,(x,y))
    
def fencer_2(x,y):
    gameDisplay.blit(fencer_2Img,(x,y))

def fencer_1_attack(x,y):
    gameDisplay.blit(fencer_1_attackImg,(x+3,y+27))  #hard coded image adjustment
    
def fencer_2_attack(x,y):
    gameDisplay.blit(fencer_2_attackImg,(x-36,y+27)) #hard coded image adjustment

def fencer_1_parry(x,y):
    gameDisplay.blit(fencer_1_parryImg,(x,y))
                     
def fencer_2_parry(x,y):
    gameDisplay.blit(fencer_2_parryImg,(x+74,y)) #hardcoded image width differance
                     
def text_objects(text, font):
    textSurface = font.render(text, True, dark_grey)
    return textSurface, textSurface.get_rect() 

def message_display(text,ymod):
    font = pygame.font.Font('freesansbold.ttf',75)
    textSurf = font.render(text, True, red)
    TextRect = textSurf.get_rect()
    TextRect.center = ((res_width /2),(res_height/2)+ymod)
    gameDisplay.blit(textSurf, TextRect)
    pygame.display.update()

    time.sleep(1)

    

def fast_message_display(text,xmod,ymod):
    font = pygame.font.Font('freesansbold.ttf',20)
    textSurf = font.render(text, True, yellow)
    TextRect = textSurf.get_rect()
    TextRect.center = ((res_width/2 + xmod),(res_height/2 + ymod))
    gameDisplay.blit(textSurf, TextRect)
    pygame.display.update()
    
def P1kill():
    
    message_display('Touche!',0)
    message_display('P1 Point!',70)
def P2kill():
    
    message_display('Touche!',0)
    message_display('P2 Point!',70)
    
def draw():
    message_display('Touche!',0)                
    message_display('Draw!',70)
    
    
def show_points(points,x,y):
    font = pygame.font.SysFont(None,25)
    text = font.render("Points: " +str(points),True, yellow)
    
    gameDisplay.blit(text,(x,y))
    
def show_ai_level(x,y):
    global AI_level
    font = pygame.font.SysFont(None,25)
    text = font.render("Level: " +str(AI_level),True, yellow)
    
    gameDisplay.blit(text,(x,y))
    
    
def button(msg,x,y,w,h,ic,ac,action=None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()    
    print(action,click[0])
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action !=None:
            if action == "play2":
                game_loop_2_players()
            elif action == "play1":
                game_loop_1_player()
            elif action == "quit":
                game_intro()
            elif action == "unpause":
                unpause()
            elif action == "back":
                game_intro()
            elif action == "how":
                how_to_play()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

            
    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf,textRect = text_objects(msg, smallText)
    textRect.center = (x+w/2, y+h/2)
    gameDisplay.blit(textSurf, textRect)

def out_of_bounds():
    message_display('Out Of Bounds',0)

def victory(msg,player):
    message_display(msg,-100)
    message_display(player,-20)
    
#******************intro************************************
def game_intro():
    pygame.time.wait(500)#this fixes the button bug with clicking to long
    intro= True

    while intro:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(intro_background, ((res_width-1552)/2,(res_height-873)/2))
        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("Fence Fighter", largeText)
        TextRect.center = ((res_width/2),(res_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        
        button("1 Player",res_width*1/11,res_height*2/3,200,100,red,bright_red,"play1")
        button("2 Player",res_width*4/11,res_height*2/3,200,100,red,bright_red,"play2")       
        button("How to Play",res_width*7/11,res_height*2/3,200,100,red,bright_red,"how") 
        pygame.display.update()
        clock.tick(15)
##********************How to play*******************************
def how_to_play():
    pygame.time.wait(500)
    instructions= True

    while instructions:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(how_to_playImg, ((res_width-800)/2,(res_height-600)/2)) #hard coded image dimentions
              
        button("Back",res_width/2,res_height*2/3,200,100,red,bright_red,"back")
                
        pygame.display.update()
        clock.tick(15)
        
##******************* paused *************************************************
def unpause():
    
    global pause
    pause = False


def paused():

    
    pygame.time.wait(500)

    while pause:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.blit(intro_background, ((res_width-1552)/2,(res_height-873)/2))
        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((res_width/2),(res_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        
        
        button("Quit (Arret)",res_width/2,res_height*2/3,200,100,red,bright_red,"quit")
        
        button("Continue (Allez)",res_width/5,res_height*2/3,200,100,red,bright_red,"unpause")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                unpause()
        
        pygame.display.update()
        clock.tick(15)

def gameover():
    pygame.time.wait(500)

    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            gameDisplay.blit(intro_background, ((res_width-1552)/2,(res_height-873)/2))
            largeText = pygame.font.Font("freesansbold.ttf",115)
            TextSurf, TextRect = text_objects("Game Over", largeText)
            TextRect.center = ((res_width/2),(res_height/2))
            gameDisplay.blit(TextSurf, TextRect)

                
                
            button("Quit",res_width/2,res_height*2/3,200,100,red,bright_red,"quit")
            button("Play Again?",res_width/5,res_height*2/3,200,100,red,bright_red,"play1")
                
            pygame.display.update()
            clock.tick(15)



        
#**************** GAME LOOP ****** 2 player mode *****************************
def game_loop_2_players():
    global pause
    pause = False

    #Game balance
    points_to_win = 11
    frame_rate = 60 #max framerate
    gamespeed = 3
    move_speed = 7
    attack_cd = 25
    attack_length = 40
    attack_time = attack_length + attack_cd
    parry_cd = 10
    parry_length = 45
    parry_time = parry_length + parry_cd
    message_stay_time = 0

    #starting postions
    x1 = (res_width * .1)
    x2 = (res_width * .6) 
    y = (res_height * .3)

    p1points =0
    p2points =0
       
    x1_change = 0
    x2_change = 0
    attacking1= 0 
    attacking2= 0
    parrying1= 0
    parrying2= 0
    slowing1=False
    slowing2=False
    
    message_stay_time = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
##player inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -1* move_speed
                if event.key == pygame.K_d:
                    x1_change = move_speed
                if event.key == pygame.K_LEFT:
                    x2_change = -1* move_speed
                if event.key == pygame.K_RIGHT:
                    x2_change = move_speed
                if event.key == pygame.K_j and attacking1 < 0 and parrying1 < 0:
                    attacking1 = attack_time                  
                if event.key == pygame.K_KP1 and attacking2 < 0 and parrying2 < 0:
                    attacking2 = attack_time              
                if event.key == pygame.K_k and attacking1 < 0 and parrying1 < 0:
                    parrying1 = parry_time               
                if event.key == pygame.K_KP2 and attacking2 < 0 and parrying2 < 0:
                    parrying2 = parry_time                    
                if event.key == pygame.K_BACKSPACE:
                    p1points =0
                    p2points =0
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or pygame.K_d:
                    slowing1 = True
                
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    slowing2 = True
                


## a momentum effect to movement
        if slowing1 or slowing2 == True:           
            if x1_change >0:
                x1_change -= 1
            if x1_change <0:
                x1_change += 1
                
            if x2_change >0:
                x2_change -= 1     
            if x2_change <0:
                x2_change += 1
            if x1_change == 0:
                slowing1 = False
            if x2_change ==0:
                slowing2 = False    
            
        x1 += x1_change
        x2 += x2_change
        
        attacking1 -= gamespeed
        attacking2 -= gamespeed
        parrying1 -= gamespeed
        parrying2 -= gamespeed
        message_stay_time -= 1
                     
        
        gameDisplay.fill(black)
        gameDisplay.blit(background,(BGx,BGy))
        show_points(p1points,(res_width-50)/3, res_height/4)    #hard coded
        show_points(p2points,(res_width-150)*2/3, res_height/4) #hard coded

        if attacking1 > attack_cd: #attack image time
            fencer_1_attack(x1,y)
            if x1 > x2 - fencer1_width/2 - 5 and attacking1 < attack_cd + 5 and parrying2 < parry_cd:  #5 is kill frames this give reaction time for parry til end of attack 
                p1points += 1
                P1kill()
                x1 = (res_width * .1)
                x2 = (res_width * .6)
                 
        elif parrying1 > parry_cd:
            fencer_1_parry(x1,y)          
        else:
            fencer_1(x1,y)

        if attacking2 > attack_cd: #attack image time
            fencer_2_attack(x2,y)
            if x1 > x2 - fencer1_width/2 - 5 and attacking2 < attack_cd + 5 and parrying1 < parry_cd:  #hardcoded
                p2points += 1
                P2kill()
                x1 = (res_width * .1)
                x2 = (res_width * .6)
        elif parrying2 > parry_cd:
            fencer_2_parry(x2,y)
        else:
            fencer_2(x2,y)
        if (5 + attack_cd > attacking1 > attack_cd and  parrying2> parry_cd) or (5 + attack_cd > attacking2 > attack_cd and parrying1 > parry_cd and x1 > x2 - fencer1_width/2):
            message_stay_time = 10
        if message_stay_time > 0:
            fast_message_display("Parry",-20,+20)
        if x1 < 0 or x2 + fencer1_width > res_width:
            out_of_bounds()
            x1 = (res_width * .1)
            x2 = (res_width * .6)
        if x1 > x2 - fencer1_width/2 - 30  and attacking1 > attack_cd and attacking2 > attack_cd:
            draw()
            x1 = (res_width * .1)
            x2 = (res_width * .6)

        if p1points > points_to_win-1 and p1points > p2points + 1:
            victory("Victory","Player 1")
        if p2points > points_to_win-1 and p2points > p1points + 1:
            victory("Victory","Player 2")   
        pygame.display.update()
        clock.tick(frame_rate)


        
#****************************** 1 player mode game mode *****************************
##def enemy(lvl,)
##    random.randrange(lvl-5,lvl)
##    
##
##    return action


        
def game_loop_1_player():
    global pause
    pause = False
    
#Game balance
    frame_rate = 60  #max frame rate
    points_to_win = 3                 #points to win is at 3 <<<<<<<<<<<<<<<<<<<
    gamespeed = 1
    move_speed = 7
    attack_cd = 25
    attack_length = 40
    attack_time = attack_length + attack_cd
    parry_cd = 5
    parry_length = 45
    parry_time = parry_length + parry_cd
    message_stay_time = 0
    
#AI lvl
    global AI_level
    
    AI_movement_lvl = random.randrange(AI_level-4,AI_level+1)
    AI_attack_lvl = random.randrange(AI_level-4,AI_level+1)
    AI_parry_lvl = random.randrange(AI_level-4,AI_level+1)
#starting postions
    x1 = (res_width * .1)
    x2 = (res_width * .6) 
    y = (res_height * .3)

    p1points =0
    p2points =0
       
    x1_change = 0
    x2_change = 0
    attacking1= 0 
    attacking2= 0
    parrying1= 0
    parrying2= 0
    ai_move_change=0
    message_stay_time = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



                
#**************************************************************** player Inputs

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -1* move_speed
                if event.key == pygame.K_d:
                    x1_change = move_speed 
                if event.key == pygame.K_j and attacking1 < 0 and parrying1 < 0:
                    attacking1 = attack_time                                
                if event.key == pygame.K_k and attacking1 < 0 and parrying1 < 0:
                    parrying1 = parry_time               
                if event.key == pygame.K_BACKSPACE:
                    p1points =0
                    p2points =0
                if event.key == pygame.K_p:
                    pause = True
                    paused()    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or pygame.K_d:
                    x1_change = 0
               
                    

#**************************************************************** computer player AI
#AI level set
        
        print(AI_level,AI_movement_lvl,AI_attack_lvl,AI_parry_lvl) #= random.randrange(1,10) #make increaseing for tourney game mode   #set above game loop
        AI_movement_lvl = random.randrange(AI_level-4,AI_level+1)
        AI_attack_lvl = random.randrange(AI_level-4,AI_level+1)
        AI_parry_lvl = random.randrange(AI_level-4,AI_level+1)
        random_attack = random.randrange(1,100)
        random_parry = random.randrange(1,100)
        ai_move = None
        ai_attack = None
        ai_parry = None
        
#movement 
        ai_move_cd = 20
        ai_move_change -= ai_move_cd
        if ai_move_change < 0:
            random_move = random.randrange(1,100)
#1-3
        if AI_movement_lvl < 4:
            if x1 < x2 - fencer1_width/2 - 200 or x2 + fencer1_width > res_width - 5:
                ai_move ='left'
            if x1 > x2 - fencer1_width/2 + 50:
                ai_move ='right'

#4-6            
        if AI_movement_lvl > 3:
            if random_move > 90 or x2 + fencer1_width > res_width - 5:
                ai_move = 'left'
            elif random_move > 15:
                ai_move = None
            else:
                ai_move = 'right'
      

#7-10        
        if AI_movement_lvl > 6:
            if random_move > 95 or x2 + fencer1_width > res_width - 5 or x1 < x2 - fencer1_width/2 - 140:
                ai_move = 'left'
            elif random_move > 80 or x1 > x2 - fencer1_width/2:
                ai_move = 'right'
            else:
                ai_move = None
                
        if ai_move == 'left':
            x2_change = -1* move_speed
        if ai_move == 'right':
            x2_change = move_speed
        if ai_move == 'None':
            x2_change = 0    
##attack 
#1-3
        if AI_attack_lvl <4:    
            if random_attack > 80:
                ai_attack = True    
            else:
                ai_attack = False
                
#4-10
        if AI_attack_lvl >3:
            if x1 > x2 - fencer1_width/2 - 5 and random_attack <= AI_attack_lvl *10:
              ai_attack = True
            else:
                ai_attack = False
       
        if (ai_attack == True) and attacking2 < 0 and parrying2 < 0:
                attacking2 = attack_time

#parry
#1-3                
        if AI_parry_lvl < 4:
            if random_parry > 90:
                ai_parry = True
            else:
                ai_parry = False
#4-10
        if AI_parry_lvl >3:
            if attacking1 > 0 and random_parry <= AI_parry_lvl *10 :
                ai_parry = True
            else:
                ai_parry = False
                

        if (ai_parry == True) and attacking2 < 0 and parrying2 < 0:
                  parrying2 = parry_time        

#*******************************************************************************
        
        x1 += x1_change
        x2 += x2_change
        
        attacking1 -= gamespeed
        attacking2 -= gamespeed
        parrying1 -= gamespeed
        parrying2 -= gamespeed
        message_stay_time -= 1             
        
        
#back ground and points        
        gameDisplay.fill(black)
        gameDisplay.blit(background,(BGx,BGy))
        show_points(p1points,(res_width-50)/3, res_height/4)    #hard coded
        show_points(p2points,(res_width-150)*2/3, res_height/4) #hard coded
        show_ai_level(10,10)
#Repost message
        if (5 + attack_cd > attacking1 > attack_cd and  parrying2 > parry_cd) or (5 + attack_cd > attacking2 > attack_cd and parrying1 > parry_cd and x1 > x2 - fencer1_width/2):
            message_stay_time = 10
        if message_stay_time > 0:
            fast_message_display("Parry",10,-65)

        
#fencer 1 displayed
        if attacking1 > attack_cd: #attack image time
            fencer_1_attack(x1,y)
            if x1 > x2 - fencer1_width/2 - 5 and attacking1 < attack_cd + 5 and parrying2 < parry_cd:  #5 is kill frames this give reaction time for repost til end of attack 
                p1points += 1
                P1kill()
                attacking1 = 0
                attacking2 = 0
                parrying1 = 0
                parrying2 = 0
                x1 = (res_width * .1)
                x2 = (res_width * .6)
                 
        elif parrying1 > parry_cd:
            fencer_1_parry(x1,y)          
        else:
            fencer_1(x1,y)
            
#fencer 2 displayed
        if attacking2 > attack_cd: #attack image time
            fencer_2_attack(x2,y)
            if x1 > x2 - fencer1_width/2 - 5 and attacking2 < attack_cd + 5 and parrying1 < parry_cd:  #hardcoded
                p2points += 1
                P2kill()
                attacking1 = 0
                attacking2 = 0
                parrying1 = 0
                parrying2 = 0
                x1 = (res_width * .1)
                x2 = (res_width * .6)
        elif parrying2 > parry_cd:
            fencer_2_parry(x2,y)
        else:
            fencer_2(x2,y)
            
#out of bounds
        if x1 < 0 or x2 + fencer1_width > res_width:
            out_of_bounds()
            x1 = (res_width * .1)
            x2 = (res_width * .6)
            attacking1 = 0
            attacking2 = 0
            parrying1 = 0
            parrying2 = 0
            
#Draw
        if x1 > x2 - fencer1_width/2 - 30  and attacking1 > attack_cd and attacking2 > attack_cd:
           
            if attacking1 > attacking2 + 1:
                P2kill()
                p2points += 1
            elif attacking2 > attacking1 + 1:
                P1kill()
                p1points += 1
            else:     
                draw()
            x1 = (res_width * .1)
            x2 = (res_width * .6)
            
            attacking1 = 0
            attacking2 = 0
            parrying1 = 0
            parrying2 = 0    
        pygame.display.update()
        clock.tick(frame_rate)
#victory
        if p1points > points_to_win-1 and p1points > p2points + 1:
            victory("La Victoire",None)
            p1points = 0
            p2points = 0
            attacking1 = 0
            attacking2 = 0
            parrying1 = 0
            parrying2 = 0
            if AI_level < 10:
                AI_level += 1
        if p2points > points_to_win-1 and p2points > p1points + 1:
            victory("Défaite",None)
            gameover()



#********************************************

game_intro()
game_loop_2_players()    
pygame.quit()
quit()
