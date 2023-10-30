import pygame, math
pygame.init()
clock = pygame.time.Clock()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])
done = False

class Right_Triangle:
    def __init__(self, w, h, originx = 0, originy = 500, moveX = 0, moveY = 0, color = (255, 255, 255)):
        self.h = h #Height
        self.w = w #Width
        self.hypotenuse = float(math.sqrt(h ** 2 + w ** 2))
        self.originx = originx
        self.originy = originy
        self.top = originy - h
        self.right = originx + w
        self.movex = moveX
        self.movey = moveY
        self.color = color
    
    def __repr__(self):
        return("Right triangle with sides " + str(self.h) + ", " + \
            str(self.w) + ", and " + str(self.hypotenuse) + ".")
    
    def drawTriangle(self, color = (240, 240, 240), thickness = 0):
        pygame.draw.polygon(screen, (color), ([(self.originx, \
        self.originy), (self.originx, self.top), (self.right, \
        self.originy)]), thickness)

    def getArea(self):
        return(abs(self.h * self.w) / 2)

    def double(self):
        self.h *= 2 #Height
        self.w *= 2 #Width
        self.hypotenuse = float(math.sqrt(self.h ** 2 + self.w ** 2))
        self.top = self.originy - self.h
        self.right = self.originx + self.w

    def reverse(self):
        h = self.h
        self.h = self.w #Height
        self.w = h #Width
        self.hypotenuse = float(math.sqrt(self.h ** 2 + self.w ** 2))
        self.top = self.originy - self.h
        self.right = self.originx + self.w

    def flip180(self):
        self.h *= -1 #Height
        self.w *= -1 #Width
        self.hypotenuse = float(math.sqrt(self.h ** 2 + self.w ** 2))
        self.top = self.originy - self.h
        self.right = self.originx + self.w

    def flipx(self):
        self.w *= -1 #Width
        self.hypotenuse = float(math.sqrt(self.h ** 2 + self.w ** 2))
        self.top = self.originy - self.h
        self.right = self.originx + self.w

    def flipy(self):
        self.h *= -1 #Height
        self.hypotenuse = float(math.sqrt(self.h ** 2 + self.w ** 2))
        self.top = self.originy - self.h
        self.right = self.originx + self.w

    def translate(self, xamount, yamount):
        self.originx += xamount
        self.originy += yamount
        self.top = self.originy - self.h
        self.right = self.originx + self.w

    def makeRect(self):
        self.translate(self.w, (self.h * -1))
        self.flip180()

    def bounce(self):
        if self.top <= 0 or self.originy >= 500:
            self.movey *=  -1
            self.flip180()
        if self.right >= 500 or self.originx <= 0:
            self.movex *= -1
            self.flip180()
        return

    def animateWithMovement(self):
	    self.translate(self.movex, self.movey)
	    self.drawTriangle(self.color)

myTri = Right_Triangle(50, 75, 100, 300, 1.25, 1.75, (0, 0, 0))
otherTri = Right_Triangle(75, 50, 100, 200, 1.75, 1.25, (255, 255, 255))
direction = "downRight"

while not done:
    clock.tick(100)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True 

    screen.fill((150, 150, 150))
    myTri.bounce()
    myTri.animateWithMovement()
    otherTri.bounce()
    otherTri.animateWithMovement()

    pygame.display.flip()
pygame.quit()