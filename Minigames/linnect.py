import pygame, math
def betterRect(color, x1, y1, x2, y2, width = 0):
    pygame.draw.polygon(screen, (color), ([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]), width)
def distanceFormula(x1, y1, x2, y2):
    return(int(math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )))

class nail:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return(self.x == other.x and self.y == other.y)
        
pygame.init()
clock = pygame.time.Clock()
screen_width = 1200
screen_height = 675
screen = pygame.display.set_mode([screen_width,screen_height])
done = False
holdingleft = False
holdingright = False
permalines = []
all_ns = []
current_n = nail(-1, -1)
frames = 0
while not done:
    clock.tick(60)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True 
    #Clear screen
    screen.fill((0, 0, 0))

    #Frames
    frames += 1
    #Get mouse positions
    mousey = pygame.mouse.get_pos()[1]
    mousex = pygame.mouse.get_pos()[0]

    #Draw stuff from lists
    for line in permalines:
        pygame.draw.line(screen, (0, 200, 50), (line[0], line[1]), (line[2], line[3]), 3)
    for selected_n in all_ns:
        if selected_n == current_n:
            pygame.draw.circle(screen, (200, 200, 200), (selected_n.x, selected_n.y), 8)
        else:
            pygame.draw.circle(screen, (0, 200, 200), (selected_n.x, selected_n.y), 8)
    #Left mouse
    if pygame.mouse.get_pressed()[0]:    
        #make lines between all_ns
        if not holdingleft:
            for selected_n in all_ns:
                #if ur clicking on the selected_n and there's no duplicates or overlapping make a new line
                if (distanceFormula(mousex, mousey, selected_n.x, selected_n.y) < 8): 
                    #make a new line here as long as the program didn't just start
                    if (current_n != selected_n and current_n != nail(-1, -1)) and ([current_n.x, current_n.y, selected_n.x, selected_n.y] not in permalines) and ([selected_n.x, selected_n.y, current_n.x, current_n.y] not in permalines):                       
                        permalines.append([current_n.x, current_n.y, selected_n.x, selected_n.y])       
                        print(len(permalines))                             
                    #but the only condition for switching selection to a new selected_n is the clicking part
                    current_n = nail(selected_n.x, selected_n.y)
            
        holdingleft = True
    else:
        holdingleft = False 

    #Right mouse
    if pygame.mouse.get_pressed()[2]:
        if not holdingright:
            all_ns.append(nail(mousex, mousey))
        holdingright = True
    else:
        holdingright = False
    pygame.display.flip()
pygame.quit()