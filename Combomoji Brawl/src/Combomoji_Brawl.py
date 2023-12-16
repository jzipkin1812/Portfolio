# Happy birthday Ruya! This is the code for the game I made for you.
# I hope you play it with your family and friends and have a lot of fun.
# Make sure to try out all the characters and see who comes out on top.
# To run the game, look up ^^^ and click Run and then click Run Module!
# Do not edit any of the code or the game may break.
# JAVIN
# ZIPKiN
# DO NOT STEAL GAME
import pygame, math, random, os
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

class Player:
    def __init__(self, character = "clonkey", x = 0, y = 0, size = 150, playerNumber = 1):
        self.character = character
        self.x = x
        self.y = y
        self.yv = 0
        self.xv = 0
        self.playerNumber = playerNumber
        self.grounded = False
        self.holdingUp = False
        self.holdingAbility1 = False
        self.holdingAbility2 = False
        self.size = size
        self.hp = 700
        self.mana = 400
        self.manaRecoveryTimer = 20
        #counter for ghonkey's attack ability, timer for doubleHunny's embiggen ability,
        #tracker for demonkey's pentagram animation, and tracker for bronkey's animations
        self.counter = 0
        self.transparency = 255
        #for xdirection, 1 is used as the "right" indicator and -1 for "left" because they easily translate
        #into momentum multipliers. Same for ydirection, where 0 and 1 are used instead.
        self.xdirection = 1
        self.ydirection = "stop"
        self.projectiles = []
        #frozen counter is for freekey's stun abilities
        self.frozen = 0
        #stun for bronkey uppercut
        self.stun = 0
        #stun counter is for 
        #dictionary that assigns characters to their image
        charactersDict = {
        "clonkey" : clonkeyImage,
        "onekey" : onekeyImage,
        "dizzykiss" : dizzyKiss,
        "ghonkey" : ghonkey,
        "doubleHunny" : doubleHunny,
        "freekey" : freekey,
        "demonkey" : demonkey,
        "bronkey" : bronkey,
        }

        self.image = charactersDict[self.character]

        if playerNumber == 1:
            self.keyDict = {
            "jump" : pygame.K_w,
            "right" : pygame.K_d,
            "left" : pygame.K_a,
            "ability1" : pygame.K_LSHIFT,
            "ability2" : pygame.K_SPACE,
            }
        elif playerNumber == 2:
            self.keyDict = {
            "jump" : pygame.K_UP,
            "right" : pygame.K_RIGHT,
            "left" : pygame.K_LEFT,
            "ability1" : pygame.K_COMMA,
            "ability2" : pygame.K_PERIOD,
            }

        #angle and projectiles for doubleHunny's orbit passive
        if self.character == "doubleHunny":
            self.orbitAngle = 0
            for i in range(2):
                self.projectiles.append(Projectile(self.x, self.y, 50, 50, redLaugh, 0, 0, 2, "pierce"))

    def display(self):
        screen.blit(pygame.transform.scale(self.image, (self.size, self.size)), (int(self.x), int(self.y)))
    def clearProjectiles(self):
        #clear projectiles if they are completely off the screen
        for proj in self.projectiles:
            if ((proj.x > 1600 or proj.x < -300 or proj.y > 930 or (proj.y < -200 and not proj.lobbed))) and not(self.character == "doubleHunny"):
                self.projectiles.remove(proj)
    def operateMovement(self):
        keys = pygame.key.get_pressed()
        #up key for jump
        if keys[self.keyDict["jump"]]: 
            if self.grounded:
                self.yv -= 20
            self.holdingUp = True
            self.ydirection = 1
        else:
            self.holdingUp = False
            self.ydirection = 0
        #left key
        if keys[self.keyDict["left"]] and self.stun == 0:
            self.xdirection = -1
            self.x -= 8
            if self.character == "bronkey":
                self.x -= 2
        #right key
        elif keys[self.keyDict["right"]] and self.stun == 0:
            self.xdirection = 1
            self.x += 8
            if self.character == "bronkey":
                self.x += 2
        #enforce gravity
        self.yv = min(40, self.yv + 0.8)
        #enforce friction
        if self.xv > 0:
            self.xv = max(0, self.xv - 0.5)
        elif self.xv < 0:
            self.xv = min(0, self.xv + 0.5)
        #enforce movement based on velocity
        self.x += self.xv
        self.y += self.yv
        #enforce falling off the map
        if self.y > 730 + self.size:
            if currentMap == trishaFloorMap:
                punishment = 150
            else:
                punishment = 300
            self.hp = max(0, self.hp - punishment) 
            self.y = -1 * self.size
            self.yv = 0
        #enforce wrapping around the map
        if self.x < -1 * self.size:
            self.x = 1300
        elif self.x > 1300:
            self.x = -1 * self.size
        #if ur doing abilities don't regenerate mana!
        if self.manaRecoveryTimer > 0:
            self.manaRecoveryTimer -= 1
        #separately, regenerate mana in this function for some reason
        else:
            self.mana = min(self.mana + 3, 400)
    def clonkeyAbilities(self):
        #banana: 82 by 123
        #x, y, width, height, image, xv = 0, yv = 0, damage = 0, tag = "none", lobbed = False, boomerang = 0
        keys = pygame.key.get_pressed()
        #BANANA TOSS: toss a banana peel at the enemy, directional aiming + higher aim while holding up
        if keys[self.keyDict["ability1"]]: 
            if (not self.holdingAbility1) and (self.mana > 160):
                self.projectiles.append(Projectile(self.x + self.size / 3, self.y, 82, 123, bananaPeel, (10 - self.ydirection * 5) * self.xdirection, -20 + (-10 * self.ydirection), 50 + (50 * self.ydirection), "bananaPeel", True, 0))
                self.mana -= 160
                self.manaRecoveryTimer = 20
            self.holdingAbility1 = True
        else:
            self.holdingAbility1 = False   
        #SILLY SLIDE: Dash forward and get a small bounce!
        if keys[self.keyDict["ability2"]]: 
            if (not self.holdingAbility2) and (self.mana > 160):
                self.mana -= 160
                #the dash (and a lil bounce)
                self.xv = 15 *self.xdirection
                self.yv -= 10
                self.manaRecoveryTimer = 20
                #sound effect whoosh
                pygame.mixer.Channel(self.playerNumber + 3).play(pygame.mixer.Sound(path + 'whoosh.wav'))
            self.holdingAbility2 = True
        else:
            self.holdingAbility2 = False   
    def onekeyAbiilties(self):
        #laser: infinity by 75
        keys = pygame.key.get_pressed()
        #LASER EYE: shoot a giant laser right or left
        #clear all lasers so that only 1 is active
        for proj in self.projectiles:
            if proj.tag != "lightning":
                self.projectiles.remove(proj)

        if keys[self.keyDict["ability1"]]:
            #drain mana and shoot the laser
            if self.mana > 4:
                self.mana -= 4
                self.manaRecoveryTimer = 20
                if self.xdirection == 1:
                    screen.blit(laserTriangle, (self.x + self.size / 2, self.y + self.size / 2 - 56))
                    self.projectiles.append(Projectile(min((self.x + self.size / 2 + 37), 1300), self.y + self.size / 2 - 56, 1310, 75, laserBeam, 0, 0, 1.5))
                elif self.xdirection == -1:
                    screen.blit(pygame.transform.flip(laserTriangle, True, False), (self.x + self.size / 2 - 37, self.y + self.size / 2 - 56))
                    self.projectiles.append(Projectile(-10, self.y + self.size / 2 - 56, max(0, (-27 + self.x + self.size / 2)), 75, laserBeam, 0, 0, 1.5))
                #look like u poppin off cuz u is
                self.image = onekeyLaser
                #sound effect

        else:
            self.image = onekeyImage
        #LIGHTNING BALL: shoot a ball of lightning that drains mana
        if keys[self.keyDict["ability2"]]: 
            if (not self.holdingAbility2) and (self.mana > 250):
                self.projectiles.append(Projectile(self.x, self.y, 118, 110, lightningBall, 5 * self.xdirection, -5 * self.ydirection, 40, "lightning", False, 0))
                self.mana -= 250
                #blowback
                self.xv -= 10 * self.xdirection
                self.manaRecoveryTimer = 20
                #sound
                pygame.mixer.Channel(self.playerNumber + 3).play(pygame.mixer.Sound(path + 'zap.wav'))
            self.holdingAbility2 = True
        else:
            self.holdingAbility2 = False  

        #Operate continuous sound effect for laser
        #for event in pygame.event.get(): 
            #if event.type == pygame.KEYDOWN and event.key == self.keyDict["ability1"] and self.mana > 30:
                #pygame.mixer.Channel(self.playerNumber + 1).play(pygame.mixer.Sound('laser.wav'))
            #elif (event.type == pygame.KEYUP and event.key == self.keyDict["ability1"]) or (self.mana < 4):
                #pygame.mixer.Channel(self.playerNumber + 1).stop()

    def dizzykissAbilities(self):
        keys = pygame.key.get_pressed()
        #BLOW KISS - Shoot a piercing boomerang! Catch it on its return trip to heal!
        if keys[self.keyDict["ability1"]]: 
            if (not self.holdingAbility1) and (self.mana > 200):
                self.projectiles.append(Projectile(self.x, self.y + self.size / 2, 50, 50, heart, 40 * self.xdirection, 0, 3, "pierce", False, -1 * self.xdirection))
                self.mana -= 200
                self.manaRecoveryTimer = 20
                #sound
                pygame.mixer.Channel(self.playerNumber + 1).play(pygame.mixer.Sound(path + 'heart.wav'))
            self.holdingAbility1 = True
        else:
            self.holdingAbility1 = False   

        #do special self-collision and rotation for projectiles
        for proj in self.projectiles:
            #rotation
            proj.angle += 3
            if proj.tag == "pierce":
                #now do the things
                #self collision
                if not((proj.x > self.x + self.size or proj.x + proj.width < self.x) \
                or(proj.y > self.y + self.size or proj.y + proj.height < self.y)) and (proj.xv * proj.boomerang > 0):
                    self.projectiles.remove(proj)
                    self.hp = min(700, self.hp + 30)
                #wrap around
                if proj.x < -50 and abs(proj.xv) < 40:
                    proj.x = 1350
                elif proj.x >= 1350 and abs(proj.xv) < 40:
                    proj.x = -50

        #DIZZY STAR - Shoot a star down and double jump!
        if keys[self.keyDict["ability2"]]: 
            if (not self.holdingAbility2) and (self.mana > 250):
                self.projectiles.append(Projectile(self.x, self.y + (self.size / 5), 100, 100, star, 0, 15, 55, "star"))
                self.mana -= 250
                self.yv = -20
                self.manaRecoveryTimer = 20
                pygame.mixer.Channel(self.playerNumber + 3).play(pygame.mixer.Sound(path + 'star.wav'))
            self.holdingAbility2 = True
        else:
            self.holdingAbility2 = False   
    def ghonkeyAbilities(self):
        keys = pygame.key.get_pressed()
        #HAUNTING WAVE - Shoot haunting projectiles all around you!
        if keys[self.keyDict["ability1"]]: 
            if (not self.holdingAbility1) and (self.mana > 180):
                self.counter = 0
                for i in [-1, 0, 1]:
                    self.projectiles.append(Projectile(self.x, self.y, 90, 115, purpleFlame, 10 * self.xdirection, i * 3, 10, "haunt"))
                self.mana -= 180
                self.manaRecoveryTimer = 20
                #blowback
                self.xv -= 12 * self.xdirection
                #sound effect
                pygame.mixer.Channel(self.playerNumber + 1).play(pygame.mixer.Sound(path + 'soulfire.wav'))
            self.holdingAbility1 = True
        else:
            self.holdingAbility1 = False   
        #INVISIBILITY - Drift into the unknown!
        if keys[self.keyDict["ability2"]] and self.mana > 3.5:
            self.mana -= 2.5
            self.manaRecoveryTimer = 20
            self.transparency = max(0, self.transparency - 10)
            #sound effect if you are completely invisible
            if 0 < self.transparency <= 10:
                pygame.mixer.Channel(self.playerNumber + 3).play(pygame.mixer.Sound(path + 'ghostlaugh.wav'))
        else:
            self.transparency = min(255, self.transparency + 10)
        ghonkey.set_alpha(self.transparency)
        #541 * 693 is flame image 
    def doubleHunnyAbilities(self):
        keys = pygame.key.get_pressed()
        #DOUBLE ORBIT: Passively weild orbiting emojis around you! (i used trig hooray)
        self.orbitAngle += math.pi / 90
        if self.orbitAngle == math.pi * 2:
            self.orbitAngle = 0
        for i in range(2):
            tempAngle = self.orbitAngle + (math.pi * i)
            self.projectiles[i].x = ((self.x + self.size / 2 - self.projectiles[i].width / 2) + 300 * math.cos(tempAngle))
            self.projectiles[i].y = ((self.y + self.size / 2 - self.projectiles[i].height / 2) + 300 * math.sin(tempAngle))

            #Wrap around screen 
            if self.projectiles[i].x > 1300:
                self.projectiles[i].x -= 1300
            elif self.projectiles[i].x < 0:
                self.projectiles[i].x += 1300
        #EMBIGGEN: Spend mana to increase the size and damage of your orbiting emojis!
        if keys[self.keyDict["ability1"]]: 
            if (not self.holdingAbility1) and (self.mana > 350):
                self.mana -= 350
                self.counter = 50
                self.manaRecoveryTimer = 20
                #sound effect
                pygame.mixer.Channel(self.playerNumber + 1).play(pygame.mixer.Sound(path + 'boing.wav'))
            self.holdingAbility1 = True
        else:
            self.holdingAbility1 = False  

        #enforce embiggen
        self.counter = max(0, self.counter - 0.5)
        for proj in self.projectiles:
            if self.counter > 0:
                proj.width = 50 + self.counter
                proj.height = 50 + self.counter 
                proj.damage = 2 + self.counter / 25
            else:
                proj.width = 50
                proj.height = 50
                proj.damage = 2
        #BLINK: Teleport to the opposite side of the map!
        if keys[self.keyDict["ability2"]]: 
            if (not self.holdingAbility2) and (self.mana > 300):
                self.mana -= 300
                self.manaRecoveryTimer = 20
                self.x = abs(1300 - (self.x + self.size) )
                #sound effect
                pygame.mixer.Channel(self.playerNumber + 3).play(pygame.mixer.Sound(path + 'ding.wav'))
            self.holdingAbility2 = True
        else:
            self.holdingAbility2 = False   
    def freekeyAbilities(self):
        keys = pygame.key.get_pressed()
        #SNOWFLAKE SHURIKEN: Lob a snowflake that damages and freezes the enemy!
        if keys[self.keyDict["ability1"]]: 
            if (not self.holdingAbility1) and (self.mana > 320):
                self.mana -= 320
                self.manaRecoveryTimer = 20
                self.projectiles.append(Projectile(self.x, self.y - 20, 80, 80, snowflake, 20 * self.xdirection, -12, 70, "freeze", True, 0))
            self.holdingAbility1 = True
        else:
            self.holdingAbility1 = False   
        #AVALANCHE: Boost yourself with a jetpack of falling icicles!
        #54 by 119 
        if keys[self.keyDict["ability2"]] and self.mana > 3:
            self.mana -= 3
            self.manaRecoveryTimer = 20
            if frames % 3 == 0:
                self.projectiles.append(Projectile(self.x + random.randint(0, self.size - 54), self.y + self.size + 1, 54, 119, icicle, 0, 0, 4, "none", True, 0))
            self.yv = -2
            if keys[self.keyDict["left"]] or keys[self.keyDict["right"]]: 
                self.x += 2 * self.xdirection

        for proj in self.projectiles:
            if proj.tag == "freeze":
                proj.angle += 4
    def demonkeyAbilities(self):
        keys = pygame.key.get_pressed()
        #FEL FIREBALL: Launch a fireball that lifesteals! If it hits an enemy, another is created above them!
        if keys[self.keyDict["ability1"]]: 
            if (not self.holdingAbility1) and (self.mana > 190):
                self.mana -= 190
                self.manaRecoveryTimer = 20
                self.projectiles.append(Projectile(self.x, self.y, 138, 105, felFireballRight, 25 * self.xdirection, random.randint(-1, 1) - (8 * self.ydirection), 25, "felSpawn", False, 0))
            self.holdingAbility1 = True
        else:
            self.holdingAbility1 = False   

        #Do orientation for fel fireball
        for proj in self.projectiles:
            if proj.tag == "felSpawn" or proj.tag == "felSteal":
                if proj.xv < -20:
                    proj.image = felFireballLeft
                elif proj.yv > 0 and proj.xv == 0:
                    proj.image = felFireballDown

        #BLOOD SACRIFICE: Perform a demonic ritual to sacrifice some HP for a mana refill!
        if keys[self.keyDict["ability2"]]: 
            if (not self.holdingAbility2) and (self.hp > 100) and (self.mana < 390):
                self.hp -= 100
                self.mana = 400
                self.counter = 250
                #sound effect
                pygame.mixer.Channel(self.playerNumber + 3).play(pygame.mixer.Sound(path + 'suspense.wav'))
            self.holdingAbility2 = True
        else:
            self.holdingAbility2 = False   

        #pentagram blit
        if self.counter > 0:
            self.counter -= 4
            pentagram.set_alpha(self.counter)
            screen.blit(pygame.transform.scale(pentagram, (self.size, self.size)), (self.x, self.y))
    def bronkeyAbilities(self):
        keys = pygame.key.get_pressed()
        #BRONKEY PUNCH: Knock back opponents with a direct melee strike!
        if keys[self.keyDict["ability1"]]: 
            if (not self.holdingAbility1) and (self.mana > 250) and (len(self.projectiles) == 0):
                self.mana -= 250
                self.manaRecoveryTimer = 20
                self.counter = 250
                self.projectiles.append(Projectile(self.x + self.size * self.xdirection, self.y + 20, 151, 116, powImage, 0, 0, 9, "punch", False, 0))
                #sound effect
                pygame.mixer.Channel(self.playerNumber + 1).play(pygame.mixer.Sound(path + 'punch.wav'))
            self.holdingAbility1 = True
        else:
            self.holdingAbility1 = False   

        #BRONKEY UPPERCUT: Toss your opponent into the air!
        if keys[self.keyDict["ability2"]]: 
            if (not self.holdingAbility2) and (self.mana > 175) and (len(self.projectiles) == 0):
                self.projectiles.append(Projectile(self.x + 88 * self.xdirection + 30, self.y, 88, 128, [uppercutLeft, nothing, uppercutRight][self.xdirection + 1], 0, -2, 3, "uppercut", False, 0))
                self.mana -= 175
                self.counter = 250
                self.manaRecoveryTimer = 20
            self.holdingAbility2 = True
        else:
            self.holdingAbility2 = False   

        #transparency and clear
        if self.counter > 0:
            self.counter = max(0, self.counter - 7)
            powImage.set_alpha(self.counter)
            uppercutRight.set_alpha(self.counter)
            uppercutLeft.set_alpha(self.counter)
            #neutralize the projectile after a brief moment
            if self.counter < 200:
                (self.projectiles[0]).damage = 0
                (self.projectiles[0]).tag = "pierce"
        else:
            self.projectiles = []
    def doAbilities(self):
        #aha look its yanderedev-style programming
        if player.character == "clonkey":
            player.clonkeyAbilities()
        elif player.character == "onekey":
            player.onekeyAbiilties()
        elif player.character == "dizzykiss":
            player.dizzykissAbilities()
        elif player.character == "ghonkey":
            player.ghonkeyAbilities()
        elif player.character == "doubleHunny":
            player.doubleHunnyAbilities()
        elif player.character == "freekey":
            player.freekeyAbilities()
        elif player.character == "demonkey":
            player.demonkeyAbilities()
        else:
            player.bronkeyAbilities()
    def continuousSound(self, event):
        #play continuous sound with proper starting and stopping points
        #only operate this function if the player is Onekey or Freekey
        if self.character == "onekey":
            sound = pygame.mixer.Sound(path + 'laser.wav')
            manaReq = 4
            ability = "ability1"
        elif self.character == "freekey":
            sound = pygame.mixer.Sound(path + 'avalanche.wav')
            manaReq = 3
            ability = "ability2"
        else:
            return

        #now actually play the sound or cease the sound
        if event.type == pygame.KEYDOWN and event.key == self.keyDict[ability] and self.mana > manaReq * 8:
                pygame.mixer.Channel(self.playerNumber + 1).play(sound)
        elif (event.type == pygame.KEYUP and event.key == self.keyDict[ability]) or (self.mana < manaReq):
                pygame.mixer.Channel(self.playerNumber + 1).stop()

class Map:
    def __init__(self, image, platforms, music, positions = [50, 1100]):
        self.image = image
        self.platforms = platforms
        self.music = pygame.mixer.Sound(music + '.wav')
        self.positions = positions
    def display(self):
        #background
        screen.blit(self.image, (0, 0))
        #platforms
    def enforcePlatforms(self, player):
        tempGroundedState = False
        for platform in self.platforms:
            #if trisha paytas map display fries
            #if self == trishaFloorMap:
                #screen.blit(frenchFry, (platform[0], platform[1] - 15))
            #to collide, the player's "feet" must be touching the platform and they must be heading down
            if ((platform[2] >= player.x + 5 >= platform[0]) or (platform[0] <= player.x + player.size - 5 <= platform[2])) \
            and (platform[3] >= player.y + player.size >= platform[1]) and (player.yv >= 0): #and not(pygame.key.get_pressed()[self.keyDict["fall"]]):
                #now enforce collision
                player.y = platform[1] - player.size - 2
                if platform == [490, 480, 800, 530]:
                    player.yv = -10
                else:
                    player.yv = 0
                tempGroundedState = True
        player.grounded = tempGroundedState

class Projectile:
    def __init__(self, x, y, width, height, image, xv = 0, yv = 0, damage = 0, tag = "none", lobbed = False, boomerang = 0, yboom = 0, alpha = 255):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.damage = damage
        self.xv = xv
        self.yv = yv
        self.tag = tag
        self.lobbed = lobbed
        self.boomerang = boomerang
        self.angle = 0
        self.alpha = alpha
    def display(self):
        screen.blit(pygame.transform.rotate(pygame.transform.scale(self.image, (int(self.width), int(self.height)) ), self.angle), (self.x, self.y))
    def enforceMovement(self):
        #account for gravity only if it is lobbed
        if self.lobbed:
            self.yv += 0.8
        #make it go backwards only if it is a boomerang
        self.xv += self.boomerang
        #enforce movement based on velocity
        self.x += self.xv
        self.y += self.yv
    def doCollision(self, target, owner):
        #if ((self.x <= target.x <= self.x + self.width) or (self.x <= target.x + target.size <= self.x + self.width)) \
        #and ((self.y <= target.y <= self.y + self.height) or (self.y <= target.y + target.size <= self.y + self.height)):

        if not((self.x > target.x + target.size or self.x + self.width < target.x) \
        or(self.y > target.y + target.size or self.y + self.height < target.y)):

            #damage time
            target.hp = max(0, target.hp - self.damage)

            #TAGS: Apply numerous kinds of special effects for different projectiles
            if self.tag == "bananaPeel": #knock back--that peel is slippery!
                target.xv += self.xv * 1.3
                pygame.mixer.Channel(owner.playerNumber + 1).play(pygame.mixer.Sound(path + 'splat.wav'))
            elif self.tag == "lightning": #lightning steals mana! That makes sense!
                target.mana = max(0, target.mana - 250)
                owner.mana = min(400, owner.mana + 150)
            elif self.tag == "pierce": #hearts and other things pierce!
                return False
            elif self.tag == "star": #stop opponent momentum!
                target.xv = 0
                target.yv = 0
            elif self.tag == "haunt": #if you hit all 3 flames, deal bonus damage!
                owner.counter += 1
                if owner.counter == 3:
                    target.hp -= 50
                    owner.counter = 0
            elif self.tag == "freeze": #stun the enemy with a chilling chill (?) !
                target.frozen = 85
                target.xv = 0
                target.yv = 0
                pygame.mixer.Channel(owner.playerNumber + 1).play(pygame.mixer.Sound(path + 'freeze.wav'))
            elif self. tag == "felSpawn": #spawn more fireballs and lifesteal!
                owner.hp = min(700, owner.hp + 15)
                pygame.mixer.Channel(owner.playerNumber + 1).play(pygame.mixer.Sound(path + 'demonbolt.wav'))
                owner.projectiles.append(Projectile(target.x + target.size / 2 - 52, target.y - target.size - 2, 105, 138, felFireballUp, 0, -28, 25, "felSteal", True, 0))
            elif self.tag == "felSteal": #just lifesteal
                owner.hp = min(700, owner.hp + 15)
                pygame.mixer.Channel(owner.playerNumber + 1).play(pygame.mixer.Sound(path + 'demonbolt.wav'))
            elif self.tag == "punch": #knock back and return false
                #target.x = self.x + (self.width + 5) * owner.xdirection
                target.xv += 3 * owner.xdirection
                return False
            elif self.tag == "uppercut" : #knock up, stun, and return false
                target.y = self.y - (self.height + 3)
                target.yv = -20
                target.xv = 0
                if target.character != "dizzykiss":
                    target.stun = 40
                return False

            return True
        else:
            return False
def betterRect(color, x1, y1, x2, y2, width = 0):
    pygame.draw.polygon(screen, (color), ([(int(x1), int(y1)), (int(x2), int(y1)), (int(x2), int(y2)), (int(x1), int(y2))]), width)
def distanceFormula(x1, y1, x2, y2):
    return(int(math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )))
def create_fonts(font_sizes_list):
    #Creates different fonts with one list
    fonts = []
    for size in font_sizes_list:
        fonts.append(
            pygame.font.SysFont("Arial", size))
    return fonts
def render(fnt, what, color, where):
    #Renders the fonts as passed from display_fps
    text_to_show = fnt.render(what, 0, pygame.Color(color))
    screen.blit(text_to_show, where)
def display_fps():
    #Data that will be rendered and blitted in _display
    render(
        fonts[0],
        what=str(int(clock.get_fps())),
        color="white",
        where=(10, 0))
#SOUND NOTES
#Channel 0: Background Music
#Channel 1: Player 1 Sounds
#Channel 2: Player 2 Sounds
#Channel 3: Player 1 Continuous Sounds
#Channel 4: Player 2 Continuous Sounds
#Channel 5: Other Sounds
def playMapMusic(map):
    pass
#Pygame-specific variables
clock = pygame.time.Clock()
screen_width = 1300
screen_height = 730
screen = pygame.display.set_mode([screen_width,screen_height])
done = False
pygame.display.set_caption("Combomoji Brawl")
fonts = create_fonts([30])

#images (brain dump)
path = os.getcwd() + "\\"
clonkeyImage = pygame.image.load(path + 'clonkey.png')
onekeyImage = pygame.image.load(path + 'onekey.png')
healthbars = pygame.image.load(path + 'healthbars.png')
bananaPeel = pygame.image.load(path + 'bananaPeel.png')
laserBeam = pygame.image.load(path + 'laserBeam.png')
lightningBall = pygame.image.load(path + 'lightning.png')
onekeyLaser = pygame.image.load(path + 'onekeyLaser.png')
laserTriangle = pygame.image.load(path + 'laserTriangle.png')
dizzyKiss = pygame.image.load(path + 'dizzykiss.png')
heart = pygame.image.load(path + 'heart.png')
star = pygame.image.load(path + 'star.png')
ghonkey = pygame.image.load(path + 'ghonkey.png')
nothing = pygame.image.load(path + 'nothing.png')
purpleFlame = pygame.image.load(path + 'purpleFlame.png')
doubleHunny = pygame.image.load(path + 'doubleHunny.png')
redLaugh = pygame.image.load(path + 'redLaugh.png')
titleScreen = pygame.image.load(path + 'titleScreen.png')
characterSelection = pygame.image.load(path + 'characterSelection.png')
grayOk = pygame.image.load(path + 'grayOk.png')
redOk = pygame.image.load(path + 'redOk.png')
p1 = pygame.image.load(path + 'p1.png')
p2 = pygame.image.load(path + 'p2.png')
frenchFry = pygame.image.load(path + 'frenchFry.png')
freekey = pygame.image.load(path + 'freekey.png')
demonkey = pygame.image.load(path + 'demonkey.png')
snowflake = pygame.image.load(path + 'snowflake.png')
icicle = pygame.image.load(path + 'icicle.png')
felFireballDown = pygame.image.load(path + 'felFireball.png')
felFireballUp = pygame.transform.flip(pygame.image.load(path + 'felFireball.png'), False, True)
felFireballLeft = pygame.image.load(path + 'felFireballLeft.png')
felFireballRight = pygame.transform.flip(pygame.image.load(path + 'felFireballLeft.png'), True, False)
pentagram = pygame.image.load(path + "pentagram.png")
iceBlock = pygame.image.load(path + "iceBlock.png")
danceStudioImage = pygame.image.load(path + "danceStudioMap.png")
microwaveImage = pygame.image.load(path + "microwaveMap.png")
trishaFloorImage = pygame.image.load(path + "trishaFloorMap.png")
countyJailImage = pygame.image.load(path + "countyJailMap.png")
tomatoImage = pygame.image.load(path + "tomatoMap.png")
mapSelectionScreen = pygame.image.load(path + "mapSelectionScreen.png")
goldenFrame = pygame.image.load(path + "goldenFrame.png")
bronkey = pygame.image.load(path + "bronkey.png")
powImage = pygame.image.load(path + "pow.png")
uppercutRight = pygame.image.load(path + 'upArrow.png')
uppercutLeft = pygame.transform.flip(pygame.image.load(path + 'upArrow.png'), True, False)
stunStars = pygame.image.load(path + 'stunStars.png')
windowsillImage = pygame.image.load(path + 'windowsillMap.png')
victoryScreen = pygame.image.load(path + 'victoryScreen.png')
#ALL SOUNDS
#splat = pygame.mixer.sound('splat.mp3')
#library of icon locations for display during the character selection screen
coordinateDict = {
    "clonkey" : [580, 0],
    "dizzykiss" : [850, 0],
    "doubleHunny" : [320, 0],
    "ghonkey" : [75, 0],
    "onekey" : [340, 250],
    "freekey" : [580, 250],
    "demonkey" : [75, 250],
    "bronkey" : [850, 250]
    }
#game variables including map descriptions
currentScreen = "title"
danceStudioMap = Map(danceStudioImage, [[-100, 695, 1400, 750], [-100, 510, 400, 555], [900, 510, 1500, 555]], path + 'pearls')
countyJailMap = Map(countyJailImage, [[-100, 700, 400, 750], [-100, 465, 250, 510], [1050, 465, 1400, 510], [900, 700, 1400, 750]], path + 'flatback')
windowsillMap = Map(windowsillImage, [[-100, 705, 275, 750], [450, 500, 850, 545], [1025, 705, 1400, 750]], path + 'roaches')
microwaveMap = Map(microwaveImage, [[-100, 715, 1400, 750], [490, 480, 800, 530]], path + 'bagel')
trishaFloorMap = Map(trishaFloorImage, [[420, 580, 920, 720]], path + 'iconic', [380, 770])
tomatoMap = Map(tomatoImage, [[130, 420, 480, 560], [760, 550, 1200, 650]], path + 'circus')
currentMap = countyJailMap
frames = 0
#player variable that represents the neutral environment (its character does not matter at all) (not currently implemented)
#environment = Player("clonkey", 0, 0, 150, 3)

#Main
while not done:
    #quit if u quit
    #clock.tick(70)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
    #have u chosen a character and a map yet? no bc u just started idiot
    p1set = False
    p2set = False
    mapset = False
    gameDelay = 70
    #no one has won yet
    victory = "none"
    
    while not done and currentScreen == "title":
        #quit if u quit
        clock.tick(70)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True
        #screen fill
        for x in range(0, 1301, 100):
            for y in range(0, 731, 73):
                betterRect((x // 5.1, y // 5.1, y // 3), x, y, x + 100, y + 73)
        #display art
        screen.blit(titleScreen, (0, 0))
        #See where the mouse is
        mousey = pygame.mouse.get_pos()[1]
        mousex = pygame.mouse.get_pos()[0]
        #Clicking the mouse 
        if pygame.mouse.get_pressed()[0]:
            #start button 
            if 425 <= mousex <= 825 and 400 <= mousey <= 500:
                currentScreen = "characterSelection"
        pygame.display.flip()

    while not done and currentScreen == "characterSelection":
        #quit if u quit
        clock.tick(70)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True
        #screen fill
        for x in range(0, 1301, 50):
            for y in range(0, 731, 46):
                betterRect((255 - x // 5.1, y // 3 + 12, x // 5.1), x, y, x + 100, y + 73)
        #display art
        screen.blit(characterSelection, (0, 0))
        #display Ok button
        if not (p1set and p2set):
            screen.blit(grayOk, (1120, 270))
        elif player1.character == player2.character:
            screen.blit(grayOk, (1120, 270))
        else:
            screen.blit(redOk, (1120, 270))
        #See where the mouse is
        mousey = pygame.mouse.get_pos()[1]
        mousex = pygame.mouse.get_pos()[0]
        #Clicking the mouse 
        if pygame.mouse.get_pressed()[0]:
            #ok button
            if mousex >= 1120 and 270 <= mousey <= 370 and p1set and p2set:
                if player1.character != player2.character:
                    player2.xdirection = -1
                    currentScreen = "mapSelection"
            #all character selection for player 1
            #top row
            if 75 <= mousey <= 300:
                p1set = True
                if 50 < mousex < 250:
                    player1 = Player("ghonkey", 50, 400, 150, 1)
                elif 250 < mousex < 500:
                    player1 = Player("doubleHunny", 50, 400, 150, 1)
                elif 500 < mousex < 775:
                    player1 = Player("clonkey", 50, 400, 150, 1)
                elif 775 < mousex < 1025:
                    player1 = Player("dizzykiss", 50, 400, 150, 1)
                else:
                    p1set = False
            #bottom row
            elif 300 < mousey < 550:
                p1set = True
                if 25 < mousex < 275:
                    player1 = Player("demonkey", 50, 400, 150, 1)
                elif 275 < mousex < 525:
                    player1 = Player("onekey", 50, 400, 150, 1)
                elif 525 < mousex < 775:
                    player1 = Player("freekey", 50, 400, 150, 1)
                elif 775 < mousex < 1025:
                    player1 = Player("bronkey", 50, 400, 150, 1)
                else:
                    p1set = False
        if pygame.mouse.get_pressed()[2]:
            #all character selection for player 2
            #top row
            if 75 <= mousey <= 300:
                p2set = True
                if 50 < mousex < 250:
                    player2 = Player("ghonkey", 1100, 400, 150, 2)
                elif 250 < mousex < 500:
                    player2 = Player("doubleHunny", 1100, 400, 150, 2)
                elif 500 < mousex < 775:
                    player2 = Player("clonkey", 1100, 400, 150, 2)
                elif 775 < mousex < 1025:
                    player2 = Player("dizzykiss", 1100, 400, 150, 2)
                else:
                    p2set = False
                #bottom row
            elif 300 < mousey < 550:
                p2set = True
                if 25 < mousex < 275:
                    player2 = Player("demonkey", 1100, 400, 150, 2)
                elif 275 < mousex < 525:
                    player2 = Player("onekey", 1100, 400, 150, 2)
                elif 525 < mousex < 775:
                    player2 = Player("freekey", 1100, 400, 150, 2)
                elif 775 < mousex < 1025:
                    player2 = Player("bronkey", 1100, 400, 150, 2)
                else:
                    p2set = False
        #display p1 and p2 icons above their respective characters
        if p1set:
            screen.blit(p1, coordinateDict[player1.character])
        if p2set:
            screen.blit(p2, coordinateDict[player2.character])
        pygame.display.flip()

    while not done and currentScreen == "mapSelection":
        #quit if u quit
        clock.tick(70)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True
        #screen fill
        for x in range(0, 1301, 50):
            for y in range(0, 731, 46):
                betterRect((y // 3, x // 5.1, y // 3), x, y, x + 100, y + 73)

        #display ok button and main art
        screen.blit(mapSelectionScreen, (0, 0))
        if mapset:
            screen.blit(redOk, (700, 575))
        else:
            screen.blit(grayOk, (700, 575))
        #display golden selection border
        if mapset:
            screen.blit(goldenFrame, borderCoords)
        #See where the mouse is
        mousey = pygame.mouse.get_pos()[1]
        mousex = pygame.mouse.get_pos()[0]

        #Clicking the mouse 
        if pygame.mouse.get_pressed()[0]:
            #ok button
            if 700 <= mousex <= 1000 and 575 <= mousey <= 700 and mapset:
                currentScreen = "game"
            #maps selection
            elif 30 <= mousex <= 416 and 30 <= mousey <= 249:
                mapset = True
                currentMap = danceStudioMap
                borderCoords = [28, 27]
            elif 450 <= mousex <= 836 and 30 <= mousey <= 249:
                mapset = True
                currentMap = countyJailMap
                borderCoords = [445, 27]
            elif 870 <= mousex <= 1256 and 30 <= mousey <= 249:
                mapset = True
                currentMap = windowsillMap
                borderCoords = [860, 27]
            elif 30 <= mousex <= 416 and 253 <= mousey <= 485:
                mapset = True
                currentMap = microwaveMap
                borderCoords = [28, 276]
            elif 450 <= mousex <= 836 and 253 <= mousey <= 485:
                mapset = True
                currentMap = trishaFloorMap
                borderCoords = [445, 276]
            elif 870 <= mousex <= 1256 and 253 <= mousey <= 485:
                mapset = True
                currentMap = tomatoMap
                borderCoords = [860, 276]

        pygame.display.flip()
    if not done:
        #play music to start the game
        pygame.mixer.Channel(0).play(currentMap.music)
        #set player positions to start the game
        player1.x = currentMap.positions[0]
        player2.x = currentMap.positions[1]
    while not done and currentScreen == "game":
        #quit if u quit
        clock.tick(80)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True
            player1.continuousSound(event)
            player2.continuousSound(event)
        #frames
        frames += 1
        #display map and health bars and mana bars
        currentMap.display()
        #player 1 health and mana
        betterRect((255, 0, 0), 139, 30, 139 + (player1.hp / 1.443), 73)
        betterRect((0, 255, 255), 140, 80, 135 + player1.mana, 118)
        #player 2 health and mana
        betterRect((255, 0, 0), 1163 - (player2.hp / 1.443), 30, 1163, 73)
        betterRect((0, 255, 255), 1165 - player2.mana, 80, 1160, 118)
        #main health bars
        screen.blit(healthbars, (0, 0))
        #display icons of player characters up top
        #player 1
        screen.blit(pygame.transform.scale(player1.image, (120, 120)), (19, 18))
        #player1.clonkeyAbilities()
        #player 2
        screen.blit(pygame.transform.scale(player2.image, (120, 120)), (1160, 18))
        #display players, operate their movement, detect their collisions
        for player in [player1, player2]:
            currentMap.enforcePlatforms(player)
            player.display()
            #perform abilities and movement(unless frozen)
            if player.frozen == 0:
                player.operateMovement()
                if player.stun == 0:
                    player.doAbilities()
                else:
                    stunStars.set_alpha(player.stun * 6)
                    screen.blit( pygame.transform.scale(stunStars, (player.size, player.size)), (player.x, player.y))
                    player.stun -= 1
            else:
                #if frozen you can't move or use abilities
                #iceblock animation
                iceBlock.set_alpha(player.frozen * 3)
                screen.blit( pygame.transform.scale(iceBlock, (player.size, player.size)), (player.x, player.y))
                player.frozen -= 1
            #clear excess projectiles
            player.clearProjectiles()
            #do projectile management and enforcement
            for projectile in player.projectiles:
                projectile.display()
                projectile.enforceMovement()
                if player.playerNumber == 1:
                    if projectile.doCollision(player2, player1):
                        player.projectiles.remove(projectile)
                else:
                    if projectile.doCollision(player1, player2):
                        player.projectiles.remove(projectile)
        #do everything related to the environment if necessary
        #(self, x, y, width, height, image, xv = 0, yv = 0, damage = 0, tag = "none", lobbed = False, boomerang = 0, yboom = 0, alpha = 255)
        #if currentMap == tomatoMap:
            #random tomatoes
            #if random.randint(0, 200) == 1:
                #environment.projectiles.append(Projectile(700, 0, 50, 50, bananaPeel, 0, 0, 50, "none", True))
            #enforce
            #for proj in environment.projectiles:
                #proj.display()
                #proj.enforceMovement()
        #detect if one player has won the fight!
        if player1.hp <= 0 and gameDelay == 70:
            victory = "p2"
        elif player2.hp <= 0 and gameDelay == 70:
            victory = "p1"

        if victory == "p2" or victory == "p1":
            gameDelay -= 1
        if gameDelay == 0:
            currentScreen = "victory"
        display_fps()
        pygame.display.flip()

    #reset all images that may have changed
    ghonkey.set_alpha(255)
    #stop music and play victory sound
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(path + 'tada.wav'))
    while not done and currentScreen == "victory":
        #quit if u quit
        clock.tick(75)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True
        #display art
        #screen fill
        for x in range(0, 1301, 50):
            for y in range(0, 731, 46):
                betterRect((255 - x // 5.1, y // 3 + 12, x // 5.1), x, y, x + 100, y + 73)
        #images
        screen.blit(victoryScreen, (0, 0))
        if victory == "p1":
            screen.blit(pygame.image.load(path +  (player1.character + "Logo.png")), (55, 50))
            screen.blit(pygame.transform.scale(player1.image, (290, 290)), (30, 370))
            screen.blit(pygame.transform.rotate(pygame.transform.scale(player2.image, (150, 150)), 33), (1100, 520))
        else:
            screen.blit(pygame.image.load(path + (player2.character + "Logo.png")), (55, 50))
            screen.blit(pygame.transform.scale(player2.image, (290, 290)), (30, 370))
            screen.blit(pygame.transform.rotate(pygame.transform.scale(player1.image, (150, 150)), 33), (1100, 520))
        #See where the mouse is
        mousey = pygame.mouse.get_pos()[1]
        mousex = pygame.mouse.get_pos()[0]
        #clicking the mouse for Menu or Rematch with same characters and map
        if pygame.mouse.get_pressed()[0]:
            #rematch
            if 600 < mousex < 1100 and 230 < mousey < 350:
                player1 = Player(player1.character, 50, 400, 150, 1)
                player2 = Player(player2.character, 1100, 400, 150, 2)
                currentScreen = "game"
            elif 700 < mousex < 1000 and 390 < mousey < 490:
                currentScreen = "title"

        pygame.display.flip()
pygame.mixer.quit()
pygame.quit()
