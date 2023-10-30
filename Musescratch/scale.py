import pygame
import numpy
import soundObject
import frequencyRatios as fr

class Scale:
    def __init__(self, tonic, quality, octaves = 3):
        # STATIC frequency ratios

        self.degree = 1
        self.melodyIndex = 0
        self.melody = []
        self.recentDuration = 0
        self.tonicFrequency = tonic
        self.frequencies = []
        self.notes = []
        self.sharpFrequencies = []
        self.sharpNotes = []
        # Assemble the frequency array using any given array from pitchCollections with the INNER loop.
        # Additional octaves will also be added with the OUTER loop.
        for octave in range(1, octaves + 1):
            for ratio in quality:
                self.frequencies.append(ratio * tonic * octave)
                self.sharpFrequencies.append(ratio * tonic * octave * fr.m2)
        for f in self.frequencies:
            self.notes.append(soundObject.SoundObject(f))
        for sf in self.sharpFrequencies:
            self.sharpNotes.append(soundObject.SoundObject(sf))
    def stop(self):
        for note in self.notes:
            note.stop()
        for note in self.sharpNotes:
            note.stop()

    def playNote(self):
        self.stop()
        self.notes[self.degree - 1].play()
    
    def playMelodic(self):
        self.stop()
        self.recentDuration = 0    
        # If the scale degree denoted by the melody array is a .5 number, it has been sharpened.
        deg = self.melody[self.melodyIndex]
        if(deg == -1):
            pass
        elif(float(int(deg)) != float(deg)):
            self.sharpNotes[int(self.melody[self.melodyIndex] - 1)].play()
        else:
            self.notes[int(self.melody[self.melodyIndex] - 1)].play()
        
        self.melodyIndex += 1
        if(self.melodyIndex >= len(self.melody)):
            self.melodyIndex = 0
        
    def playChord(self, degreeArr):
        self.stop()
        for d in degreeArr:
            self.notes[d - 1].play()
    
    def increaseScaleDegree(self, scaleSize = 8):    
        self.recentDuration = 0    
        if (self.degree == scaleSize):
            self.degree = 1
        else:
            self.degree += 1
        