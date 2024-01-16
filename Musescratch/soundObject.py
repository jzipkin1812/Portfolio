import pygame
import numpy
import random

class SoundObject:
    def __init__(self, info, preloaded = False):
        self.sampleRate = 44100
        if(preloaded == True):
            self.snd = info
        else:
            self.frequency = info
            self.arr = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * self.frequency * x / self.sampleRate) for x in range(0, self.sampleRate)]).astype(numpy.int16)
            self.sndArr = numpy.c_[self.arr,self.arr]
            self.snd = pygame.sndarray.make_sound(self.sndArr)
    def play(self):
        # print(pygame.mixer.find_channel(True))
        pygame.mixer.find_channel(True).play(self.snd)
        # self.snd.play(-1)
    def stop(self):
        self.snd.stop()
        
        
