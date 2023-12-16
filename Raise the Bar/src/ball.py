import pygame
import random
import math
import assets as a
import utility as u

class Ball:
    def __init__(self, screen, speed = 0.4, radius = 110):
        self.screen = screen
        self.x = 0.0
        self.y = random.randint(200, 500)
        self.bounces = 5
        #Ball image default size is 359x359
        self.radius = radius
        self.image = pygame.transform.scale(a.barBallImage, (radius, radius))
        #The speed can be whatever it wants to be.
        #We multiply the speed by the number of milliseconds passed. A medium speed would be roughly 0.4.
        self.speed = speed
        angle = random.uniform(math.pi / 2, -1 * math.pi / 2)
        self.xv = math.cos(angle) * self.speed
        self.yv = math.sin(angle) * self.speed


    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
    def move(self, tickTime):
        #Move at any angle with deference to framerate changes
        self.x += self.xv * tickTime
        self.y += self.yv * tickTime
        #Bounce on the borders of the screen
        if self.bounces > 0 and (self.x > 1200 - self.radius or self.x < 0):
            self.xv *= -1
            self.x = max(0, min(1200 - self.radius, self.x))
            self.bounces -= 1
        if self.bounces > 0 and (self.y > 750 - self.radius or self.y < 0):
            self.yv *= -1
            self.y = max(0, min(750 - self.radius, self.y))
            self.bounces -= 1
    def centerX(self):
        return(self.x + self.radius / 2)
    def centerY(self):
        return(self.y + self.radius / 2)