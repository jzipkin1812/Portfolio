import pygame, random
pygame.init()
clock = pygame.time.Clock()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode([screen_width,screen_height])
done = False
holding = False
#T = Top, B = Bottom, M = Middle, R = Right, L = Left
tr = [False, "tr", 500, 100]
tm = [False, "tm", 300, 100]
tl = [False, "tl", 100, 100]
mr = [False, "mr", 500, 300]
mm = [False, "mm", 300, 300]
ml = [False, "ml", 100, 300]
br = [False, "br", 500, 500]
bm = [False, "bm", 300, 500]
bl = [False, "bl", 100, 500]
turnsymbol = "x"
allSquares = [tr, tm, tl, mr, mm, ml, br, bm, bl]
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
def drawSymbol(surface, centerx, centery):
    col = random_color()
    if turnsymbol == "x":
        pygame.draw.line(surface, col, (centerx + 55, centery + 55), (centerx - 55, centery - 55), 4)
        pygame.draw.line(surface, col, (centerx - 55, centery + 55), (centerx + 55, centery - 55), 4)
    elif turnsymbol == "o":
        pygame.draw.circle(surface, col, (centerx, centery), 80, 4)
def switchTurns():
    global turnsymbol
    if turnsymbol == "o":
        turnsymbol = "x"
    elif turnsymbol == "x":
        turnsymbol = "o"

def whichSquare(mousex, mousey):
    if mousey <= 200:
        if mousex <= 200:
            return tl
        elif mousex <= 400:
            return tm
        else:
            return tr
    elif mousey <= 400:
        if mousex <= 200:
            return ml
        elif mousex <= 400:
            return mm
        else:
            return mr
    else:
        if mousex <= 200:
            return bl
        elif mousex <= 400:
            return bm
        else:
            return br

while not done:
    #clock.tick(10)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True 
    #See where the mouse is
    mousey = pygame.mouse.get_pos()[1]
    mousex = pygame.mouse.get_pos()[0]
    #Clicking the mouse 
    if pygame.mouse.get_pressed()[0]:
        if holding == False:
            #now we gonna find what square we in
            currentSquare = whichSquare(mousex, mousey)
            for square in allSquares:
                if square == currentSquare and square[0] == False:
                    drawSymbol(screen, square[2], square[3])
                    square[0] = True
                    switchTurns()
            holding = True
    else:
        holding = False
    #Spacebar clears the whole game
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        screen.fill((0, 0, 0))
        for square in allSquares:
            square[0] = False
        turnsymbol = "x"

    #Draw boundary lines
    pygame.draw.line(screen, (255, 255, 255), (200, 0), (200, 600), 6)
    pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 600), 6)
    pygame.draw.line(screen, (255, 255, 255), (0, 200), (600, 200), 6)
    pygame.draw.line(screen, (255, 255, 255), (0, 400), (600, 400), 6)
    pygame.display.flip()
pygame.quit()