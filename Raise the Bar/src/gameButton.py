import pygame
import assets as a
import utility as u
class GameButton:
    def __init__(self, x, y, width, height, image, function, screen, cooldown = 0):
        self.image = image
        self.visible = True
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.function = function
        self.screen = screen
        self.cooldown = 0
        self.maxCoolDown = cooldown
    def isClicked(self, mouseX, mouseY):
        return((self.x <= mouseX <= self.x + self.width) and (self.y <= mouseY <= self.y + self.height))
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        if(self.cooldown > 0):
            bar = pygame.Surface((self.width * (self.cooldown / self.maxCoolDown), self.height))  
            bar.set_alpha(128)              
            bar.fill((50, 50, 50))           
            self.screen.blit(bar, (self.x,self.y)) 
            self.cooldown -= 1
    def press(self, statusObj):
        if(self.cooldown == 0):
            self.function(statusObj)
            self.cooldown = self.maxCoolDown
    def getPosition(self):
        return (self.x, self.y)