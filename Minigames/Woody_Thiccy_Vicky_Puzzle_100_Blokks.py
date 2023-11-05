import pygame, math, random
pygame.init()
#HIGH SCORES
# Normal: 1318
# Blocked: 0 Blocks Left 
# Randomized: 354
class GridSpace:
    def __init__(self, x = 1, y = 1, fill = False, color = (0, 0, 0)):
        self.x = x                          
        self.y = y
        self.fill = fill 
        self.color = color
    def __repr__(self):
        if self.fill:
            fillmsg = "Filled"
        else: 
            fillmsg = "Unfilled"
        return(str(self.x) + ", " + str(self.y) + ", " + fillmsg)
    def drawSpace(self):

        #determine the color of the piece based on the chosen color scheme
        if scheme == "default" or scheme == "halloween":
            usedColor = self.color
        elif scheme == "gradient1":
            usedColor = (self.y * 20 + 50, self.x * 20 + 50, 0)#self.y * 20 + 50)
        elif scheme == "gradient2":
            usedColor = (self.y *  20 + 50, 0, self.x * 20 + 50)
        elif scheme == "gradient3":
            usedColor = (0, self.y *  20 + 50, self.x * 20 + 50)

        if self.fill == True:
            betterRect(usedColor, self.x * 50, self.y * 50, self.x\
            * 50 + 50, self.y * 50 + 50, 0)

class Piece:
    def __init__(self, limbs = [], color = (0, 0, 0)):
        # The 'limbs' are a list of x and y values that make up a shape when
        # compared to a focal point. For example, The list [[1, 1], [1, 0], 
        # [0, 1]] plus the focal point [0, 0] would make a 2 by 2 square.
        self.limbs = limbs
        self.color = color

    def placeOntoGrid(self, focalX, focalY):
        global messagetext, currentPiece, score
        #first check if the piece can even be placed without bumping into anything
        roomToPlace = True

        #halloween colors
        if scheme != "halloween":
            usedColor = self.color
        else:
            usedColor = random.choice([(20, 20, 20), (255, 165, 0), (75, 0, 130), (255, 215, 0)])
        # In order to check if there's room for the limbs, we need to convert each 
        # limb into a position on the grid that we can use,
        # because right now they're probably all 1s or 2s or 0s.
        usableLimbCoords = []
        for limb in self.limbs:
            try:
                usableLimbCoords.append([limb[0] + focalX, limb[1] + focalY])
            except TypeError:
                pass
            #print(usableLimbCoords)

        # check if the piece will go off the screen
        # note: the breaks are there because once roomtoplace is false there's no
        # point checking anything else
        for limb in usableLimbCoords:
            if limb[0] > 10 or limb[0] < 1 or limb[1] > 10 or limb[1] < 1:
                #print('will go off screen')
                roomToPlace = False
                break
        for square in allSpaces:
            #check if there's room for the focal point
            if (square.x == focalX and square.y == focalY) and square.fill:
                #print('no room for focal point')
                roomToPlace = False
                break
            #check if there's room for each limb
            if [square.x, square.y] in usableLimbCoords and square.fill:
                #print('no room for limb')
                roomToPlace = False
                break
        #now draw it if there's room for it
        if roomToPlace:
            messagetext = largefont.render(randomMessage(), True, (0, 0, 0), (backgroundcol))
            fillSquare(focalX, focalY, usedColor)#random_color())
            for limb in self.limbs:
                try:
                    fillSquare(focalX + limb[0], focalY + limb[1], usedColor)#random_color())
                    score += 1
                except:
                    pass
            score += 1
            currentPiece = changePiece(mode)
            print(computeBlockedLeft())
            
    
    def __eq__(self, other):
        return(self.limbs == other.limbs)
    
    def display(self):
        black = (0, 0, 0)
        #display limbs
        for limb in self.limbs:
            x = limb[0] * 25
            y = limb[1] * 25
            betterRectWidth(black, 700 + x, 150 + y, 25, 25)
        #display focal point
        betterRectWidth((70, 70, 70), 700, 150, 25, 25)

def betterRect(color, x1, y1, x2, y2, width = 0):
    pygame.draw.polygon(screen, (color), ([(x1, y1), (x2, y1), \
    (x2, y2), (x1, y2)]), width)

def betterRectWidth(color, x1, y1, w, h, width = 0):
    pygame.draw.polygon(screen, (color), ([(x1, y1), (x1 + w, y1), \
    (x1 + w, y1 + h), (x1, y1 + h)]), width)

#haha yes look i have made a necessary function yay
def inBetween(value, myMin, myMax):
    return(value >= myMin and value < myMax)

#ooh look another funcion that definitely appears in another place in the code!
def distanceFormula(x1, y1, x2, y2):
    return(int(math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )))

def drawGrid(color = (255, 255, 255), thickness = 5, clear = False):
    for xvalue in range(50, 551, 50):
        if not clear or xvalue == 50 or xvalue == 550:
            pygame.draw.line(screen, color, (xvalue, 50), (xvalue, 550), thickness)
    for yvalue in range(50, 551, 50):
        if not clear or yvalue == 50 or yvalue == 550:
            pygame.draw.line(screen, color, (50, yvalue), (550, yvalue), thickness)
def random_color(min = 0, max = 255):
    return (random.randint(min, max), random.randint(min, max), random.randint(min, max))
def getAllSpaces(arr):
    #This function gets a list of every space on the grid
    for x in range(1, 11):
        for y in range(1, 11):
            arr.append(GridSpace(x, y, False))
def isItOnGrid(target):
    return(target in range(50, 551))

def mouseOnGrid():
    return(isItOnGrid(mouseX) and isItOnGrid(mouseY))

def fillSquare(x, y, color = (0, 0, 0), bool = True):
    for square in allSpaces:
        if square.x == x and square.y == y:
            square.color = color
            square.fill = bool
def clearScreen():
    global score
    score = 0
    for square in allSpaces:
        square.fill = False
def randomPiece():
    return Piece([[random.randint(-1, 1), random.randint(-1, 1)], \
    [random.randint(-1, 1), random.randint(-1, 1)], \
    [random.randint(-2, 2), random.randint(-2, 2)]], \
    (random.randint(25, 255), random.randint(25, 255), random.randint(25, 255)))
def changePiece(funcMode = "normal"):
    if "normal" in funcMode:
        return(random.choice(possiblePieces))
    elif funcMode == "randomized":
        #for randomized mode u get one by ones to make it easier
        if random.randint(1, 6) == 6:
            return(Piece([], (125, 0, 125)))
        else:
            return(randomPiece())
def computeBlockedLeft():
    black = 0
    for square in allSpaces:
        if square.color == (0, 0, 0) and square.fill == True:
            black += 1
    return black
def randomMessage():
    return(random.choice(["Nice play gurl!", "thats a skinny play", \
        "mmm that play is a little sketch", "ew that move sucked", \
        "Can you lose soon?", "when will the thiccies arrive", \
        "love that play!!!", "GOOD PLA oh caps lock sry", \
        "Are you new to this? b/c like gurl.", "and thats the tea", \
        "Slime tutori- WAIT this isnt google sry haha", \
        "Your score: haha pranked I don't keep score", \
        "Congrats, you win! Jk you cant win this game haha", \
        "I have not seen a worse play literally ever", \
        "With plays like those you're gonna lose real soon hunny", \
        "A good play? from u? truly a rare sight", "can i go home yet", \
        "III wanna swiiing from the shandeleHEEEEE", \
        "after this game can we get some food?" , "smh at that move...",\
        "ill let u undo that awful play if u go get me some boba", \
        "i sense a thiccy", "this game is so boring can we do summ else", \
        "surprised u made it this far", "this next piece is my fav", \
        "#blocklivesmatter", "i ship the L piece and the | piece", \
        "the next ones gonna be a shape? i think", "I hate this peice    *piece",\
        "Warning: ur ugly hahahahahah", "oops wrong pieice sorry   *piece", \
        "ok lemme spill some tea real quick", "im so glad i dont have eyes bc um yeah", \
        "for $100 ill show you my circuit board" \
        ]))
def convertToGrid(target):
    # for this function we will convert an x or y value into a grid position
    # We will assume that the x or y value is somewhere on the 10 by 10 grid
    # Grid is between 50 and 550
    # I KNOW THIS IS REALLY BAD ILL COME BACK TO IT LATER I PROMISE IM LAZY AND IM SORRY
    if inBetween(target, 50, 100):
        return 1
    elif inBetween(target, 100, 150):
        return 2
    elif inBetween(target, 150, 200):
        return 3
    elif inBetween(target, 200, 250):
        return 4
    elif inBetween(target, 250, 300):
        return 5
    elif inBetween(target, 300, 350):
        return 6
    elif inBetween(target, 350, 400):
        return 7
    elif inBetween(target, 400, 450):
        return 8
    elif inBetween(target, 450, 500):
        return 9
    elif inBetween(target, 500, 550):
        return 10    

def clearRows():
    global score
    #iterate through each possible y value of a square
    for yValue in range(1, 11):

        #generate the list of all squares in a single row
        squaresBeingChecked = []
        for square in allSpaces:
            if square.y == yValue:
                squaresBeingChecked.append(square)

        #check if it's a complete row or not, assume its true
        completeRow = True
        for square in squaresBeingChecked:
            if not(square.fill == True):
                completeRow = False

        #Clear it!
        if completeRow:
            # This random function call is here because we want to make sure to clear
            # a row AND a column if both share a square and are complete
            clearColumns()
            score += 10
            for square in allSpaces:
                if square.y == yValue:
                    square.fill = False

def clearColumns():
    global score
    #iterate through each possible y value of a square
    for xValue in range(1, 11):

        #generate the list of all squares in a single row
        squaresBeingChecked = []
        for square in allSpaces:
            if square.x == xValue:
                squaresBeingChecked.append(square)

        #check if it's a complete row or not, assume its true and then set to false
        completeColumn = True
        for square in squaresBeingChecked:
            if not(square.fill == True):
                completeColumn = False

        #Clear it!
        if completeColumn:
            # DO NOT UNCOMMENT THIS. IT WILL BUG INTO INFINITY.
            # I AM DEFINITELY GOOD AT DEBUGGING dOn'T wOrRyY!!!1!!
            #clearRows()
            score += 10
            for square in allSpaces:
                if square.x == xValue:
                    square.fill = False

def drawAllThings():
    global scoretext, score
    #Clear screen
    screen.fill((backgroundcol))
    
    #Draw the grid
    if scheme == "halloween":
        drawGrid((150, 150, 150), 1, True)
    else:
        drawGrid((0, 0, 0), 1, False)

    #Draw each square that is filled
    for square in allSpaces:
        square.drawSpace()

    #text
    screen.blit(messagetext, (10, 10))
    scoretext = thiccfont.render("Score: " + str(score), True, (0, 0, 0), (backgroundcol))
    screen.blit(scoretext, (570, 550))
    #mouse debug
    #pygame.draw.circle(screen, (255, 255, 255), (mouseX, mouseY), 20)

    currentPiece.display()

def makeClick():
    if mouseOnGrid():
        if testingSquares:
            #For testing, clicking on a space will fill it in (or unfill if right click)
            gridX = convertToGrid(mouseX)
            gridY = convertToGrid(mouseY)
            if pygame.mouse.get_pressed()[2]:
                fillSquare(gridX, gridY, (0, 0, 0), False)
            else:
                currentPiece.placeOntoGrid(gridX, gridY)
                #fillSquare(gridX, gridY, True)
            
def selectMode():
    global mode
    if pressed and mouseY in range(350, 500):
        if inBetween(mouseX, 124, 282):
            mode = "normal"
        elif inBetween(mouseX, 315, 500):
            mode = "blockednormal"
        elif inBetween(mouseX, 524, 800):
            mode = "randomized"
    #draw rectangles that show what mode you have selected
    if mode == "normal":
        betterRect((0, 0, 0), 124, 395, 282, 450, 3)
    elif mode == "randomized":
        betterRect((0, 0, 0), 524, 395, 800, 450, 3)
    elif mode == "blockednormal":
        betterRect((0, 0, 0), 320, 395, 500, 450, 3)
#MAIN
#Pygame initialization
clock = pygame.time.Clock()
screen_width = 850
screen_height = 600
screen = pygame.display.set_mode([screen_width,screen_height])
done = False
#Variables that control whether debug/testing stuff is enabled    
testingSquares = True                    
#Other variables
allSpaces = []
getAllSpaces(allSpaces)
holding = False
scheme = "gradient" + str(random.randint(1, 3))
if scheme == "halloween":
    backgroundcol = (100, 100, 100)
else:
    backgroundcol = (200, 200, 200)
score = 0
play = False
mode = "normal"
holdingspace = False
#Number of black squares left to track blocked mode
blockedLeft = 0

# **** ALL PIECES ****
TwoByTwo = Piece([[1, 1], [1, 0], [0, 1]], (0, 255, 0))
ThreeByThree = Piece([[1, 0], [0, 1], [-1, 0], [0, -1], \
[-1, -1], [1, 1], [-1, 1], [1, -1]], (0, 50, 200))
OneByOne = Piece([], (125, 0, 125))
DownRightL2 = Piece([[0, 1], [0, 2], [1, 0], [2, 0]], (0, 255, 127))
UpRightL2 = Piece([[0, -1], [0, -2], [1, 0], [2, 0]], (0, 128, 0))
DownLeftL2 = Piece([[0, 1], [0, 2], [-1, 0], [-2, 0]], (123, 104, 238))
UpLeftL2 = Piece([[0, -1], [0, -2], [-1, 0], [-2, 0]], (0, 170, 170))
Vertical1 = Piece([[0, -1], [0, 1]], (255, 165, 0))
Vertical2 = Piece([[0, -1], [0, 1], [0, 2], [0, -2]], (255, 255, 0))
Horiz1 = Piece([[1, 0], [-1, 0]], (255, 0, 0))
Horiz2 = Piece([[1, 0], [-1, 0], [2, 0], [-2, 0]], (255, 20, 147))
vert = Piece([[0, 1]], (220, 20, 60))
horiz = Piece([[1, 0]], (230, 230, 250))
star1 = Piece([[1, 1], [-1, -1], [-1, 1], [1, -1]], (255, 215, 0))
star2 = Piece([[1, 0], [-1, 0], [0, 1], [0, -1]], (0, 255, 255))
DownRightL1 = Piece([[0, 1], [1, 0]], (0, 255, 127))
UpRightL1 = Piece([[0, -1], [1, 0]], (0, 128, 0))
DownLeftL1 = Piece([[0, 1], [-1, 0]], (123, 104, 238))
UpLeftL1 = Piece([[0, -1], [-1, 0]], (0, 170, 170))
hole = Piece([[-1, 0], [1, 0], [-1, 1], [1, 1], [0, 2], [1, 2], [-1, 2]], (75, 0, 130))

#crazy random piece that changes each game
myPiece = randomPiece()

#select a piece
possiblePieces = [myPiece, UpLeftL1, DownLeftL1, UpRightL1, DownRightL1, star2, vert, horiz, TwoByTwo, ThreeByThree, OneByOne, DownRightL2, UpRightL2, DownLeftL2, UpLeftL2, Vertical1, Vertical2, Horiz1, Horiz2]

# text variables
largefont = pygame.font.SysFont(None, 45)
smallfont = pygame.font.SysFont(None, 30)
thiccfont = pygame.font.SysFont(None, 60)
widefont = pygame.font.SysFont(None, 100)
messagetext = largefont.render("uh like welcome to the game?", True, (0, 0, 0), (backgroundcol))
scoretext = thiccfont.render("Score: " + str(score), True, (0, 0, 0), (backgroundcol))
introtext = thiccfont.render("Press Space to Play / Restart", True, (0, 0, 0), (backgroundcol))
titletext = thiccfont.render("THICC BLOCCS", True, (0, 0, 0), (backgroundcol))
modestext = thiccfont.render("Normal     Blocked    Randomized", True, (0, 0, 0), (backgroundcol))


while not play and not done:
    #TITLE SCREEN
    clock.tick(60)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True     

    #text
    screen.fill((backgroundcol))
    screen.blit(titletext, (260, 10))
    screen.blit(introtext, (135, 200))
    screen.blit(modestext, (129, 400))

    #press space to play
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        play = True

    #Get raw input from the mouse (this will be converted into usable data during makeClick)
    pressed = pygame.mouse.get_pressed()[0]
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    selectMode()

    pygame.display.flip()

currentPiece = changePiece(mode)

while not done:
    #MAIN GAME
    clock.tick(60)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True 
    #Get raw input from the mouse (this will be converted into usable data during makeClick)
    pressed = pygame.mouse.get_pressed()[0]
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    #Clicking the mouse does stuff, but not holding it
    if pressed:
        if not holding:
            #print('click!')
            makeClick()
        holding = True
    else:
        holding = False
    #getting input from the keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if not holdingspace:
            #space clears the whole game 
            clearScreen()
            scheme = "gradient" + str(random.randint(1, 3))
            #reset the random piece for normal mode
            myPiece = randomPiece()
            possiblePieces = [myPiece, UpLeftL1, DownLeftL1, UpRightL1, DownRightL1, star2, vert, horiz, TwoByTwo, OneByOne, DownRightL2, UpRightL2, DownLeftL2, UpLeftL2, Vertical1, Vertical2, Horiz1, Horiz2]
            #blocked mode is too hard with the three by three so i only add it in normal
            if mode == "normal":
                possiblePieces.append(ThreeByThree)
            #fill screen with random stuff for Blocked mode
            if mode == "blockednormal":
                for square in allSpaces:
                    if random.randint(1, 4) == 4:
                        square.fill = True 
                        square.color = (0, 0, 0)
            blockedLeft = computeBlockedLeft()
            holdingspace = True  
    else:
        holdingspace = False
    #if keys[pygame.K_k]:
        #currentPiece = random.choice(possiblePieces)

    #clear rows
    clearRows()
    #clear columns
    clearColumns()
    #DRAWINGS
    drawAllThings()

    pygame.display.flip()
pygame.quit()