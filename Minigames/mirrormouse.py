#Module initialization
import pygame
pygame.init()
clock = pygame.time.Clock()

#starting level
level = 1

#setting up the screen
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])

#these variables track if the player has quit the game or not, and if they have touched an obstacle
done = False
lose = False

#this variable tracks if the player JUST started the level
levelstart = 6
#text display initialization
basicfont = pygame.font.SysFont(None, 48)
text = basicfont.render('You lose!', True, (255, 255, 255), (0, 0, 0))
press_space = basicfont.render('Press space to restart.', True, (255, 255, 255), (0, 0, 0))

#level initialization - this is essentially the code for level 0
obstacles = []
key = []
keyobstacles = []

#colors
aqua = (0, 210, 210)
lime = (0, 200, 0)

#mouse position initialization
flipy = abs(pygame.mouse.get_pos()[1])
flipx = 250 - abs(pygame.mouse.get_pos()[0] - 250)

#i hate the pygame rect function so this is better yay
def betterRect(color, x1, y1, x2, y2):
    pygame.draw.polygon(screen, (color), ([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]), 0)

while not done:
    lose = False
    restart = False
    levelstart = 15
    while not done and not lose:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True 
        #clear screen
        screen.fill((0, 100, 100))
        #at the beginning of the level make sure the mouse position is at the start
        if levelstart > 0:
            pygame.mouse.set_pos([375, 495])
            levelstart -= 1
            lose = False
        
        #place the obstacles for each level
        if level == 1:
            obstacles = [[0, 200, 150, 350], [180, 0, 250, 100]]
            key = []
            keyobstacles = []
        if level == 2:
            obstacles = [[50, 300, 200, 450], [50, 50, 200, 200], [0, 230, 100, 270], [150, 230, 250, 270]]
            key = []
            keyobstacles = []
        if level == 3:
            obstacles = [[30, 0, 250, 220], [30, 280, 250, 475], [0, 240, 85, 260], [105, 0, 250, 300]]
            key = []
            keyobstacles = []
        if level == 4:
            obstacles = [[100, 100, 150, 400], [150, 100, 250, 150]]
            if levelstart > 0:
                key = [[200, 200]]
                keyobstacles = [[0, 100, 100, 125]]
        if level == 5:
            obstacles = [[200, 0, 250, 25], [40, 0, 115, 325], [0, 350, 115, 500], [135, 200, 250, 500], [40, 0, 210, 160]]
            if levelstart > 0:
                key = [[230, 50]]
                keyobstacles = [[40, 325, 115, 350]]
        if level == 6:
            obstacles = [[0, 0, 100, 75], [150, 0, 250, 75], [0, 425, 100, 500], [150, 425, 250, 500], [0, 0, 10, 500], [240, 0, 250, 500]]
            if levelstart > 0:
                key = [[125, 250]]
                keyobstacles = [[100, 50, 150, 75]]
            if keyobstacles == []:
                obstacles.append([30, 125, 220, 150])
                obstacles.append([30, 125, 55, 300])
                obstacles.append([190, 125, 220, 300])
        if level == 7:
            obstacles = []
            if levelstart > 0:
                key = []
                keyobstacles = []
        if level == 8:
            obstacles = []
            if levelstart > 0:
                key = []
                keyobstacles = []
        if level == 9:
            obstacles = []
            if levelstart > 0:
                key = []
                keyobstacles = []

        #See where the mouse is, flipped over a vertical line
        prevy = flipy
        prevx = flipx

        flipy = abs(pygame.mouse.get_pos()[1])
        flipx = 250 - abs(pygame.mouse.get_pos()[0] - 250)

        #pygame.draw.circle(screen, (0, 0, 255), (flipx, flipy), 5, 0)
        
        #to avoid a mouse jerk bug we will now
        #check collision with obstacles
        for i in obstacles:
            if levelstart == 0 and (((pygame.mouse.get_pos()[0] < 250) or (flipx in range(i[0], i[2]) and flipy in range(i[1], i[3])))):#player colliding with a rect
                lose = True    
                #level -= 1    

        #check collision with key obstacles
        for i in keyobstacles:
            if levelstart == 0 and (((pygame.mouse.get_pos()[0] < 250) or (flipx in range(i[0], i[2]) and flipy in range(i[1], i[3])))):
                lose = True    
                #level -= 1    
        
        #check collision with a key - if u collect the key u delete key obstacles
        for i in key:
            if levelstart == 0 and (flipy in range(i[1] - 20, i[1] + 20) and flipx in range(i[0] - 20, i[0] + 20)):
                key = []
                keyobstacles = []
        
        #Draw the finish line
        pygame.draw.line(screen, (lime), (0, 1), (500, 1), 10)

        #draw the obstacles
        for i in obstacles:
            betterRect(aqua, i[0], i[1], i[2], i[3])        

        #draw the key obstacles
        for i in keyobstacles:
            betterRect(lime, i[0], i[1], i[2], i[3])    
        
        #Draw the divide
        pygame.draw.line(screen, (aqua), (250, 0), (250, 500), 6)

        #Draw the key
        if len(key) > 0:
            for i in key:
                pygame.draw.circle(screen, (lime), (i[0], i[1]), 20, 0)
        #Draw marker
        #pygame.draw.circle(screen, (0, 0, 255), (flipx, flipy), 10, 0)

        #calculate if the player has won or not
        if flipy <= 5 and levelstart == 0:
            level += 1
            levelstart = 3

        pygame.display.flip()
    
    while not restart and not done:
        #This is the 'u lose' screen
        #clear screen
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    done = True 
        screen.blit(text, (180, 202))
        screen.blit(press_space, (100, 230))
        
        #restart the game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            restart = True
        if keys[pygame.K_DOWN]:
            level = 1
        pygame.display.flip()
pygame.quit()