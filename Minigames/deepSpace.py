import pygame, math, random
pygame.init()

class Player:
    def __init__(self):
        self.x = 250
        self.y = 400
        self.size = 7
        self.xv = 0
        self.yv = 0
        self.color = [120, 0, 200]

    def draw(self):
        pygame.draw.circle(screen, (self.color), (self.x, self.y), self.size, 0)
    def move(self, keys):
        if keys[pygame.K_DOWN]:
            self.y += 4
        if keys[pygame.K_UP]:
            self.y -= 4
        if keys[pygame.K_LEFT]:
            self.x -= 4
        if keys[pygame.K_RIGHT]:
            self.x += 4

        #apply velocity
        self.x += self.xv
        self.y += self.yv
    def collide(self, fish):
        if self.size > fish.size:
            self.size += 1
            allFishes.remove(fish)
        elif self.size < fish.size:
            self.size = 7
    def detectCollision(self, fish):
        if distanceFormula(self.x, self.y, fish.x, fish.y) <= self.size + fish.size:
            self.collide(fish)

class Fish:
    def __init__(self, x, y, size, xv, yv, color = [50, 20, 150]):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.xv = xv
        self.yv = yv
    def draw(self):
        pygame.draw.circle(screen, (self.color), (self.x, self.y), self.size, 0)
    def move(self):
        self.x += self.xv
        self.y += self.yv

def betterRect(color, x1, y1, x2, y2, width = 0):
    pygame.draw.polygon(screen, (color), ([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]), width)
def distanceFormula(x1, y1, x2, y2):
    return(int(math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )))
def housekeeping():
    clock.tick(60)
    screen.fill((backgroundCol))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            return True
    return False

clock = pygame.time.Clock()
screen_width = 1000
screen_height = 700
frames = 0
screen = pygame.display.set_mode([screen_width,screen_height])
backgroundCol = [10, 10, 20]
allFishes = []
done = False
player1 = Player()

while not done:
    done = housekeeping()
    keys = pygame.key.get_pressed()

    #increment frames
    frames += 1

    #operate player
    player1.draw()
    player1.move(keys)

    #operate fishes
    #spawn
    if frames % 10 == 0:
        allFishes.append(Fish(random.randint(0, screen_width), 0, random.randint(3, max(40, player1.size + 10)), 0, \
        random.randint(1, 5), [50 + random.randint(-20, 50), 20 + random.randint(-20, 50), 150 + random.randint(-20, 50)]))
    #other
    i = 0
    while(i < len(allFishes)):
        allFishes[i].draw()
        allFishes[i].move()
        if allFishes[i].y > screen_height + allFishes[i].size:
            allFishes.pop(i)
            i -= 1
        player1.detectCollision(allFishes[i])
        i+= 1

    
    pygame.display.flip()
pygame.quit()