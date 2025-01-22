import pygame
import os
import math

#settings for display
pygame.init() #initializes the display module
WIDTH, HEIGHT = 800, 500 #setting the size of the game window
win = pygame.display.set_mode((WIDTH, HEIGHT)) #initializes a windows with WIDTH and HEIGHT parameters
pygame.display.set_caption("Le Super Jeu du Pendu!") #game's title 
WHITE = (255,255,255)
BLACK=(0,0,0)

#buttons variables
#creating the circle around the letter
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH-(RADIUS*2+GAP)*13)/2)
starty = 400
#adding the letter in the circle
A = 65 #cf ascii, A = 65, B=66... et ajouter dans append A +i
LETTER_FONT= pygame.font.SysFont('Arial',30)

for i in range(26):
    x=startx+GAP*2+((RADIUS*2+GAP)*(i%13)) #i%13 est une fonction périodique qui fait 0,1,2...12 et réitère dès qu'on passe l'élément 13. RADIUS*2+GAP distance entre les boutons. GAP*2 crée un gap différent avec les bords de l'écran, qui sera différent de l'écart entre les boutons
    y= starty+(i//13*(GAP+RADIUS*2))
    letters.append([x,y, chr(A+i), True]) #chr convertit le chiffre en ascii, True makes our elements visible




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


def draw():
    win.fill(WHITE) #doesn't work, every second the screen should be white. Need to update the display, as it's uploading every second

    #draw buttons
    for letter in letters: #in letters, there a list in which we put the quadruplet for the circle, the letter and its position. x and y are the position, ltr is the ascii letter associated with this element in the loop. visible check if the item is visible or not. we use this loop to draw a circle and put the letter in
        x,y,ltr,visible=letter
        if visible: #when an input happens in a button, visible will become false, so it will disappear thanks to this line
            pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
            text=LETTER_FONT.render(ltr,1,BLACK)
            win.blit(text, (x - text.get_width()/2,y-text.get_height()/2))

    win.blit(pendu_etapes[status], (50,50))
    pygame.display.update() #wouhou

while run:
    clock.tick(FPS)#clock object that's counting at 60 FPS

    draw()

    #for loop to make it possible to create events such as clicking with a mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #ability to close the game by clicking on the red cross X
            run = False #quit pygame
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos() #how you get the position of the mouse. gives the position of the mouse, especially useful when clicking
            for letter in letters:
                x, y, ltr, visible = letter
                if visible: #don't check for collision of mouse input unless this button is visible
                    distance = math.sqrt((x - m_x)**2+(y-m_y)**2) #pythagore
                    if distance < RADIUS:
                        letter[3]=False #the fourth element of the quadruplet will be false, meaning the letter will disappear
                        print(ltr)

pygame.quit()

#for the mouse input : we need to check if the mouse input is in a range less than the distance between the center of a circle and the radius