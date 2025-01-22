import pygame
import os

#settings for display
pygame.init() #initializes the display module
WIDTH, HEIGHT = 800, 500 #setting the size of the game window
win = pygame.display.set_mode((WIDTH, HEIGHT)) #initializes a windows with WIDTH and HEIGHT parameters
pygame.display.set_caption("Le Super Jeu du Pendu!") #game's title 
WHITE = (255,255,255)


#load images
pendu_etapes = [
    pygame.image.load("images/image0.png"),
    pygame.image.load("images/image1.png"),
    pygame.image.load("images/image2.png"),
    pygame.image.load("images/image3.png"),
    pygame.image.load("images/image4.png"),
    pygame.image.load("images/image5.png"),
    pygame.image.load("images/image6.png"),
]
#loop to show images. I see the surfaces in terminal so i think it's working (via print(pendu_etapes))
for i in range(7):
    pendu_images=pygame.image.load("images/image"+str(i)+".png")
    pendu_etapes.append(pendu_images)

# print(pendu_etapes)
# print(pendu_images) penser à les retirer avant présentation

#game status
status = 0


#setup game loop
FPS = 60 #setting the maximum speed of the game at 60 frames per second
clock = pygame.time.Clock() #clock object
run = True #control the while loop below. will be set to false when the game is over

while run:
    clock.tick(FPS)#clock object that's counting at 60 FPS

    win.fill(WHITE) #doesn't work, every second the screen should be white. Need to update the display, as it's uploading every second
    win.blit(pendu_etapes[status], (150,100))
    pygame.display.update() #wouhou

    #for loop to make it possible to create events such as clicking with a mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #ability to close the game by clicking on the red cross X
            run = False #quit pygame
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() #how you get the position of the mouse. gives the position of the mouse, especially useful when clicking
            print(pos)
    

pygame.quit()