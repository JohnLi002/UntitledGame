import pygame

#Initialize the pygame
pygame.init() 

#Create the screen
screen = pygame.display.set_mode((800,600))

running = True


#Title and Icon
pygame.display.set_caption("This is a game")
icon = pygame.image.load("Pentagon.png")
pygame.display.set_icon(icon)


#Allows screen to continue existing until it is exited
while running:
    #Checks for events that happen to the screen
    for event in pygame.event.get():
        #if the exit button on the screen is pressed the loops will stop
        if event.type == pygame.QUIT:
            running = False