import pygame
import os

pygame.init() #initializes the display module
WIDTH, HEIGHT = 800, 500 #setting the size of the game window
pygame.display.set_mode((WIDTH, HEIGHT)) #initializes a windows with WIDTH and HEIGHT parameters
pygame.display.set_caption("Le Super Jeu du Pendu!") #game's title 

FPS = 60 #setting the maximum speed of the game at 60 frames per second
clock = pygame.time.Clock() #clock object
run = True #control the while loop below. will be set to false when the game is over

while run:
    clock.tick(FPS)#clock object that's counting at 60 FPS

    #for loop to make it possible to create events such as clicking with a mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #ability to close the game by clicking on the red cross X
            run = False #quit pygame
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() #how you get the position of the mouse. gives the position of the mouse, especially useful when clicking
            print(pos)

pygame.quit()