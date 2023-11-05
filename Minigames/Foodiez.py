import pygame
import random
import math
pygame.init()
clock = pygame.time.Clock()
screen_width = 500
screen_height = 600
screen = pygame.display.set_mode([screen_width,screen_height])
center = (250, 250)
done = False
holding = False
makefood = False
selectedFood = 'cookie'
biteSize = 60
#colors
peru = (205, 133,  63)
lightSteelBlue = (176, 196, 222)
chocolate = (139, 69, 19)
steelBlue =  (70, 130, 180)
hotPink = (255, 105, 180)
babyBlue = (0, 191, 255)
gold = (255, 215, 0)
crimson = (220, 20, 60)
plum = (221, 160, 221)
white = (250, 250, 250)
cheese = (255, 215, 65)
red = (255, 0, 0)
yellow = (255, 255, 0)
lime = (0, 255, 0)
blue = (0, 0, 255)
darkChocolate = (110, 50, 5)

sprinkleColors = [plum, gold, babyBlue, crimson]

backgroundcol = lightSteelBlue
 
boun1x = 133
boun2x = 245
boun3x = 355
#text
largefont = pygame.font.SysFont(None, 45)
smallfont = pygame.font.SysFont(None, 30)
foodstext = largefont.render('Cookie    Pizza   Donut   Rainbow', True, (70, 70, 70), (lightSteelBlue))
biteSizeText = smallfont.render('Bite Size', True, (70, 70, 70))

def distanceFormula(x1, y1, x2, y2):
    return(int(math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )))

def closeToCenter(x, y):
    if x in range(180, 320) and y in range(180, 320):
        closetoc = True
    else:
        closetoc = False
    return(closetoc)

def drawPepperoni(x, y):
    pygame.draw.circle(screen, red, (x, y), 30)
    pygame.draw.circle(screen, (190, 0, 0), (x, y), 30, 5)
 
def drawSprinkle(x, y):
    pygame.draw.circle(screen, (random.choice(sprinkleColors)), (x, y), 10)

def drawChip(x, y):
    pygame.draw.circle(screen, (random.choice([chocolate, darkChocolate])), (x, y), 20)

def makebite(size = 35):
    pygame.draw.circle(screen, (backgroundcol), (mousex, mousey), size)

def randomperu():
    #this function will switch up the cookie color every time
    darkness = random.randint(-8, 8)
    return((205 + darkness, 133 + darkness, 63 + darkness))

def randDonut():
    return(random.randint(50, 450))

def sprinkle(num):
    for i in range(num):
        sprX = 250
        sprY = 250
        while distanceFormula(sprX, sprY, 250, 250) not in range(81, 185):
            sprX = randDonut()
            sprY = randDonut()
        drawSprinkle(sprX, sprY) 

def pepperoni(num):
    for i in range(num):
        pepX = 0
        pepY = 0
        while distanceFormula(pepX, pepY, 250, 350) not in range(70, 220):
            pepX = random.randint(100, 400)
            pepY = random.randint(150, 450)
        drawPepperoni(pepX, pepY) 

def drawFood(food = 'nothing'):
    if food == 'cookie':
        #draw main cookie body
        pygame.draw.circle(screen, chocolate, (258, 258), 200)
        pygame.draw.circle(screen, randomperu(), center, 200)
        #draw chocolate chips randomly
        for i in range(random.randint(18, 24)):
            chipX = 0
            chipY = 0
            while distanceFormula(chipX, chipY, 250, 250) not in range(175):
                chipX = randDonut()
                chipY = randDonut() 
            drawChip(chipX, chipY)
     
    elif food == 'donut':
        #draw main donut body
        pygame.draw.circle(screen, chocolate, (258, 258), 200)
        pygame.draw.circle(screen, randomperu(), center, 200)
 
        #draw frosting
        pygame.draw.circle(screen, random.choice([hotPink, chocolate]), center, 185 , 90)

        #draw the sprinkles randomly 
        sprinkle(random.randint(80, 90))

        #draw the hole
        pygame.draw.circle(screen, backgroundcol, center, 80)

    elif food == 'pizza':
        #draw the bread
        pygame.draw.circle(screen, randomperu(), (250, 350), 300)
        #draw the cheese
        pygame.draw.circle(screen, cheese, (250, 350), 250)
        #draw the pepperoni
        pepperoni(random.randint(12, 14))
        #draw the cover 
        pygame.draw.polygon(screen, backgroundcol, ([(0, 0,), (250, 500), (500, 0), (500, 600), (0, 600)]))
        #draw the shadow
        pygame.draw.line(screen, chocolate, (255, 500), (437, 120), 9)

    elif food == 'rainbow':
        for i in range(200):
            pygame.draw.circle(screen, random.choice([red, blue, hotPink, yellow, lime]), (random.randint(10, 500), random.randint(10, 500)), random.randint(10, 30))

def interfaceDisplay():
    #polygon that covers stuff
    pygame.draw.polygon(screen, backgroundcol, ([(0, 0,), (500, 0), (500, 30), (0, 30)]))
    #Display text
    screen.blit(foodstext, (8, 540))
    screen.blit(biteSizeText, (4, 8))

    #Bonudary lines
    pygame.draw.line(screen, steelBlue, (0, 530), (500, 530), 5)
    pygame.draw.line(screen, steelBlue, (boun1x, 530), (boun1x, 600), 5)
    pygame.draw.line(screen, steelBlue, (boun2x, 530), (boun2x, 600), 5)
    pygame.draw.line(screen, steelBlue, (boun3x, 530), (boun3x, 600), 5)
    pygame.draw.line(screen, steelBlue, (0, 30), (500, 30), 5)
    pygame.draw.line(screen, steelBlue, (100, 0), (100, 30), 5)

    #Circle that represents the bite size, line across it
    pygame.draw.circle(screen, (69, 69, 69), (int(biteSize) * 5, 15), 10)
    pygame.draw.line(screen, (69, 69, 69), (110, 15), (490, 15), 5)


def game_init():
    screen.fill((backgroundcol))

game_init()
while not done:
    #clock.tick(10)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True 
    #See where the mouse is
    mousey = pygame.mouse.get_pos()[1]
    mousex = pygame.mouse.get_pos()[0]
    #Clicking the mouse 
    if pygame.mouse.get_pressed()[0]:

        #select a different bite size
        if mousey < 30:
            if mousex > 110:# and holding == False:
                pygame.draw.circle(screen, backgroundcol, (int(biteSize) * 5, 15), 10)
                biteSize = int(mousex / 5)
        #bite
        elif mousey < 530:
            makebite(biteSize)

        #select another food
        elif holding == False:
            if mousex < boun1x:
                selectedFood = 'cookie'
            elif mousex >= boun1x and mousex <= boun2x:
                selectedFood = 'pizza'
            elif mousex >= boun2x and mousex <= boun3x:
                selectedFood = 'donut'
            else:
                selectedFood = 'rainbow'
            makefood = True

        holding = True
    else:
        holding = False

    #Draw the food
    if makefood:
        screen.fill(backgroundcol)
        drawFood(selectedFood)
        makefood = False

    #Spacebar clears the whole game
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not holdingspace:
        screen.fill((backgroundcol))
        makefood = True
        holdingspace = True
    elif not keys[pygame.K_SPACE]:
        holdingspace = False

    interfaceDisplay()

    pygame.display.flip()
pygame.quit()