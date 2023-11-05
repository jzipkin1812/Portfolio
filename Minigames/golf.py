import pygame
import math
pygame.init()

class GolfBall:
    def __init__(self, x, y, velocity = 0, directionAngle = 0):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.direction = directionAngle
        self.size = 15
    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.size)
    def move(self):
        self.x += math.cos(math.radians(self.direction)) * self.velocity
        self.y -= math.sin(math.radians(self.direction)) * self.velocity
    def connectMouse(self):
        pygame.draw.line(screen, (255, 255, 255), (int(self.x), int(self.y)), \
        (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 3)
    def hitByMouse(self):
        mousex = pygame.mouse.get_pos()[0]
        mousey = pygame.mouse.get_pos()[1]

        

        #first augment magnitude
        self.velocity += distanceFormula(self.x, self.y, mousex, mousey) / 20

        #next augment angle



def betterRect(color, x1, y1, x2, y2, width = 0):
    pygame.draw.polygon(screen, (color), ([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]), width)
def distanceFormula(x1, y1, x2, y2):
    return(int(math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )))
def thetaToPosition(angle, magnitude):
	return( [magnitude * math.cos(math.radians(self.direction)), \
	magnitude * math.sin(math.radians(self.direction))] )

clock = pygame.time.Clock()
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode([screen_width,screen_height])
done = False

testBall = GolfBall(100, 100, 0, -45)
while not done:
    #limit framerate
    clock.tick(60)

    #detect input
    for event in pygame.event.get(): 
        #quit the game
        if event.type == pygame.QUIT:
            done = True

        #click
        if event.type == pygame.MOUSEBUTTONDOWN :
            testBall.hitByMouse()

    #fill screen
    screen.fill((0, 0, 0))
    
    #operate test ball
    testBall.move()
    testBall.draw()
    testBall.connectMouse()
    
    #update display
    pygame.display.flip()
pygame.quit()