import pygame, random, math
clock = pygame.time.Clock()
screen_width = 700
screen_height = 562
screen = pygame.display.set_mode([screen_width,screen_height])
done = False
mousey = 0
mousex = 0
line_width = 6
circolor = (0, 0, 0)
circBlack = True
#Possible values: 31, 93, 155, 217, 279, 341, 403, 465
indicatory = 465
r = 255
g = 255
b = 255
holding = False

# KEY GUIDE
# Left Mouse: Draw
# Right Mouse: Random Color
# Middle Mouse: Straight Lines
# F: Fill the screen with the chosen color
# Space: Fill the screen with black
# C: Draw a circle
# Minus: Make all circles unfilled
# Plus: Make all circles filled

def distanceFormula(x1, y1, x2, y2):
    return(int(math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )))

while not done:
    #clock.tick(10)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True 
    #See where the mouse was last time
    if not (pygame.mouse.get_pressed()[1]):
        prevmousey = mousey
        prevmousex = mousex
    #See where the mouse is
    if holding == False:
        mousey = pygame.mouse.get_pos()[1]
        mousex = pygame.mouse.get_pos()[0]
    elif holding == True: 
        mousey = pygame.mouse.get_pos()[1]
        mousex = min(pygame.mouse.get_pos()[0], screen_width - 100)

    #press keys = do things
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        screen.fill((0, 0, 0))
    elif keys[pygame.K_f]:
        screen.fill((r, g, b))
    
    #Change whether the circle is filled or not
    if keys[pygame.K_UP]:
        circBlack = False
    elif keys[pygame.K_DOWN]:
        circBlack = True

    #construct midpoint
    if keys[pygame.K_m]:
        pygame.draw.circle(screen, (r, g, b), ( (mousex + prevmousex) // 2, (mousey + prevmousey) // 2), 8)

    if circBlack:
        circolor = (0, 0, 0)
    elif not circBlack:
        circolor = (r, g, b)

    #if u right clicc color change
    if pygame.mouse.get_pressed()[2]:
        r = random.randint(50, 255)
        g = random.randint(50, 255)
        b = random.randint(50, 255)
    #Draw lines
    if pygame.mouse.get_pressed()[0]:
        if mousex < screen_width - 100:
            
            #CIRCLES
            if keys[pygame.K_c]:
                if not holdingmouse:
                    circlex = mousex
                    circley = mousey
                if holdingmouse and not keys[pygame.K_LCTRL]:
                    myrad = int(distanceFormula(circlex, circley, mousex, mousey))
                    #pygame.draw.circle(screen, (circolor), (circlex, circley), myrad)
                    pygame.draw.circle(screen, (r, g, b), (circlex, circley), myrad, min(int(distanceFormula(circlex, circley, mousex, mousey)), 3))

            #LINES
            elif not keys[pygame.K_LCTRL]:
                pygame.draw.line(screen, (r, g, b), (prevmousex, prevmousey), (mousex, mousey), line_width)
        else:
            #Change color for squares
            #Possible values: 31, 93, 155, 217, 279, 341, 403, 465
            if mousey <= 62:
                r = 255
                g = 0
                b = 0
                indicatory = 31
            elif mousey <= 124:
                r = 255
                g = 165
                b = 0
                indicatory = 93
            elif mousey <= 186:
                r = 255
                g = 255
                b = 0
                indicatory = 155
            elif mousey <= 248:
                r = 0
                g = 255
                b = 0
                indicatory = 217
            elif mousey <= 310:
                r = 0
                g = 0
                b = 255
                indicatory = 279
            elif mousey <= 372:
                r = 255
                g = 0
                b = 255
                indicatory = 341
            elif mousey <= 434:
                r = 100
                g = 100
                b = 100
                indicatory = 403
            elif mousey <= 500:
                r = 255
                g = 255
                b = 255
                indicatory = 469
            else:
                r = 102
                g = 51
                b = 0
                indicatory = 531
        holdingmouse = True
    else:
        holdingmouse = False
    #Color squares
    #Red
    pygame.draw.polygon(screen, (255, 0, 0), ([(screen_width - 100, 0), (screen_width - 100, 62), (screen_width, 62), (screen_width, 0)]) ,0)
    #Orange
    pygame.draw.polygon(screen, (255, 165, 0), ([(screen_width - 100, 62), (screen_width - 100, 124), (screen_width, 124), (screen_width, 62)]) ,0)
    #Yellow
    pygame.draw.polygon(screen, (255, 255, 0), ([(screen_width - 100, 124), (screen_width - 100, 186), (screen_width, 186), (screen_width, 124)]) ,0)
    #Green
    pygame.draw.polygon(screen, (0, 255, 0), ([(screen_width - 100, 186), (screen_width - 100, 248), (screen_width, 248), (screen_width, 186)]) ,0)
    #Blue
    pygame.draw.polygon(screen, (0, 0, 255), ([(screen_width - 100, 248), (screen_width - 100, 310), (screen_width, 310), (screen_width, 248)]) ,0)
    #Purple
    pygame.draw.polygon(screen, (255, 0, 255), ([(screen_width - 100, 310), (screen_width - 100, 372), (screen_width, 372), (screen_width, 310)]) ,0)
    #Grey
    pygame.draw.polygon(screen, (100, 100, 100), ([(screen_width - 100, 372), (screen_width - 100, 434), (screen_width, 434), (screen_width, 372)]) ,0)
    #White
    pygame.draw.polygon(screen, (255, 255, 255), ([(screen_width - 100, 434), (screen_width - 100, 500), (screen_width, 500), (screen_width, 434)]) ,0)
    #Brown
    pygame.draw.polygon(screen, (102, 51, 0), ([(screen_width - 100, 500), (screen_width - 100, 562), (screen_width, 562), (screen_width, 500)]) ,0)

    #This circle indicates what color u have picked
    pygame.draw.circle(screen, (0, 0, 0), (screen_width - 50, indicatory), 10, 0)
    pygame.display.flip()
pygame.quit()
