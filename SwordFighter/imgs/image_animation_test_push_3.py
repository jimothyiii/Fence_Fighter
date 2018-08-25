import pygame
import time
import random
from PIL import Image
import operator, itertools
pygame.init()

res_width = 800
res_height = 600

gameDisplay = pygame.display.set_mode((res_width,res_height))
pygame.display.set_caption('SwordFighter')
clock = pygame.time.Clock()






fencer_1_normalImg = pygame.image.load('fencer_1_normal.png')

fencer_1_attackImg = pygame.image.load('fencer_1_attack.png')
fencer_1_attack_transImg = pygame.image.load('fencer_1_attack_trans.png')

fencer_1_backImg = pygame.image.load('fencer_1_back.png')
fencer_1_forwardImg = pygame.image.load('fencer_1_forward.png')

fencer_1_parryImg = pygame.image.load('fencer_1_parry.png')
fencer_1_parry_transImg = pygame.image.load('fencer_1_parry_trans.png')

loop = True

for event in pygame.event.get():
            
           
# forward and back

    while loop:
        gameDisplay.blit(fencer_1_normalImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_backImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_normalImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_forwardImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_normalImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_backImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_normalImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_forwardImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
     
##attack           

             
        gameDisplay.blit(fencer_1_normalImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_attack_transImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_attackImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_normalImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_normalImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_attack_transImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_attackImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_normalImg,(0,0))
        pygame.display.update()
        time.sleep(.5)

##parry
                      

        gameDisplay.blit(fencer_1_normalImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_parry_transImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_parryImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_parry_transImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_normalImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_parry_transImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_parryImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
        gameDisplay.blit(fencer_1_parry_transImg,(0,0))
        pygame.display.update()
        time.sleep(.5)
 
