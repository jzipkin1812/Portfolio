import pygame
import random
import assets as a
import utility as u

class Button:
    def __init__(self, screen, type, image, key, y, speed = 0.4125):
        #Pygame varaibles
        self.screen = screen
        self.type = type
        self.image = image
        self.key = key
        self.x = 170.0
        self.y = y
        self.swapped = False
        #The speed depends on the beat of the song.
        #The arrows must move 792 pixels in exactly some number of beats, which is some number of milliseconds.
        #For Dance the Night, 792 pixels / 4 beats = 792 pixels / (480 * 4) milliseconds = 0.4125 pixels per millisecond.
        #Therefore, we multiply 0.4125 by the number of milliseconds passed.
        self.speed = speed
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
    def move(self, tickTime):
        self.x += self.speed * tickTime
    def swap(self):
        #Arrows may only be swapped once.
        if self.swapped == True:
            return
        if self.type == "down":
            self.type = "up"
            self.key = pygame.K_UP
            self.image = a.upImage
        elif self.type == "up":
            self.type = "down"
            self.key = pygame.K_DOWN
            self.image = a.downImage    
        elif self.type == "left":
            self.type = "right"
            self.key = pygame.K_RIGHT
            self.image = a.rightImage
        elif self.type == "right":
            self.type = "left"
            self.key = pygame.K_LEFT
            self.image = a.leftImage
        else:
            return
        self.swapped = True
    
def down(screen, speed = 0.4125):
    return(Button(screen, "down", a.downImage, pygame.K_DOWN, 475, speed))
def up(screen, speed = 0.4125):
    return(Button(screen, "up", a.upImage, pygame.K_UP, 177, speed))
def left(screen, speed = 0.4125):
    return(Button(screen, "left", a.leftImage, pygame.K_LEFT, 375, speed))
def right(screen, speed = 0.4125):
    return(Button(screen, "right", a.rightImage, pygame.K_RIGHT, 275, speed))