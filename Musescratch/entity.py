# Entities are visually displayed objects.
import pygame
import pitchCollections as pc
import soundObject as so
import constants as c
import random
import math
class Entity:
    def __init__(self, x = 0, y = 0, xv = 0, yv = 0, note = 0, color = (0, 0, 0)):
        self.x = x
        self.y = y
        self.speed = math.sqrt(xv ** 2 + yv ** 2)
        self.xv = xv
        self.yv = yv
        self.note = note
        self.size = 30
        self.color = color
    def initRandomSynthMajor(self, speed):
        self.size = 50
        self.speed = speed
        angle = random.uniform(0, 2 * math.pi)
        self.xv = math.cos(angle) * speed
        self.yv = math.sin(angle) * speed
        self.x = random.randint(0, c.SCREEN_WIDTH - self.size)
        self.y = random.randint(0, c.SCREEN_HEIGHT - self.size)
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.note = random.choice(pc.synthChromatic)
    def bounceMove(self, ticks = 1):
        self.x += self.xv * ticks
        self.y += self.yv * ticks
        if (self.y > c.SCREEN_HEIGHT - self.size):
            self.y = c.SCREEN_HEIGHT - self.size
            self.yv *= -1
            self.play()
        elif (self.y < self.size):
            self.y = self.size
            self.yv *= -1
            self.play()
        if (self.x > c.SCREEN_WIDTH - self.size):
            self.x = c.SCREEN_WIDTH - self.size
            self.xv *= -1
            self.play()
        elif (self.x < self.size):
            self.x = self.size
            self.xv *= -1
            self.play()
    def play(self):
        pygame.mixer.find_channel(True).play(self.note)
    def display(self, screen):
        pygame.draw.circle(screen, (self.color), (int(self.x), int(self.y)), self.size, 0)