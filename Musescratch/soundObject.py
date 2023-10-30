import pygame
import numpy

class SoundObject:
    def __init__(self, f):
        self.sampleRate = 44100
        self.frequency = f
        self.arr = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * self.frequency * x / self.sampleRate) for x in range(0, self.sampleRate)]).astype(numpy.int16)
        self.sndArr = numpy.c_[self.arr,self.arr]
        self.snd = pygame.sndarray.make_sound(self.sndArr)
    def play(self):
        self.snd.play(-1)
    def stop(self):
        self.snd.stop()
        
        
