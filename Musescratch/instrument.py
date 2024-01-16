import soundObject as so
import pygame

class Instrument:
    def __init__(self, scaleType):
        self.insScale = []
        self.frames = 0
        if(scaleType == 1):
            insScale = so.synthChromatic
        elif(scaleType == 2):
            insScale = so.synthMajor
    def play(self, note):
        
        pygame.mixer.Channel(0).play(self.insScale[note])
    def playMelody(self, degreeSequence):
        self.frames += 1

