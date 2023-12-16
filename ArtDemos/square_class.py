import pygame, math, random, time
pygame.init()
clock = pygame.time.Clock()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])
lineWidth = 5
widthChange = 1
done = False

def random_color(min = 0, max = 255):
    return (random.randint(min, max), random.randint(min, max), random.randint(min, max))

class Square:
    def __init__(self, s = 5, originx = 0, originy = screen_height, moveX = 0, moveY = 0, color = (255, 255, 255)):
        self.s = s #Side length
        self.originx = originx
        self.originy = originy
        self.movex = moveX
        self.movey = moveY
        self.color = color
    
    def __repr__(self):
        return("Square with side length " + str(self.s) + ".")
    def getCenterX(self):
        return((self.originx * 2 + self.s) // 2)
    def getCenterY(self):
        return((self.originy * 2 + self.s) // 2)
    def drawSquare(self, color = (240, 240, 240), thickness = 0):
        selections = [(self.color), (self.originy // 3 + 50, self.originx // 3 + 50, 0), (self.originy // 3 + 50, 0, self.originx // 3 + 50), (0, self.originy // 3 + 50, self.originx // 3 + 50)]

        pygame.draw.polygon(screen, (selections[colorsetting]), ([(self.originx, \
        self.originy), (self.originx, self.originy + self.s), (self.originx + self.s, self.originy + self.s), \
        (self.originx + self.s, self.originy)]), thickness)

    def drawAsCircle(self):
        pygame.draw.circle(screen, (self.color), (int((self.originx * 2 + self.s) / 2), int((self.originy * 2 + self.s) / 2) ), int(self.s / 2),  0)
    
    def getArea(self):
        return(self.s ** 2)

    def double(self):
        self.s *= 2

    def translate(self, xamount, yamount):
        self.originx += xamount
        self.originy += yamount

    def bounce(self):
        if self.originy <= 0 or self.originy + self.s >= screen_height:
            self.movey *= -1
        if self.originx + self.s >= screen_width or self.originx <= 0:
            self.movex *= -1

    def animateWithMovement(self, shape = "square"):
        self.translate(self.movex, self.movey)
        if shape == "square":
            self.drawSquare()
        elif shape == "circle":
            self.drawAsCircle()

    def bounceAround(self, shape = "square"):
        self.bounce()
        self.animateWithMovement(shape)

    def clickingOnSquare(self):
        if pygame.mouse.get_pressed()[0] :
            #See where the mouse is
            mousey = int(pygame.mouse.get_pos()[1])
            mousex = int(pygame.mouse.get_pos()[0])

            #See if ur clicking in a square
            if (self.originx <= mousex <= self.originx + self.s) and \
            (self.originy<= mousey <= self.originy + self.s):
                return True
        return False

    def addcolor(self, amount):
        self.color = list(self.color)
        for i in range(len(self.color)):
            if  0 <= self.color[i] *amount <= 255:
                self.color[i] *= amount
                self.color[i] = int(self.color[i])
        self.color = tuple(self.color)

#different fun settings
def streakUp():
    global randomSquares
    side = 10
    if random.randint(0, 3) == 3:
        randomSquares.append(Square(side, random.randint(0, screen_width - side), \
            500 - side, 0, random.random() * 1.25, random_color(0, 255)))
    #destroy squares to prevent lag
    for square in randomSquares:
        if square.originy <= 0:
            randomSquares.remove(square)
    for sq in randomSquares:
        sq.bounceAround()
        if sq.clickingOnSquare():
            randomSquares.remove(sq)

def increaseSizeSquares():
    global randomSquares 
    if len(randomSquares) < 500:
        for i in range(3):
            side = random.randint(1, 1)
            randomSquares.append(Square(side, random.randint(side, screen_width - side), \
            random.randint(side, screen_height - side), random.randint(-1 * speedrange, speedrange) / 10, \
            random.randint(-1 * speedrange, speedrange) / 10, random_color(0, 255)))
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        for square in randomSquares:
            square.s += 1
    screen.fill((0, 0, 0))
    for sq in randomSquares:
        sq.bounceAround()
        if sq.clickingOnSquare():
            randomSquares.remove(sq)
            #randomSquares.remove(sq)
def streakSquares():
    global randomSquares
    if len(randomSquares) < 1000:
        side = 10
        randomSquares.append(Square(side, random.randint(side, screen_width - side), \
        random.randint(side, screen_height - side), random.randint(-1 * speedrange, speedrange) / 10, \
        random.randint(-1 * speedrange, speedrange) / 10, random_color(0, 255)))
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        screen.fill((0, 0, 0))

    for sq in randomSquares:
        sq.bounceAround()
        if sq.clickingOnSquare():
            randomSquares.remove(sq)
def squareLines(specialWidth):
    global randomSquares, squareInit
    screen.fill((0, 0, 0))
    if not squareInit:
        for repeat in range(100):
            side = 10
            randomSquares.append(Square(side, random.randint(side, screen_width - side), \
            random.randint(side, screen_height - side), random.randint(-1 * speedrange, speedrange) / 10, \
            random.randint(-1 * speedrange, speedrange) / 10, random_color(0, 255)))
        squareInit = True
    #for sq in randomSquares:

    if pygame.mouse.get_pressed()[0]:
        mousey = int(pygame.mouse.get_pos()[1])
        mousex = int(pygame.mouse.get_pos()[0])
        for sq in randomSquares:
            pygame.draw.line(screen, sq.color, (sq.getCenterX(), sq.getCenterY()), (mousex, mousey), specialWidth)
    #draw squares
    for sq in randomSquares:
        sq.bounceAround("square")
x = 1
xmod = 1
'''
marinaSquare = Square(15, 70, 40, 15, 7.5, (255, 0, 255))
abbySquare = Square(75, 300, 300, 2, -1.5, (200, 125, 0))
javinSquare = Square(50, 290, 320, 5, 7, (0, 120, 250))
'''
colorsetting = 0 
randomSquares = []
speedrange = 10
frames = 0
squareInit = False                            
while not done:
    clock.tick(100)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True 
    frames += 1
    #if frames % 300 == 0:
        #colorsetting = random.choice([1, 2, 3])

    #square designs
    #increaseSizeSquares()
    squareLines(5)
    #streakSquares()

    #change width
    #print(lineWidth)
    if frames % 10 == 0:
        lineWidth += widthChange
        if lineWidth == 9 or lineWidth == 1:
            widthChange *= -1

    pygame.display.flip()
pygame.quit()