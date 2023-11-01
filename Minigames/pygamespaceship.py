import pygame
import random
#INITIALIZATION HELLLLLL
pygame.init()
clock = pygame.time.Clock()
screen_width = 500
screen_height = 500
boundaryS = -2000
boundaryL = 3000
screen = pygame.display.set_mode([screen_width,screen_height])
done = False
clearscreen = True
animate = 40
#Velocity & Movement
xmod = 0
ymod = 0
xvelocity = 0
yvelocity = 0
orientation = "up"

#Colors
starRed = [204, 81, 57]
starBlue = [64, 121, 178]
starYellow = [245, 247, 190]
starWhite = [255, 255, 255]

#Text handler
myfont = pygame.font.SysFont('Comic Sans MS', 20)
textsurface = myfont.render('Detailed Spaceship', False, (255, 255, 255))

#In order to generate random starts we will get a list of their y pos and x pos, as well as color
numberofstars = 2250
starxpos = []
starypos = []
starcolors = []
for i in range(numberofstars):
    starcolors.append(random.choice([starWhite, starYellow, starWhite, starRed, starBlue, starYellow, starWhite]))
    starxpos.append(random.randint(boundaryS, boundaryL))
    starypos.append(random.randint(boundaryS, boundaryL))

#We'll do the same thing to daw meteors as we did with stars
meteorxpos = []
meteorypos = []
numberofmeteors = 35
for i in range(numberofmeteors):
    meteorxpos.append(random.randint(boundaryS, boundaryL))
    meteorypos.append(random.randint(boundaryS, boundaryL))

#Now we will generate the wormhole position
wormx = 0#random.randint(boundaryS + 200, boundaryL - 200)
wormy = 0#random.randint(boundaryS + 200, boundaryL - 200)

def drawSmartCircle(r, g, b, x, y, radius, width):
    global xmod
    global ymod
    if x + xmod >= 0 and y + ymod >= 0:
        pygame.draw.circle(screen, (r, g, b), (x + xmod, y + ymod), radius, width)
def drawOrientedSpaceship(orientation):
    #Center of iso triangle = median of base and mpt of legs
    if orientation == "up":
        pygame.draw.polygon(screen, (255, 255, 255), ([(250, 225), (265, 275), (235, 275)]), 0)
    elif orientation == "down":
        pygame.draw.polygon(screen, (255, 255, 255), ([(250, 275), (265, 225), (235, 225)]), 0)
    elif orientation == "left":
        pygame.draw.polygon(screen, (255, 255, 255), ([(225, 250), (275, 265), (275, 235)]), 0)
    elif orientation == "right":
        pygame.draw.polygon(screen, (255, 255, 255), ([(275, 250), (225, 265), (225, 235)]), 0)
#Main loop
while not done:
    clock.tick(60)
    #Clear screen
    if clearscreen == True:
        screen.fill((0, 0, 0))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        yvelocity -= 4
        orientation = "down"
    elif keys[pygame.K_UP]:
        yvelocity += 4
        orientation = "up"
    if keys[pygame.K_LEFT]:
        xvelocity += 4
        orientation = "left"
    elif keys[pygame.K_RIGHT]:
        xvelocity -= 4
        orientation = "right"

    #Top speed
    if xvelocity > 16:
        xvelocity = 16
    elif xvelocity < -16:
        xvelocity = -16
    if yvelocity > 16:
        yvelocity = 16
    elif yvelocity < -16:
        yvelocity = -16

    ymod += yvelocity
    xmod += xvelocity
    xvelocity = int(xvelocity * 0.9)
    yvelocity = int(yvelocity * 0.9)
    #print("Y: " + str(ymod))
    #print("X: " + str(xmod))

    #Now the wormhole
    for i in range(animate, 0, -1):
        drawSmartCircle(i * 2, i * 5, i * 6, wormx, wormy, i, 0)
    if (xmod + wormx) in range(210, 290) and (ymod + wormy) in range(210, 290):
        clearscreen = not clearscreen
    #Draw the stars using the list of their positions and random colors
    for i in range(numberofstars):
        drawSmartCircle(starcolors[i][0], starcolors[i][1], starcolors[i][2], starxpos[i], starypos[i], 2, 0)
    
    #Same but with meteors
    for i in range(numberofmeteors):
        drawSmartCircle(100, 100, 100, meteorxpos[i], meteorypos[i], 30, 0)
        drawSmartCircle(60, 60, 60, meteorxpos[i] + 10, meteorypos[i] + 10, 8, 0)
        drawSmartCircle(60, 60, 60, meteorxpos[i] - 15 , meteorypos[i] - 5, 8, 0)
    
    #Boundaries
    if xmod > -(boundaryS):
        xmod = -(boundaryS)
    if ymod > -(boundaryS):
        ymod = -(boundaryS)
    if xmod < ((boundaryS) - boundaryL) // 2:
        xmod = ((boundaryS) - boundaryL) // 2
    if ymod < ((boundaryS) - boundaryL) // 2:
        ymod = ((boundaryS) - boundaryL) // 2 

    #Ship
    drawOrientedSpaceship(orientation)
    #Edit the size of the wormhole to make it look animated
    if animate == 40:
        upordown = -1
    elif animate == 10:
        upordown = 1
    animate += upordown
    pygame.display.flip()
pygame.quit()
