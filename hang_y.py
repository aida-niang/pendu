import pygame
import os

pygame.init()
WIDTH, HEIGHT = 800, 500
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Le Super Jeu du Pendu!")

FPS = 60 #setting the maximum speed of the game at 60 frames per second
clock = pygame.time.Clock() #clock object
run = True #control the while loop below. will be set to false when the game is over

while run:
    clock.tick(FPS)#clock object that's counting at 60 FPS

    #for loop to make it possible to create events such as clicking with a mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #ability to close the game by clicking on the red cross X
            run = False #quit pygame

pygame.quit()