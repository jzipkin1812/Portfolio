import pygame
import random
import math
import assets as a
import utility as u
import gameStateInfo as gs
import button as b
import level as l
import ball 

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

#Functions that correlate to specific game buttons

#pygame variables 
clock = pygame.time.Clock()
screen_width = 1200
screen_height = 750
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Raise the Bar")
done = False  
frames = 0

#The game state object carries almost all the information about everything going on in the game.
#To shorten the game loop, we will be updating the game state's instance variables,
#rather than variables local to this file.
mainStatus = gs.GameStateInfo(screen)

#Cursor processing for fun visuals!
pygame.mouse.set_visible(False)
cursor_img_rect = a.cursorImage.get_rect()

while not mainStatus.quit:
    clock.tick()
    mainStatus.tickTime = clock.get_time() 
    mainStatus.updateFrames()

    #Background handling
    screen.fill((0, 0, 0))
    
    #Display appropriate backgrounds using the GameState object
    mainStatus.displayBackground()

    #Cursor processing
    cursor_img_rect.center = pygame.mouse.get_pos()  # update position 
    screen.blit(a.cursorImage, cursor_img_rect) # draw the cursor
    
    #All sources of user input
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    for event in pygame.event.get(): 
        #Clicking x button
        if event.type == pygame.QUIT:
            mainStatus.quit = True
        #Clicking the mouse on gameButtons
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mainStatus.inGame:
                mainStatus.clearClick(mouseX, mouseY)
            elif mainStatus.instructorScreen:
                pass
                #Borders: 104 211, 492 214, 878 215
                #Select LANA
                if 104 <= mouseX <= 355 and 211 <= mouseY <= 462:
                    mainStatus.borderX = 88
                    mainStatus.borderY = 195
                    mainStatus.reset(l.Lana())
                #Select GLITCH BETTY
                elif 492 <= mouseX <= 492 + 251 and 214 <= mouseY <= 465:
                    mainStatus.borderX = 475
                    mainStatus.borderY = 198
                    mainStatus.reset(l.Betty())
                #Select GERRI
                elif 878 <= mouseX <= 878 + 251 and 215 <= mouseY <= 466:
                    mainStatus.borderX = 862
                    mainStatus.borderY = 199
                    mainStatus.reset(l.Gerri())
        #Key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mainStatus.incrementScreen()
            if event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT] and len(mainStatus.buttons) > 0:
                mainStatus.clear(event.key)
        #The check stack event is timed by milliseconds, not by frames.
        if event.type == 10 and mainStatus.inGame and mainStatus.trackStarted:
            mainStatus.checkStack()
    
    #Update frame-by-frame stuff

    #Debug: Display mouse position x and y
    u.screenText(10, 10, screen, "x: " + str(mouseX) + " / y: " + str(mouseY), 30)
    #Debug: Display FPS
    u.screenText(10, 40, screen, "FPS: " + str(int(clock.get_fps())), 30)

    pygame.display.flip()
pygame.quit()