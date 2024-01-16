import pygame
import numpy
import pitchCollections as pc
import scale
import frequencyRatios as fr
import entity

class GameStateInfo:
    def __init__(self, screen):
        #Pygame varaibles
        self.frames = 0
        self.clock = pygame.time.Clock()
        self.tickTime = 0
        self.quit = False
        self.screen = screen
        #Variables that track which screen the player is on
        self.titleScreen = True
        self.inGame = False
        self.instructorScreen = False
        self.gameOver = False
        #Rhythm
        self.startTime = 0
        self.tickTime = 0
        #Pitch index for scales
        self.scaleDegree = 1
        self.mostRecentNoteDuration = 0.00
        #Entities
        self.entities = []
        for i in range(12):
            newE = entity.Entity()
            newE.initRandomSynthMajor(0.2)
            self.entities.append(newE)

    def updateFrames(self):
        self.frames += 1 
        self.clock.tick()
        ticks = self.clock.get_time()
        self.tickTime = ticks 
    
    def operateEntities(self):
        for e in self.entities:
            e.bounceMove(self.tickTime)
            e.display(self.screen)

    def playMelody(self, melody, scaleToPlay, speed = 1):
        scaleToPlay.melody = melody
        scaleToPlay.recentDuration += self.tickTime / 1000.00
        # Go to the next note
        if (scaleToPlay.recentDuration > speed):
            #ascendingScale.playChord([self.scaleDegree, self.scaleDegree + 2, self.scaleDegree + 4])
            scaleToPlay.playMelodic()        

    def scaleAscending(self, ascendingScale, speed = 1, scaleSize = 8):
        ascendingScale.recentDuration += self.tickTime / 1000.00
        # Go to the next note
        if (ascendingScale.recentDuration > speed):
            # print(ascendingScale.degree)
            #ascendingScale.playChord([self.scaleDegree, self.scaleDegree + 2, self.scaleDegree + 4])
            ascendingScale.playNote()
            ascendingScale.increaseScaleDegree(scaleSize)

    def ballScale(self):
        self.entities = []
        for i in range(0, 8, 1):
            self.entities.append(entity.Entity(30, 60 * (i + 1), 0.05 * (i + 1), 0, pc.synthMajor[i], \
                                               (200 - 20 * i, 10 * i + 10, 30 * i + 10)))
            print(i)


            