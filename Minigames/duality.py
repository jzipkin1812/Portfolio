import pygame
pygame.init()
clock = pygame.time.Clock()
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode([screen_width,screen_height])
done = False

class Player:
    def __init__(self, x, y, color = (255, 255, 255), size = 30):
        self.color = color
        self.x = x
        self.y = y
        self.xv = 0
        self.yv = 0
        self.size = size
        self.grounded = False
        self.holdingup = False
    def draw(self):
        betterRect(self.color, self.x, self.y, self.x + self.size, self.y + self.size, 0)
    def moveKeys(self):
        #check keys
        keys = pygame.key.get_pressed()
        #X
        #left
        if keys[pygame.K_LEFT]:
            self.xv = max(self.xv - 0.5, -5)
        #right
        elif keys[pygame.K_RIGHT]:
            self.xv = min(self.xv + 0.5, 5) 
        #friction
        else:
            if self.xv > 0:
                self.xv -= 1
            elif self.xv < 0:
                self.xv += 1
        #Y
        #jump
        if keys[pygame.K_UP]:
            if (not self.holdingup) and self.grounded:
                self.grounded = False
                self.yv -= 20  
            self.holdingup = True
        else:
            self.holdingup = False
        
        if not self.grounded:
            self.yv += 0.75

    def moveApply(self):
        self.x += self.xv
        self.y += self.yv
    def collide(self, platform):
        #if colliding: self.gronuded = true else: false
        left = self.x
        right = self.x + self.size
        down = self.y + self.size  
        up = self.y
        modifier = self.size
        #left and right collision
        if (platform.y1 < up < platform.y2 or platform.y1 < down < platform.y2):
            if (platform.x1 <= right <= platform.x1 + modifier):
                self.xv = 0
                self.x = platform.x1 - self.size
            elif (platform.x2 - modifier <= left <= platform.x2):
                self.xv = 0
                self.x = platform.x2
        #up and down collision
        if (platform.x1 <= left <= platform.x2 or platform.x1 <= right <= platform.x2):
            if platform.y1 <= down <= platform.y1 + modifier and self.yv >= 0:
                self.y = platform.y1 - modifier
                self.yv = 0
                return True
            elif platform.y2 - modifier <= up <= platform.y2 and self.yv < 0:
                self.yv = 0
                self.y = platform.y2 + 2
                return False

        #else:
            #self.grounded = False

class Platform:
    def __init__(self, x1, y1, x2, y2, color = (150, 150, 150)):
        self.color = color
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.grounded = False
    def draw(self):
        betterRect(self.color, self.x1, self.y1, self.x2, self.y2, 0)

def betterRect(color, x1, y1, x2, y2, width = 0):
    pygame.draw.polygon(screen, (color), ([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]), width)
def distanceFormula(x1, y1, x2, y2):
    return(int(math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )))
def drawAllThings():
    #clear screen
    screen.fill((0, 0, 0))

    #player draw
    player1.draw()
    player2.draw()

    #level objects
    for plat in levelPlatforms:
        plat.draw()


player1 = Player(300, 200)
player2 = Player(100, 100)
levelPlatforms = [Platform(425, 300, 475, 600), Platform(100, 400, 800, 450), Platform(100, 300, 200, 350), Platform(600, 200, 800, 250)]
while not done:
    clock.tick(60)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True 
    #draw stuff
    drawAllThings()

    for plat in levelPlatforms:
        if player1.collide(plat):
            player1.grounded = True
            break
        player1.grounded = False
    player1.moveKeys()
    player1.moveApply()

    for plat in levelPlatforms:
        if player2.collide(plat):
            player2.grounded = True
            break
        player2.grounded = False
    player2.moveKeys()
    player2.moveApply()

    #print(player1.grounded)
    pygame.display.flip()
pygame.quit()