import pygame
import numpy
import soundObject
import scale
import frequencyRatios as fr
import os
pygame.mixer.init(44100, -16, 2, 512)

# Ratios for different qualities of scales

# Creating some static Sound objects
# cMajor = scale.Scale(261, fr.major, 3)
# cChromatic = scale.Scale(261, fr.chromatic, 2)
# cNaturalMinor = scale.Scale(261, fr.naturalMinor, 3)
# cHarmonicMinor = scale.Scale(261, fr.harmonicMinor, 3)
# cCounterpoint = scale.Scale(261, fr.counterpoint, 3)
# cSeconds = scale.Scale(261, fr.seconds, 2)
# a4Minor = scale.Scale(440, fr.naturalMinor, 4)
a3Minor = scale.Scale(220, fr.naturalMinor, 4)
a3Minor2 = scale.Scale(220, fr.naturalMinor, 4)
# a3Major = scale.Scale(220, fr.major, 4)
# a3Major2 = scale.Scale(220, fr.major, 4)
# WAV files loaded
path = os.getcwd() + "\\assets\\"
c3 = pygame.mixer.Sound(path + "c3.wav")
cs3 = pygame.mixer.Sound(path + "cs3.wav")

d3 = pygame.mixer.Sound(path + "d3.wav")
ds3 = pygame.mixer.Sound(path + "ds3.wav")

e3 = pygame.mixer.Sound(path + "e3.wav")

f3 = pygame.mixer.Sound(path + "f3.wav")
fs3 = pygame.mixer.Sound(path + "fs3.wav")

g3 = pygame.mixer.Sound(path + "g3.wav")
gs3 = pygame.mixer.Sound(path + "gs3.wav")

a3 = pygame.mixer.Sound(path + "a3.wav")
as3 = pygame.mixer.Sound(path + "as3.wav")

b3 = pygame.mixer.Sound(path + "b3.wav")
c4 = pygame.mixer.Sound(path + "c4.wav")

synthChromatic = [c3, cs3, d3, ds3, e3, f3, fs3, g3, gs3, a3, as3, b3, c4]
synthMajor = [c3, d3, e3, f3, g3, a3, b3, c4]
synthMajorScale = scale.Scale(0, 0, 0, synthMajor, False)
# Melodies
above1        = [-1, -1, 8, 5, 6, 7, 6, 5, 8, 10, 9, 8, 9, 10, 12, 13, 11, 12, 5, 6.5, 7.5, 8, 8, -1]
cantusFirmus1 = [1, 3, 2, 3, 5, 6, 5, 4, 3, 2, 1, -1]                      