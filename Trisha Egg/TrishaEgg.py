import pygame
import math
import random
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

class Trisha:
    def __init__(self, name, rarity, image, multiplier = 1, x = 50, y = 100):
        self.name = name
        self.rarity = rarity
        #initialize color based on rarity
        if self.rarity == "Common":
            self.textColor = [200, 200, 200]
        elif self.rarity == "Rare":
            self.textColor = [100, 100, 255]
        elif self.rarity == "Epic":
            self.textColor = [148, 0, 211]
        elif self.rarity == "Legendary":
            self.textColor = [255, 215, 0] 
        self.image = image
        self.multiplier = multiplier
        self.x = x
        self.y = y

    def display(self):
        screen.blit(resize(self.image, self.multiplier), (self.x, self.y))
    def displayText(self):
        screenText(80, 50, (self.name + "  (" + self.rarity + ")"), 60, self.textColor)

def betterRect(color, x1, y1, x2, y2, width = 0):
    pygame.draw.polygon(screen, (color), ([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]), width)

def distanceFormula(x1, y1, x2, y2):
    return(int(math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )))

def resize(image, multiplier):
    width = image.get_rect().size[0]
    height = image.get_rect().size[1]

    return(pygame.transform.scale(image, (int(width * multiplier), int(height * multiplier))))
def screenText(x, y, text = "Default", size = 70, color = [200, 200, 200], background = None):
    tempFont = pygame.font.SysFont(None, size)
    tempText = tempFont.render(text, True, color, background)
    screen.blit(tempText, (x, y))

def incrementCrack(num):
    if num < 3:
        value = num + 1
    else:
        value = 0

    if value < 3:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('crack.wav'))   

    return value

def chooseTrisha():
    rarity = random.randint(0, 100)
    if rarity < 40:
        #common
        trish = random.choice(commons)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('tada.wav'))
    elif rarity < 70:
        #rare
        trish = random.choice(rares)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('wow.wav'))
    elif rarity < 90:
        #epic
        trish = random.choice(epics)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('secret.wav'))
    else:
        #legendary
        trish = random.choice(legendaries)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('kingTut.wav'))

    return(trish)
def displayAll():
    #clear screen
    screen.fill((255, 105, 180))
    
    #text conditionally displays
    screenText(240, 690, "Reset", 60, [255, 255, 255])
    if crackStage < 3:
        screenText(7, 5, "You got a Trisha Variety Egg!", 60, [255, 255, 255])
        screenText(180, 40, "Click to open!", 60, [255, 255, 255])
        screen.blit(goldEgg, (25, 60))

    else:
        screenText(7, 5, "Congratulations! You found:", 60, [255, 255, 255])
        selectedTrisha.display()
        selectedTrisha.displayText()


#pygame variables
clock = pygame.time.Clock()
screen_width = 600
screen_height = 750
screen = pygame.display.set_mode([screen_width,screen_height])
done = False

#images
goldEgg = pygame.image.load("goldEgg.png")
glamTrisha = pygame.image.load("glamTrisha.jpg")
dominosTrisha = pygame.image.load("dominosTrisha.PNG")
kawaiiTrisha = pygame.image.load("kawaiiTrisha.PNG")
sadTrisha = pygame.image.load("sadTrisha.PNG")
pinkTrisha = pygame.image.load("pinkTrisha.PNG")
emoTrisha = pygame.image.load("emoTrisha.PNG")
afroTrisha = pygame.image.load("afroTrisha.PNG")
egyptTrisha = pygame.image.load("egyptTrisha.PNG")
cowboyTrisha = pygame.image.load("cowboyTrisha.PNG")
ursulaTrisha = pygame.image.load("ursulaTrisha.PNG")

#game variables and start the music
crackStage = 0
pygame.mixer.Channel(0).play(pygame.mixer.Sound('eggSpawn.wav'))

#lists of Trisha types
commons = [Trisha("Emo Trisha", "Common", emoTrisha), Trisha("Glam Trisha", "Common", glamTrisha, 0.8), \
Trisha("Sad Trisha", "Common", sadTrisha, 1, 50, 180)]

rares = [Trisha("Dominos Trisha", "Rare", dominosTrisha, 0.95, 80), Trisha("Cowboy Trisha", "Rare", cowboyTrisha, 1),\
Trisha("Pink Trisha", "Rare", pinkTrisha, 0.8, 70)]

epics = [Trisha("Kawaii Trisha", "Epic", kawaiiTrisha, 0.8, 41), Trisha("Afro Trisha", "Epic", afroTrisha, 0.6, 35), \
Trisha("Ursula Trisha", "Epic", ursulaTrisha, 1, 70)]

legendaries = [Trisha("Tut Trisha", "Legendary", egyptTrisha, 1.1, 120, 120)]

selectedTrisha = commons[0]

while not done:
    clock.tick(60)
    for event in pygame.event.get(): 
        #clicking x button
        if event.type == pygame.QUIT:
            done = True
        #clicking el mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            #cracking the egg
            if(80 < pygame.mouse.get_pos()[1] < 600 and (crackStage < 3)):
                crackStage = incrementCrack(crackStage)
                #choose a Trisha randomly
                if(crackStage == 3):
                    selectedTrisha = chooseTrisha()
            #resetting the game
            elif(600 < pygame.mouse.get_pos()[1]):
                crackStage = 0
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('eggSpawn.wav'))

                

    displayAll()
    pygame.display.flip()
pygame.quit()