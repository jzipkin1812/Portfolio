import pygame
import numpy
import pysine
import gameStateInfo as gs
import frequencyRatios as fr
import soundObject 
import pitchCollections
pygame.init()

# Pygame trackers
screen_width = 750
screen_height = 750
screen = pygame.display.set_mode([screen_width,screen_height])
done = False

# Game state info
mainStatus = gs.GameStateInfo(screen)

while not done:
    mainStatus.updateFrames()
    

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_Q:
                 

    
    #ur drawings uwu
    # mainStatus.scaleAscending(pitchCollections.cNaturalMinor, 1, 8)
    # mainStatus.scaleAscending(pitchCollections.cCounterpoint, 1, 8)
    mainStatus.playMelody(pitchCollections.cantusFirmus1, pitchCollections.a3Minor, 1.5)
    mainStatus.playMelody(pitchCollections.above1, pitchCollections.a3Minor2, 0.75)

    
    pygame.display.flip()

pygame.quit()