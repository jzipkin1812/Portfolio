#dodge le circle
import random, pygame, math
pygame.init()

def betterRect(x1, y1, x2, y2):
    pygame.draw.polygon(screen, (0, 250, 250), ([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]), 0)
def distanceFormula(x1, y1, x2, y2):
    return(int(math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )))
def adjustBallColors():
    if scheme == 'blue':
        colorArray = ([0, 0, 125], [0, 0, 255], [0, 125, 125], [0, 255, 255])
    elif scheme == 'green':
        colorArray = ([0, 125, 0], [0, 255, 0], [50, 100, 50], [125, 255, 125])
    elif scheme == 'red':
        colorArray = ([125, 0, 0], [255, 0, 0], [230, 230, 0], [255, 125, 0])
    elif scheme == 'pink':
        colorArray = ([125, 0, 125], [255, 0, 255], [255, 0, 125], [125, 0, 255])
    return colorArray
def adjustBackground():
    if scheme == 'blue':
        backCol = (0, 20, 60)
    elif scheme == 'green':
        backCol = (0, 50, 0)
    elif scheme == 'red':
        backCol = (75, 0, 0)
    elif scheme == 'pink':
        backCol = (50, 0, 50)
    return backCol

clock = pygame.time.Clock()
screen_width = 650 
screen_height = 500
backgroundcol = (0, 0, 0)
globalrad = 20
lose = False
mousey = pygame.mouse.get_pos()[1]
mousex = pygame.mouse.get_pos()[0]
screen = pygame.display.set_mode([screen_width,screen_height])
done = False
basicfont = pygame.font.SysFont(None, 48)
YouLose = basicfont.render('You lose!', True, (255, 255, 255), \
(backgroundcol))
scoredisplay = basicfont.render('Score: 0', True, (255, 255, 255), \
(backgroundcol))

while not done:
    frames = 0
    restart = False
    movementspeed = 6
    spawnspeed = 10
    lose = False
    allcircles = []

    #Make all colors randomly
    scheme = random.choice(['green', 'red', 'blue', 'pink'])
    colors = adjustBallColors()
    backgroundcol = adjustBackground()

    #adjust text color to fit background
    YouLose = basicfont.render('You lose!', True, (255, 255, 255), \
    (backgroundcol))
    while not done and not lose:
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
        clock.tick(70)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True 
        screen.fill((backgroundcol))
        
        frames += 0.5
        #create moar circles, increase circle speed over time, also circles appear more frequently as the game goes on
        if frames % 75 == 0 and spawnspeed >= 2:
            spawnspeed -= 1
            #globalrad += 1
        if spawnspeed == 1 and frames % 200 == 0:
            movementspeed += 1
        if frames % spawnspeed == 0:
            allcircles.append([0, random.randint(0, 500), random.choice(colors), random.randint(-1, 1)])
        #After 200 points, spawn double circles
        if frames // 10 >= 200 and frames % 2 == 0:
            allcircles.append([0, random.randint(10, 490), random.choice(colors), random.randint(-1, 1)])
        #move circles forward with variation
        for circle in allcircles:
            circle[0] += (movementspeed + circle[3])
        #Gain score
        scoredisplay = basicfont.render('Score: ' + str(frames // 10), True, (255, 255, 255), (backgroundcol))
        screen.blit(scoredisplay, (10, 10))

        mousey = pygame.mouse.get_pos()[1]
        mousex = pygame.mouse.get_pos()[0]
        
        #draw the circles
        for circle in allcircles:
            pygame.draw.circle(screen, (circle[2]), (circle[0], circle[1]), globalrad, 0)
        #if you collide with a circle you lose
        for circle in allcircles:
            #circle[0] = x, circle[1] = y
            if distanceFormula(mousex, mousey, circle[0], circle[1]) in range(globalrad):
                lose = True
        #if circlex - mousex in range(-10, 10) and circley - mousey in range(-10, 10):
            #lose = True
        pygame.display.flip()

    while not done and not restart:
        clock.tick(25)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True 
        screen.fill((backgroundcol))
        screen.blit(YouLose, (180, 202))
        screen.blit(scoredisplay, (182, 250))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            restart = True
        pygame.display.flip()
pygame.quit()