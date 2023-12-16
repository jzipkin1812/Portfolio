import pygame
import os
import utility as u
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
#pygame.display.set_mode((1200, 750))
#images
path = os.getcwd() + "\\"
barStudioImage = pygame.image.load(path + "barStudio.jpg")
titleImage = u.resize(pygame.image.load(path + "title.jpg"), 0.58)
instructorImage = pygame.image.load(path + "instructors.png")
lanaImage = u.resize(pygame.image.load(path + "lana.png"), 0.5)
glitchBettyImage = u.resize(pygame.image.load(path + "glitchBetty.png"), 0.5)
gerriImage = u.resize(pygame.image.load(path + "gerri.png"), 0.4)
textBoxImage = pygame.image.load(path + "textBox.png")
theBarImage = pygame.image.load(path + "theBar.png")

upImage = u.resize(pygame.image.load(path + "up.png"), 0.15692)        
rightImage = u.resize(pygame.image.load(path + "right.png"), 0.15692)     
leftImage = u.resize(pygame.image.load(path + "left.png"), 0.15692)     
downImage = u.resize(pygame.image.load(path + "down.png"), 0.15692)     

barBallImage = pygame.image.load(path + "barBall.png")
cursorImage = pygame.image.load(path + "cursor.png")
perfectImage = u.resize(pygame.image.load(path + "perfect.png"), 0.6)
greatImage = u.resize(pygame.image.load(path + "great.png"), 0.6)
okImage = pygame.image.load(path + "ok.png")
missImage = u.resize(pygame.image.load(path + "miss.png"), 0.8)
scoreImage = u.resize(pygame.image.load(path + "score.png"), 0.9)
rankImage = u.resize(pygame.image.load(path + "rank.png"), 0.9)
possiblePointsImage = u.resize(pygame.image.load(path + "possiblePoints.png"), 0.9)
borderImage = pygame.image.load(path + "border.png")
sliderImage = u.resize(pygame.image.load(path + "slider.png"), 0.13)
#sound
house = pygame.mixer.Sound(path + "house.wav")
chill = pygame.mixer.Sound(path + "chill.wav")
danceTheNight = pygame.mixer.Sound(path + "danceTheNight.wav")
g6 = pygame.mixer.Sound(path + "g6.wav")
succession = pygame.mixer.Sound(path + "succession.wav")
#text files