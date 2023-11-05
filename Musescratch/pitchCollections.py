import pygame
import numpy
import soundObject
import scale
import frequencyRatios as fr
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
#Melodies
above1        = [-1, -1, 8, 5, 6, 7, 6, 5, 8, 10, 9, 8, 9, 10, 12, 13, 11, 12, 5, 6.5, 7.5, 8, 8, -1]
cantusFirmus1 = [1, 3, 2, 3, 5, 6, 5, 4, 3, 2, 1, -1]                      