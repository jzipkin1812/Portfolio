import pygame
pygame.init()
color1 = input("Color 1: ")
color2 = input("Color 2: ")
rgb = [0, 0, 0]
clock = pygame.time.Clock()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])
done = False

def omax(x):
	return(max(x, 0))
while not done:
	clock.tick(10)
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			done = True 
	for i in range(255):
		
		if "red" in color1:
			rgb[0] = omax(255 - i)
		if "blue" in color1:
			rgb[2] = omax(255 - i)
		if "green" in color1:
			rgb[1] = omax(255 - i)

		if "red" in color2:
			rgb[0] = omax(i)
		if "blue" in color2:
			rgb[2] = omax(i)
		if "green" in color2:
			rgb[1] = omax(i)
		
		if "red" in color1 and "red" in color2:
			rgb[0] = 255
		if "blue" in color1 and "blue" in color2:
			rgb[2] = 255
		if "green" in color1 and "green" in color2:
			rgb[1] = 255

		pygame.draw.line(screen, (rgb), (0, i * 2), (500, i * 2), 2)
	pygame.display.flip()
pygame.quit()
