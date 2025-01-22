#In this version, I will try to draw the hangman using pygame library
import keyboard  #That will allow the user to use the keyboards
import pygame
from pygame.locals import *

#initialize pygame in order to be able to use its functionnalities
pygame.init()

#Define somes tuples (colors) :
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#Create the screen
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
title = pygame.display.set_caption('Hangman Game')


#Create the objects :
object_1 = pygame.rect((10, 10))

#The main loop of the game :
running = True
while running :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() #how you get the position of the mouse. gives the position of the mouse, especially useful when clicking
            print(pos)

    screen.fill((green))
    screen.blit(object_1, (0, 0)) #this 
    pygame.display.flip()

pygame.quit()