import pygame
pygame.init()

def betterRect(color, x1, y1, x2, y2, width = 0):
	pygame.draw.polygon(screen, (color), ([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]), width)

#gws = Gradient White Squares
#gls = Gradient White Lines
def gws(reversed = False):
	for i in range(500, 0, -25):
		if reversed:
			cnum = (i // 2)
		else:
			cnum = 250 - (i // 2)
		betterRect((cnum, cnum, cnum), 0, 0, i, i)
def gwsCentered(reversed = False):
	for i in range(250, 0, -25):
		if reversed:
			cnum = i
		else:
			cnum = 250 - i
		betterRect((cnum, cnum, cnum), 250 - i, 250 - i, 250 + i, 250 + i)
def gwsDiagonal(reversed = False):
	for i in range(500, 0, -25):
		if reversed:
			cnum = i // 2
		else:
			cnum = 250 - (i // 2)
		pygame.draw.polygon(screen, (cnum, cnum, cnum), ([(0, 0), (0, i * 2), (i * 2, 0)]))

clock = pygame.time.Clock()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])
done = False

while not done:
	clock.tick(10)
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			done = True 
	gwsDiagonal()
	pygame.display.flip()
pygame.quit()