import pygame
import numpy
import pysine
import gameStateInfo as gs
import frequencyRatios as fr
import soundObject 
import pitchCollections
import constants as c
pygame.init()

# Pygame trackers

screen = pygame.display.set_mode([c.SCREEN_WIDTH, c.SCREEN_HEIGHT])
done = False
pygame.mixer.set_num_channels(12)

# Game state info
mainStatus = gs.GameStateInfo(screen)
mainStatus.ballChromaticScale()
print(pygame.mixer.get_num_channels())
while not done:

    mainStatus.loop()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            mainStatus.keyDown(event.key)
    # mainStatus.scaleAscending(pitchCollections.cNaturalMinor, 1, 8)
    # mainStatus.scaleAscending(pitchCollections.cCounterpoint, 1, 8)
    # mainStatus.playMelody(pitchCollections.cantusFirmus1, pitchCollections.a3Minor, 1.5)
    # mainStatus.playMelody(pitchCollections.above1, pitchCollections.a3Minor2, 0.75)
    # mainStatus.scaleAscending(pitchCollections.synthMajorScale, 0.4, 8)
    pygame.display.flip()
pygame.quit()