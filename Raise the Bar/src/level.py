import pygame
import random
import assets as a
import utility as u
import button as b
import ball
  

class level:
    def __init__(self, instructorImage, bpm, arrowSpeed, introLength, music, dialogueFile, stackFile):
        #Pygame varaibles
        #Borders: 104 211, 492 214, 878 215
        #self.instructorBorderLocation = 
        self.instructorImage = instructorImage
        self.bpm = bpm
        self.introLength = introLength
        self.music = music
        self.stackFile = stackFile
        self.dialogueFile = dialogueFile
        self.arrowSpeed = arrowSpeed

def Lana():
	return level(a.lanaImage, 480, 0.4125, 21, a.danceTheNight, "lana.txt", "lanaStacks.txt")
def Betty():
	return level(a.glitchBettyImage, 440, 0.4459, 13, a.g6, "betty.txt", "bettyStacks.txt")
def Gerri():
	return level(a.gerriImage, 421, 0.4637, 23, a.succession, "gerri.txt", "gerriStacks.txt")