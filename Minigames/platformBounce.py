#IMPORTS
import pygame
pygame.init()
#CLASSES
class Platform:
    def __init__(self, x1, y1, x2, y2, color = (150, 150, 150)):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.color = color

    def draw(self):
        pygame.draw.polygon(screen, (self.color), ([(self.x1, self.y1), (self.x2, self.y1), (self.x2, self.y2), (self.x1, self.y2)]), 0)

class Ball:
    def __init__(self, color = (150, 150, 150), radius = 20, x = 0, y = 0):
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        #x velocity
        self.xv = 0
        #y velocity
        self.yv = 0
        #maximum velocity (absolute value)
        self.xvmax = 100
        self.yvmax = 100
        self.grounded = False
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius, 0)
    
    def collisionDown(self, platform):
        colliding = (platform.x1 <= self.x <= platform.x2) and  \
        (int(self.y + self.radius) in range(platform.y1, platform.y2 + 1))

        if colliding:
            self.y = platform.y1 - self.radius
            self.yv *= -1
        return colliding
    
    def collisionUp(self, platform):
        colliding = (platform.x1 <= self.x <= platform.x2) and  \
        (int(self.y - self.radius) in range(platform.y1, platform.y2 + 1))

        if colliding:
            self.y = platform.y2 + self.radius
            self.yv = 0
        return colliding

    def collisionLeft(self, platform):
        colliding = (platform.y1 <= self.y <= platform.y2) and  \
        (int(self.x - self.radius) in range(platform.x1, platform.x2 + 1))

        if colliding:
            self.x = platform.x2 + self.radius
            self.xv *= -1  
        return colliding

    def collisionRight(self, platform):
        colliding = (platform.y1 <= self.y <= platform.y2) and  \
        (int(self.x + self.radius) in range(platform.x1, platform.x2 + 1))

        if colliding:
            self.x = platform.x1 - self.radius
            self.xv *= -1 
        return colliding


    def movex(self, value, collPlatforms):
        #Check collision
        isColliding = False
        #collision if the ball is moving right
        if value > 0:
            for platform in collPlatforms:
                if self.collisionRight(platform):
                    isColliding = True
        #collision if the ball is moving left
        elif value < 0:
            for platform in collPlatforms:
                if self.collisionLeft(platform):
                    isColliding = True
        if not(isColliding):
            self.x += value
    
    def movey(self, value, collPlatforms):
        #Check collision
        isColliding = False
        #collision if the ball is moving down
        if value > 0:
            for platform in collPlatforms:
                if self.collisionDown(platform):
                    isColliding = True
        #collision if the ball is moving up
        elif value < 0:
            for platform in collPlatforms:
                if self.collisionUp(platform):
                    isColliding = True
        if not(isColliding):
            self.y += value

    def checkAllCollisions(self, platforms):
        for platform in platforms:
            self.collisionUp(platform)
            self.collisionDown(platform)
            self.collisionRight(platform)
            self.collisionLeft(platform)

    def applyVelocity(self):
        if self.xv > self.xvmax:
            self.xv = self.xvmax
        elif self.xv < -1 * self.xvmax:
            self.xv = -1 * self.xvmax
        if self.yv > self.yvmax:
            self.yv = self.yvmax
        elif self.yv < -1 * self.yvmax:
            self.yv = -1 * self.yvmax
        self.movex(self.xv, CurrentPlatforms)
        self.movey(self.yv, CurrentPlatforms)
    
    def eightDirectionArrows(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.yv -= 2
        #if keys[pygame.K_DOWN]:
            #self.yv += 3
        if keys[pygame.K_RIGHT]:
            self.xv += 1
        if keys[pygame.K_LEFT]:
            self.xv -= 1


#FUNCTIONS
def betterRect(color, x1, y1, x2, y2, width = 0):
    pygame.draw.polygon(screen, (color), ([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]), width)
def distanceFormula(x1, y1, x2, y2):
    return(int(math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )))
#MAIN
clock = pygame.time.Clock()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode([screen_width,screen_height])
done = False
myball = Ball(color = (90, 150, 255), x = 300, y = 150, radius = 25)
blue = (25, 100, 255)
CurrentPlatforms = [Platform(0, 0, 50, 600, blue), Platform(0, 0, 600, 50, blue), \
Platform(550, 0, 600, 600, blue), Platform(0, 550, 600, 600, blue)]
while not done:
    clock.tick(60)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True 

    #Clear screen
    screen.fill((0, 0, 0))

    #keys
    keys = pygame.keys = pygame.key.get_pressed()
    #pressing keys moves the ball
    myball.eightDirectionArrows()
    myball.yv += 1
    
    myball.applyVelocity()
    myball.checkAllCollisions(CurrentPlatforms)

    for platform in CurrentPlatforms:
        platform.draw()
    
    myball.draw()
    
    pygame.display.flip()
pygame.quit()