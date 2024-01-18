import pygame
import numpy
import pitchCollections as pc
import scale
import frequencyRatios as fr
import entity
import constants as c

class GameStateInfo:
    def __init__(self, screen):
        #Pygame varaibles
        self.frames = 0
        self.clock = pygame.time.Clock()
        self.tickTime = 0
        self.quit = False
        self.screen = screen
        #Variables that track which screen the player is on
        self.frameFunction = self.playScene
        #Variables that track game state based on input
        self.play = False
        #Rhythm
        self.startTime = 0
        self.tickTime = 0
        #Pitch index for scales
        self.scaleDegree = 1
        self.mostRecentNoteDuration = 0.00
        #Entities
        self.entities = []
        #Constants
        self.lineColor = (100, 200, 255)
    
    def loop(self):
        self.drawBackground()
        self.updateFrames()
        self.drawUI()
        #Call whatever function is determined by the current game state. Could be playing the entities, could not.
        self.frameFunction()
    #Once-per-frame function for the actual moving entities
    def playScene(self):
        self.operateEntities()
    def keyDown(self, key):
        if key == pygame.K_SPACE:
            self.play = not(self.play)

    def updateFrames(self):
        self.frames += 1 
        self.clock.tick()
        ticks = self.clock.get_time()
        self.tickTime = ticks 
    
    def operateEntities(self):
        for e in self.entities:
            e.display(self.screen)
            if self.play:
                e.bounceMove(self.tickTime)

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

    def ballMajorScale(self, size = 20):
        self.entities = []
        for i in range(0, 8, 1):
            self.entities.append(entity.Entity(size, c.UI_HEIGHT + 40 * (i + 1), 0.05 * (i + 1), 0, pc.synthMajor[i], \
                                               (200 - 20 * i, 10 * i + 10, 30 * i + 10), size))
    def ballChromaticScale(self, size = 20):
        self.entities = []
        for i in range(0, 12, 1):
            self.entities.append(entity.Entity(size, c.UI_HEIGHT + 40 * (i + 1), 0.03 * (i + 1), 0, pc.synthChromatic[i], \
                                               (10 * i + 10, 200 - 15 * i, 20 * i + 10), size))
    
    def screenText(self, x, y, text = "Default", size = 70, color = [200, 200, 200], background = None):
        tempFont = pygame.font.SysFont(None, size)
        tempText = tempFont.render(text, True, color, background)
        self.screen.blit(tempText, (x, y))

    def drawUI(self):
        # Play button
        self.screenText(20, 20, "PLAY", 70, (100, 100, 200))
        # Play button
        self.screenText(200, 20, "OBJECTS", 70, (100, 100, 200))
        # Play button
        self.screenText(500, 20, "TRIGGERS", 70, (100, 100, 200))
        # Horizontal UI Bar
        pygame.draw.line(self.screen, self.lineColor, (0, c.UI_HEIGHT), (c.SCREEN_WIDTH, c.UI_HEIGHT), 3)
        #Vertical UI Bars
        pygame.draw.line(self.screen, self.lineColor, (180, 0), (180, c.UI_HEIGHT), 3)
        pygame.draw.line(self.screen, self.lineColor, (450, 0), (450, c.UI_HEIGHT), 3)


    def drawBackground(self):
        self.screen.fill((20, 20, 60))