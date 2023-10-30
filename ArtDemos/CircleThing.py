import pygame, math
pygame.init()
clock = pygame.time.Clock()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])
done = False
myRad = 50
def col():
	return max(255 - circleDi(), 0)
def inversecol():
	return min(circleDi(), 255)
def circleDi():
	return int(distanceFormula(250, 250, mousex, mousey))
def distanceFormula(x1, y1, x2, y2):
    return(int(math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )))
def betterRect(color, x1, y1, x2, y2, width = 0):
    pygame.draw.polygon(screen, (color), ([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]), width)
while not done:
    #clock.tick(100)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True 
    #mouse
    mousey = pygame.mouse.get_pos()[1]
    mousex = pygame.mouse.get_pos()[0]

    myRad = circleDi()

    #betterRect((150, 150, 150), 100, 100, 400, 400)
    myCircle = pygame.draw.circle(screen, (col(), col(), inversecol()), (250, 250), myRad, min(circleDi(), 10))
    
    pygame.display.flip()
pygame.quit()