import pygame
import random
pygame.init()
clock = pygame.time.Clock()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])
done = False
holding = False
balls = []
while not done:
    clock.tick(60)
    screen.fill((250, 250, 250))
    mousey = pygame.mouse.get_pos()[1]
    mousex = pygame.mouse.get_pos()[0]
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True 

    #If you click the mouse, spawn a ball
    if pygame.mouse.get_pressed()[0]:
        if holding == False or holding == True:
            holding = True
            #x position, y position, velocity (negative = down positive = up), color, radius, xvelocity
            balls.append([mousex, mousey, 0, [random.randint(100, 250), random.randint(100, 250), random.randint(100, 250)], 20, 5])
    else:
        holding = False

    #calculate ball velocity
    for ball in balls:
        #If the ball plus its velocity wouldn't make it go onto the floor, make it go down
        if ball[1] + ball[2] + ball[4] < 500:
            ball[2] += 1
        #Otherwise make it bounce up and make it lose some energy
        else:
            ball[2] = ball[2] * -0.9
            #x velocity for random fun
            ball[5] *= -1
    #Apply gravity and momentum to all the balls based on their velocity
    for ball in balls:
        ball[1] += ball[2]
        #make them move to the right or left
        #if ball[2] != 0:
        	#ball[0] += ball[5]
    #draw all the balls
    for ball in balls:
        pygame.draw.circle(screen, (ball[3]), (int(ball[0]), int(ball[1])), ball[4], 0)
    #clear the screen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        balls = []
    pygame.display.flip()
pygame.quit()
