import pygame
import random
import assets as a
import utility as u
import button as b
import level as l
import ball
  

class GameStateInfo:
    def __init__(self, screen):
        #Pygame varaibles
        self.frames = 0
        self.quit = False
        self.screen = screen
        #Variables that track which screen the player is on
        self.titleScreen = True
        self.inGame = False
        self.instructorScreen = False
        self.gameOver = False
        #The current level the player is playing
        self.level = l.Lana()
        self.borderX = 88
        self.borderY = 195
        #The current background to be displayed and other images
        self.currentBackground = a.barStudioImage
        self.instructorProfile = self.level.instructorImage
        #Stage counter (each two lines of dialogue represents a stage)
        self.stage = -1
        #Text
        self.textCover = 980 * 2
        self.textSpeed = 13
        self.textFile = open(self.level.dialogueFile, "r")
        
        #Rhythm
        self.startTime = 0
        self.stackFile = open(self.level.stackFile, "r")
        self.stackLine = ""
        self.stackStage = 0
        self.trackStarted = False
        self.tickTime = 0
        #Game entities
        self.buttons = []
        self.balls = []
        self.sliders = [False, False, False, False]
        #Score
        self.score = 0
        self.possiblePoints = 0
        self.recentPointTotal = -1
        self.showPossible = False
        self.showRank = False
        #for Gerri stage awful beat counter for awful things
        self.beat = 0
        #start the text
        self.incrementText()


    def reset(self, newLevel):
        #Level-specific resets
        self.level = newLevel
        self.instructorProfile = self.level.instructorImage
        self.textFile = open(self.level.dialogueFile, "r")
        self.stackFile = open(self.level.stackFile, "r")
        #Non-level-specific resets
        self.frames = 0
        self.stage = -1
        self.incrementText()
        self.startTime = 0
        self.stackStage = 0
        self.trackStarted = False
        self.gameOver = False
        self.tickTime = 0
        self.buttons = []
        self.balls = []
        self.score = 0
        self.possiblePoints = 0
        self.recentPointTotal = -1
        self.showPossible = False
        self.showRank = False

    def updateFrames(self):
        self.frames += 1 
        if self.textCover > 0:
            self.textCover = max(0, self.textCover - self.textSpeed)     

    def displayBackground(self):
        if self.inGame:
            #background images
            self.screen.blit(a.barStudioImage, (0, 0))
            self.showInstructor()
            self.screen.blit(a.textBoxImage, (170, 600))
            self.screen.blit(a.scoreImage, (170, 70))
            #The current score
            u.screenText(460, 87, self.screen, str(self.score), 80, (255, 255, 191))
            #everything for instructor dialogue
            u.screenText(180, 610, self.screen, self.line1, 30)
            u.screenText(180, 660, self.screen, self.line2, 30)
                #black boxes for text obfuscation
            midLineY = 660
            rightX = 1161
            if self.textCover > 980:
                u.betterRect((0, 0, 0), rightX - self.textCover + 980, 610, rightX, midLineY, self.screen)
                u.betterRect((0, 0, 0), rightX - 980, midLineY, rightX, 734, self.screen)
            else:
                u.betterRect((0, 0, 0), rightX - self.textCover, midLineY, rightX, 734, self.screen)
            if (self.stage >= 13 or self.level.introLength != 21) and self.gameOver == False:
                self.screen.blit(a.theBarImage, (170, 175))
            #THE BAR! THE ARROWS!
            if self.trackStarted:
                
                i = 0
                while i < len(self.buttons):
                    #print(i)
                    stack = self.buttons[i]
                    for arrow in stack:
                        arrow.display()
                        # Also, move arrows to the right
                        arrow.move(self.tickTime) 
                        # ALso, do sliders.
                        self.operateSliders(arrow)
                    # Also, delete any arrows that have gone too far.
                    if stack[0].x > 1100:
                        del self.buttons[0]
                        i -= 1  
                        self.recentPointTotal = 0
                        #print("Now:", i)   
                    i += 1
                #Bar balls
                for ball in self.balls:
                    ball.display()
                    ball.move(self.tickTime)
                #Sliders
                self.drawSliders()
                #Score indicator text like "Perfect!" Or "Miss"
                self.displayScoreMessage()
            #Game Over Stuff
            if self.showPossible:
                self.screen.blit(a.possiblePointsImage, (170, 200))
                u.screenText(810, 217, self.screen, str(self.possiblePoints), 80, (255, 255, 191))
            if self.showRank:
                self.screen.blit(a.rankImage, (170, 330))
                ratio = self.score / self.possiblePoints
                index = int(ratio * 10) + 2 #Rank is from 2-12
                ranks = ["Index 0", "Index 1", "Did You Even Try?", "Meh...", 
                "Beginner", "Apprentice", "Bar Babe", "Bar Bitch", 
                "Bar Boss", "Instructor", "Winterbottom Warrior", 
                "Bar Grandmaster", "PERFECTION!", "IMPOSSIBLY AMAZING!", "WHAAAAAAAT?", "STOPPIT!"]
                print(len(ranks))
                u.screenText(400, 347, self.screen, ranks[index], 75, (255, 255, 191))
                    

                        
                            
        elif self.instructorScreen:
            self.screen.blit(a.instructorImage, (0, 0))
            self.screen.blit(a.borderImage, (self.borderX, self.borderY))
        elif self.titleScreen:
            self.screen.blit(a.titleImage, (0, -63))

    def displayScoreMessage(self):
        if self.recentPointTotal < 0:
            return
        elif self.recentPointTotal == 50:
            #a.perfectImage.set_alpha(50)
            self.screen.blit(a.perfectImage, (880, 85))
            #print(a.perfectImage.get_alpha())
        elif self.recentPointTotal > 25:
            self.screen.blit(a.greatImage, (892, 85))
        elif self.recentPointTotal > 0:
            self.screen.blit(a.okImage, (937, 85))
        else:
            self.screen.blit(a.missImage, (915, 85))

    def setButtons(self, buttons = []):
        self.buttons = buttons

    def incrementScreen(self):
        if self.titleScreen:
            self.titleScreen = False
            self.instructorScreen = True
        elif self.instructorScreen:
            self.instructorScreen = False
            self.inGame = True
            pygame.mixer.Channel(0).play(a.house)
        else:
            if self.trackStarted == False:
                self.incrementText()
                

    def incrementText(self):
        if self.showRank == True:
            self.showRank = False
            self.textFile.close()
            self.stackFile.close()
            self.reset(l.Lana())
            self.titleScreen = True
            self.inGame = False
            self.gameOver = False
            self.instructorScreen = False  
            pygame.mixer.Channel(0).stop()
            return   
        self.line1 = self.textFile.readline()
        self.line1 = self.line1[:len(self.line1) - 1]
        self.line2 = self.textFile.readline()
        self.line2 = self.line2[:len(self.line2) - 1]
        self.textCover = 1960
        self.stage += 2
        if self.stage == self.level.introLength:
            self.startTrack(1)
        if "Here's the possible points" in self.line1:
            self.showPossible = True
        if "Here's your final rank" in self.line1:
            self.showRank = True

    def startTrack(self, trackNum):
        self.startTime = pygame.time.get_ticks()
        self.trackStarted = True
        #Dance the Night: 1 beat = 480 Milliseconds
        pygame.mixer.Channel(0).play(self.level.music)
        pygame.time.set_timer(10, self.level.bpm)

    def checkStack(self):
        #Process text
        self.stackLine = self.stackFile.readline()
        self.stackLine = self.stackLine[:len(self.stackLine) - 1]
        print(self.stackLine)
        #Spawn Objects
        currentStack = []
        if "d" in self.stackLine:
            currentStack.append(b.down(self.screen, self.level.arrowSpeed))
            self.possiblePoints += 50
        if "u" in self.stackLine:
            currentStack.append(b.up(self.screen, self.level.arrowSpeed))
            self.possiblePoints += 50
        if "l" in self.stackLine:
            currentStack.append(b.left(self.screen, self.level.arrowSpeed))
            self.possiblePoints += 50
        if "r" in self.stackLine:
            currentStack.append(b.right(self.screen, self.level.arrowSpeed))
            self.possiblePoints += 50
        #Ball objects
        if "b" in self.stackLine:
            self.balls.append(ball.Ball(self.screen, 0.5))
            self.possiblePoints += 100
        #Slider objects
        if "s-D" in self.stackLine:
            self.sliders[3] = not self.sliders[3]
        if "s-U" in self.stackLine:
            self.sliders[0] = not self.sliders[0]
        if "s-R" in self.stackLine:
            self.sliders[1] = not self.sliders[1]
        if "s-L" in self.stackLine:
            self.sliders[2] = not self.sliders[2]
        #Speedup and slowdown
        if "ARROWSPEEDSLOWER" in self.stackLine:
            self.level.arrowSpeed /= 2
        elif "ARROWSPEEDFASTER" in self.stackLine:
            self.level.arrowSpeed *= 2
        #Append the entire list of spawned objects to the self.buttons list
        if len(currentStack) > 0:
            self.buttons.append(currentStack)
        #Advance Text
        if "t" in self.stackLine and self.trackStarted:
            self.incrementText()
        #End the song
        if "END" in self.stackLine:
            self.trackStarted = False
            self.gameOver = True
            pygame.mixer.Channel(0).play(a.chill)
        #For uneven-millisecond tracks, change the BPM every other time to get a BPM of 0.5.
        if self.level.bpm == 440: 
            self.level.bpm = 439
            pygame.time.set_timer(10, self.level.bpm)
        elif self.level.bpm == 439 and not(19 <= self.stage <= 22):
            self.level.bpm = 440
            pygame.time.set_timer(10, self.level.bpm)
            #print("Changed back to 440!")
        elif self.level.bpm == 421: 
            self.level.bpm = 420
            self.beat = 0
            pygame.time.set_timer(10, self.level.bpm)
        elif self.level.bpm == 420:
            if self.beat == 1:
                self.level.bpm = 421
                pygame.time.set_timer(10, self.level.bpm)
            else:
                self.beat = 1
            
            #print("Changed back to 440!")
    
    def clear(self, key):
        #Clearing only works on the oldest stack in the bunch.
        stack = self.buttons[0]
        i = 0
        while i < len(stack):
            #The perfect x value for clearing a button is 962.
            #print(abs(stack[i].x - 962))
            if(key == stack[i].key):
                self.recentPointTotal = int(min(50, max(0, 65 - abs(stack[i].x - 962))))
                self.score += self.recentPointTotal
                del stack[i]
                i -= 1
            i += 1
        if len(stack) == 0:
            del self.buttons[0]

    def clearClick(self, mouseX, mouseY):
        #Bar balls
        i = 0
        while i < len(self.balls):
            if u.distanceFormula(mouseX, mouseY, self.balls[i].centerX(), self.balls[i].centerY()) <= self.balls[i].radius:
                self.score += 50 + 10 * self.balls[i].bounces
                del self.balls[i]
                i -= 1
            i += 1
    
    def showInstructor(self):
        if self.level.introLength == 21:
            self.screen.blit(self.instructorProfile, (10, 470))
        elif self.level.introLength == 23:
            self.screen.blit(self.instructorProfile, (-50, 470))
        else:
            self.screen.blit(self.instructorProfile, (-90, 470))

    def drawSliders(self):
        i = 0
        for i in range(4):
            if self.sliders[i]:
                self.screen.blit(a.sliderImage, (550, 175 + 100 * i))
    def operateSliders(self, arrow):
        if (600 > int(arrow.x) > 554) and ((arrow.type == "down" and self.sliders[3]) or (arrow.type == "left" and self.sliders[2]) or (arrow.type == "right" and self.sliders[1]) or (arrow.type == "up" and self.sliders[0])):
            arrow.swap()
