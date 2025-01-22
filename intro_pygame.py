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
width = 600
height = 600
screen = pygame.display.set_mode((width,height))
title = pygame.display.set_caption('Hangman Game')

#I want to print objects on my screen :
#######Method1 : show images
# step1 = pygame.image.load('pendu_image\image1.png')
# step2 = pygame.image.load('pendu_image\image2.png')
# step3 = pygame.image.load('pendu_image\image3.png')
# step4 = pygame.image.load('pendu_image\image4.png')
# step5 = pygame.image.load('pendu_image\image5.png')
# step6 = pygame.image.load('pendu_image\image6.png')
# step7 = pygame.image.load('pendu_image\image7.png')

#I want to use a loop to import all the images using one variable:
#Initialize an empty list
images = []
for i in range(1, 8):
    image = pygame.image.load(f'pendu_image\image{i}.png')  
    images.append(image)


######Method2 : Create the objects :
#object_1 = pygame.draw.line(()) #to perform later ....

#The main loop of the game :
image_index = 0  
running = True
while running :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() #this function allows to print the positions of the objects, just by clicking on the screen
            print(pos) #print the positions in the terminal

        if event.type == pygame.KEYDOWN: # When we press a key , that changes the hangman image 
            if event.key == pygame.K_RETURN :
                image_index += 1 #when all the images are shown, we exit

                

    screen.fill(white) #choose the color of the screen

    screen.blit(images[image_index], (150, 150)) #show the images and use a keyboard to change the image

    pygame.display.flip()

pygame.quit()
