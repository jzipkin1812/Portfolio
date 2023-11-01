import pygame, math
def betterRect(color, x1, y1, x2, y2, width = 0):
    pygame.draw.polygon(screen, (color), ([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]), width)
def distanceFormula(x1, y1, x2, y2):
    return(int(math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )))
class player:
    def __init__(self, x, y, size = 30, color = [100, 100, 30]):
        self.x = x
        self.y = y
        self.size = size
        self.center = [int((self.x * 2 + self.size) / 2),  int((self.y * 2 + self.size) / 2)]
        self.color = color
        self.orientation = "stop"
        self.holdingSpace = False
    def drawPlayer(self):
        betterRect(self.color, self.x, self.y, self.x+self.size, self.y+self.size, 1)
        betterRect([0, 0, 0], self.x + 1, self.y + 1, self.x + self.size - 1, self.y + self.size - 1, 0)
    def markCenter(self):
        betterRect([0, 0, 255], self.center[0] - 5, self.center[1] - 5, self.center[0] + 5, self.center[1] + 5, 0)
    def moveX(self, amount):
        self.x += amount
        self.center = [int((self.x * 2 + self.size) / 2),  int((self.y * 2 + self.size) / 2)]
    def moveY(self, amount):
        self.y += amount
        self.center = [int((self.x * 2 + self.size) / 2),  int((self.y * 2 + self.size) / 2)]
    def keyMove(self, platformList):
        keys = pygame.key.get_pressed()
        speed = 7
        if self.inField(platformList):
            speed = 4
        if keys[pygame.K_DOWN]:
            self.orientation = "down"
            self.moveY(speed)
        elif keys[pygame.K_UP]:
            self.orientation = "up"
            self.moveY(-1 * speed)
        elif keys[pygame.K_LEFT]:
            self.orientation = "left"
            self.moveX(-1 * speed)
        elif keys[pygame.K_RIGHT]:
            self.orientation = "right"
            self.moveX(speed)
    def screenLimit(self):
        if self.x + self.size >= 1200:
            self.x = 1199 - self.size
        if self.x <= 0:
            self.x = 1
        if self.y + self.size >= 675:
            self.y = 674 - self.size
        if self.y < 0:
            self.y = 0
    def getProjPoint(self, platformList, x, y, direction, draw = True):
        #mirrors = True
        mirrorForm = "null"
        if direction == "right":
            projPoint = [1200, y]
            for form in platformList:
                if (form.y1 <= y <= form.y2) and (x <= form.x1) and (form.x1 <= projPoint[0]):
                    if (form.tag == "solid"):
                        projPoint = [form.x1, y]
                    elif (form.tag == "mirrorA" or form.tag == "mirrorB"):
                        if draw == False:
                            projPoint = self.getProjPoint(platformList, int((form.x1 + form.x2) / 2), int((form.y1 + form.y2) / 2), transformDirection(direction, form.tag), False) 
                        else:
                            projPoint = [form.x1, y]
                            mirrorForm = form
                            #self.projectLine(platformList, form.center[0], form.center[1], transformDirection(direction, form.tag))        
        
        if direction == "left":
            projPoint = [0, y]
            for form in platformList:
                if (form.y1 <= y <= form.y2) and (x >= form.x2) and (form.x2 >= projPoint[0]):
                    if (form.tag == "solid"):
                        projPoint = [form.x2, y]
                    elif (form.tag == "mirrorA" or form.tag == "mirrorB"):
                        if draw == False:
                            projPoint = self.getProjPoint(platformList, int((form.x1 + form.x2) / 2), int((form.y1 + form.y2) / 2), transformDirection(direction, form.tag), False) 
                        else:
                            projPoint = [form.x2, y]
                            mirrorForm = form
                            #self.projectLine(platformList, form.center[0], form.center[1], transformDirection(direction, form.tag))        
        
        if direction == "up":
            projPoint = [x, 0]
            for form in platformList:
                if ((form.x1 <= x <= form.x2) and (y >= form.y2) and (form.y2 >= projPoint[1])): 
                    if(form.tag == "solid"):
                        projPoint = [x, form.y2]
                    elif (form.tag == "mirrorA" or form.tag == "mirrorB"):
                        if draw == False:
                            projPoint = self.getProjPoint(platformList, int((form.x1 + form.x2) / 2), int((form.y1 + form.y2) / 2), transformDirection(direction, form.tag), False) 
                        else:
                            projPoint = [x, form.y2]
                            mirrorForm = form
                            #self.projectLine(platformList, form.center[0], form.center[1], transformDirection(direction, form.tag))                
        if direction == "down":
            projPoint = [x, 675]
            for form in platformList:
                if ((form.x1 <= x <= form.x2) and (y <= form.y1) and (form.y1 <= projPoint[1])):
                    if (form.tag == "solid"):
                        projPoint = [x, form.y1]
                    elif (form.tag == "mirrorA" or form.tag == "mirrorB"):
                        if draw == False:
                            projPoint = self.getProjPoint(platformList, int((form.x1 + form.x2) / 2), int((form.y1 + form.y2) / 2), transformDirection(direction, form.tag), False) 
                        else:
                            projPoint = [x, form.y1]
                            mirrorForm = form
                            #self.projectLine(platformList, form.center[0], form.center[1], transformDirection(direction, form.tag))
        if mirrorForm != "null":
            self.projectLine(platformList, mirrorForm.center[0], mirrorForm.center[1], transformDirection(direction, mirrorForm.tag))        
        return projPoint
    def projectLine(self, platformList, x, y, direction,size = 30):
        if direction == "stop":
            return
        #tempCenter = [int((x * 2 + size) / 2),  int((y * 2 + size) / 2)]
        finalProjPoint = self.getProjPoint(platformList, x, y, direction)
        if self.inField(platformList):
            return
        pygame.draw.line(screen, self.color, [x, y], finalProjPoint, 1)
        #if self.orientation == "down":
            #pygame.draw.line(screen, self.color, [x, y + size], finalProjPoint, 1)
        '''
        elif self.orientation == "up":
            pygame.draw.line(screen, self.color, [x, y], finalProjPoint, 1)
        elif self.orientation == "left":
            pygame.draw.line(screen, self.color, [x, y], finalProjPoint, 1)
        elif self.orientation == "right":
            pygame.draw.line(screen, self.color, [x + size, y], finalProjPoint, 1)
        '''
    def detectTrigger(self, platformList):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.orientation != "stop":
            if not self.holdingSpace and not self.inField(platformList):
                #shoot at buttons n stuff
                self.color = [255, 255, 255]
                temp_projPoint = self.getProjPoint(platformList, self.center[0], self.center[1], self.orientation, False)
                for form in platformList:
                    if form.secondx1 != "null":
                        if not self.collidingWithRect(platform(form.secondx1, form.secondy1, form.secondx2, form.secondy2)) and form.buttonx1 <= temp_projPoint[0] <= form.buttonx2 and form.buttony1 <= temp_projPoint[1] <= form.buttony2:
                            form.switch()
            self.holdingSpace = True
        else:
            if self.color[0] > 50:
                self.color[0] -= 5
            if self.color[2] > 50:
                self.color[2] -= 5
            self.holdingSpace = False
    def inField(self, platformList):
        for form in platformList:
            if form.tag == "field":
                if ((form.x1 < self.x < form.x2) or (form.x1 < self.x + self.size < form.x2)) \
                and ((form.y1 < self.y < form.y2) or (form.y1 < self.y + self.size < form.y2)):
                    return True
        return False
    def operateAll(self, platformList, levelVar):
        self.projectLine(platformList, int(self.x + (self.size / 2)), int(self.y + (self.size / 2)), self.orientation)
        #player1.markCenter()
        self.keyMove(platformList)
        self.detectTrigger(platformList)
        self.screenLimit()
        self.collideWithPlatforms(platformList, levelVar)
        self.drawPlayer()
    def collidingWithRect(self, rect):
        return ((self.x in range(rect.x1, rect.x2)  or  (self.x + self.size) in range(rect.x1, rect.x2)) \
        and (self.y in range(rect.y1, rect.y2)  or  (self.y + self.size) in range(rect.y1, rect.y2)))
    def collideWithPlatforms(self, platformList, levelVar):
        for i in platformList:
            if self.collidingWithRect(i) and i.tag != "field":
                if i.tag == "win":
                    levelVar += 1
                    switchlevels(levelVar)
                else:
                    if self.orientation == "down":
                        self.y = i.y1 - self.size - 1
                    elif self.orientation == "up":
                        self.y = i.y2 + 1
                    elif self.orientation == "right":
                        self.x = i.x1 - self.size - 1
                    elif self.orientation == "left":
                        self.x = i.x2 + 1


class platform: 
    def __init__(self, x1, y1, x2, y2, tag = "solid", secondx1 = "null", secondy1= "null", \
        secondx2 = "null", secondy2 = "null", buttonx1 = "null", buttony1 = "null", buttonx2 = "null", buttony2 = "null"):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.tag = tag
        self.secondx1 = secondx1
        self.secondy2 = secondy2
        self.secondy1 = secondy1
        self.secondx2 = secondx2
        self.buttonx2 = buttonx2
        self.buttonx1 = buttonx1
        self.buttony2 = buttony2
        self.buttony1 = buttony1

        self.center = int((self.x1 + self.x2) / 2), int((self.y1 + self.y2) / 2)

    def grateLines(self, priority):
        #horizontal
        if priority == "primary":
            for increment in range(self.y1, self.y2, 20):
                pygame.draw.line(screen, [40, 100, 40], [self.x1, increment], [self.x2, increment], 1)
            for increment in range(self.x1, self.x2, 20):
                pygame.draw.line(screen, [40, 100, 40], [increment, self.y1], [increment, self.y2], 1)
        elif priority == "secondary":
            for increment in range(self.secondy1, self.secondy2, 20):
                pygame.draw.line(screen, [40, 40, 40], [self.secondx1, increment], [self.secondx2, increment], 1)
            for increment in range(self.secondx1, self.secondx2, 20):
                pygame.draw.line(screen, [40, 40, 40], [increment, self.secondy1], [increment, self.secondy2], 1)
    def drawPlatform(self):
        #base
        if self.tag == "solid" or self.tag == "grate":
            if self.secondx1 == "null":
                betterRect([40, 100, 40], self.x1, self.y1, self.x2, self.y2, 1)
            else:
                betterRect([230, 230, 230], self.x1 + 1, self.y1 + 1, self.x2 - 1, self.y2 - 1, 1)
        elif self.tag == "win":
            betterRect([255, 255, 40], self.x1, self.y1, self.x2, self.y2, 1)
        elif self.tag == "field":
            #betterRect([130, 40, 40], self.x1, self.y1, self.x2, self.y2, 0)
            betterRect([173, 255, 47], self.x1, self.y1, self.x2, self.y2, 2)
            for yincrement in range(self.y1 + 1, self.y2, 20): 
                for xincrement in range(self.x1 + 1, self.x2, 20):
                    pygame.draw.circle(screen, [173, 255, 47], [xincrement, yincrement], 0, 0)
        elif self.tag == "mirrorA":
            betterRect([50, 255, 50], self.x1, self.y1, self.x2, self.y2, 1)
            pygame.draw.line(screen, [50, 255, 50], [self.x1, self.y1], [self.x2, self.y2], 1)
        elif self.tag == "mirrorB":
            betterRect([50, 255, 50], self.x1, self.y1, self.x2, self.y2, 1)
            pygame.draw.line(screen, [50, 255, 50], [self.x1, self.y2], [self.x2, self.y1], 1)
        #grate lines
        if self.tag == "grate":
            self.grateLines("primary")
        #scondary inactive platform
        if self.secondx1 != "null":
            betterRect([40, 40, 40], self.secondx1 + 1, self.secondy1 + 1, self.secondx2 - 1, self.secondy2 - 1, 1)
            if self.tag == "grate":
                self.grateLines("secondary")
            #button
            betterRect([150, 40, 40], self.buttonx1, self.buttony1, self.buttonx2, self.buttony2, 1)
    def switch(self):
        storage = platform(self.x1, self.y1, self.x2, self.y2, self.tag, self.secondx1, self.secondy1, self.secondx2, self.secondy2)

        self.secondx1 = storage.x1
        self.secondy1 = storage.y1
        self.secondx2 = storage.x2
        self.secondy2 = storage.y2

        self.x1 = storage.secondx1
        self.y1 = storage.secondy1
        self.x2 = storage.secondx2
        self.y2 = storage.secondy2

        self.center = int((self.x1 + self.x2) / 2), int((self.y1 + self.y2) / 2)

def switchlevels(level):
    global allForms, player1
    funcArr = ["nothing", level_1, level_2]
    #lower the level to the max one if you've finished all the levels
    while level >= len(funcArr):
        level -= 1
    #If theres no more levels, just restart the current level otherwise start the new level
    player1.orientation = "stop"
    allForms = funcArr[level]()[0]
    player1.x = funcArr[level]()[1][0]
    player1.y = funcArr[level]()[1][1]
def noFatList(inputList, fat):
    tempList = []
    for item in inputList:
        if item != fat:
            tempList.append(item)
    return tempList
def transformDirection(laser, mirror):
    if laser == "down":
        if mirror == "mirrorA":
            return "right"
        else:
            return "left"
    elif laser == "up":
        if mirror == "mirrorA":
            return "left"
        else:
            return "right"
    elif laser == "right":
        if mirror == "mirrorA":
            return "down"
        else:
            return "up"
    elif laser == "left":
        if mirror == "mirrorA":
            return "up"
        else:
            return "down"
def level_1():
    playerPos = [300, 550]
    levelForms = [platform(829, 450, 1149, 670, "field"), platform(1150, 0, 1200, 675), platform(925, 0, 975, 250), \
    platform(925, 250, 975, 400, "solid", 450, 0, 500, 200, 540, 0, 710, 25), platform(750, 0, 800, 200, "solid", 975, 400, 1150, 450, 995, 0, 1130, 25), \
    platform(510, 205, 750, 245, "grate"), platform(350, 200, 510, 250), platform(750, 200, 975, 250), platform(750, 400, 975, 450), platform(0, 400, 610, 450), \
    platform(610, 405, 750, 445, "grate"), platform(850, 80, 880, 110, "win")]
    return([levelForms, playerPos])
def level_2():
    playerPos = [100, 100]
    levelForms = [platform(300, 300, 500, 500), platform(700, 500, 740, 540, "mirrorA", 900, 300, 940, 340, 300, 0, 1100, 25), platform(1000, 80, 1030, 110, "win"), platform(900, 500, 940, 540, "mirrorB")]#, \
    #platform(1125, 300, 1150, 325, "solid", 1125, 400, 1150, 425, 300, 0, 1100, 25), platform(900, 300, 940, 340, "mirrorA")]
    return([levelForms, playerPos])

pygame.init()
clock = pygame.time.Clock()
screen_width = 1200
screen_height = 675
screen = pygame.display.set_mode([screen_width,screen_height])
done = False
holdingleft = False
holdingright = False
frames = 0
player1 = player(0, 0, 30, [50, 255, 50])
currentLevel = 1
allForms = []
switchlevels(currentLevel)
#allForms = allForms = [platform(829, 450, 1149, 670, "field"), platform(1150, 0, 1200, 675), platform(925, 0, 975, 250), platform(925, 250, 975, 400, "solid", 450, 0, 500, 200, 540, 0, 710, 25), platform(750, 0, 800, 200, "solid", 975, 400, 1150, 450, 995, 0, 1130, 25), platform(510, 205, 750, 245, "grate"), platform(350, 200, 510, 250), platform(750, 200, 975, 250), platform(750, 400, 975, 450), platform(0, 400, 610, 450), platform(610, 405, 750, 445, "grate")]
while not done:
    clock.tick(60)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True 
    #Clear screen
    screen.fill((12, 15, 0))

    #Frames
    frames += 1

    #player movement
    keys = pygame.key.get_pressed()


    #Get mouse positions
    mousey = pygame.mouse.get_pos()[1]
    mousex = pygame.mouse.get_pos()[0]
    #platforms
    for form in allForms:
        form.drawPlatform()
    #player
    player1.operateAll(allForms, currentLevel)
    #screen border
    betterRect([40, 100, 40], 0, 1, 1199, 674, 1)
    #Left mouse
    if pygame.mouse.get_pressed()[0]:   
        if not holdingleft:
            pass
        holdingleft = True
    else:
        holdingleft = False 

    pygame.display.flip()
pygame.quit()