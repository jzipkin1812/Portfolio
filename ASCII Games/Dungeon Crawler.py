#Dungeon Crawler
#By Javin Zipkin
#Special thanks to Karyn Voldstad

#housekeeping
killstage = 0
import random
import math
import sys
tea = 1
cursetimer = 0
orbofdeath = 0
health = 100
bosshealth1 = 250
poisontimer = 0
killedmonster1 = 0
killedmonster2 = 0
killedmonster3 = 0
killedmonster4 = 0

#Functions for item checking and checking if you defeated a monster or not
def itemcheck(): 
    if (chosenitemkey.lower()) == "bs":
        chosenitem = beginner_shield
    elif (chosenitemkey.lower()) == "ww":
        chosenitem = wooden_wand
    elif (chosenitemkey.lower()) == "is":
        chosenitem = iron_sword
    elif (chosenitemkey.lower()) == "vw":
        chosenitem = vampiric_wand
    elif (chosenitemkey.lower()) == "ba":
        chosenitem = bow_and_arrow
    elif (chosenitemkey.lower()) == "ls":
        chosenitem = lightning_sword   
    else:
        chosenitem = nothing
    return chosenitem

def defeatcheck():
    global health
    global killstage	
    global possibledamage
    global poisontimer
    global cursetimer
    global tea
    if "block" in chosenitem[2] and chosenitem in posessed_items and (chosenitemkey.lower()) not in stagemonsters[chosenmonsterA][0]:
        possibledamage -= chosenitem[2][1]
        print("You blocked " + str(chosenitem[2][1]) + " damage.")
    
    if "leech" in chosenitem[2] and chosenitem in posessed_items and (chosenitemkey.lower()) in stagemonsters[chosenmonsterA][0]:
        health += (chosenitem[2][1]) * tea
        print("You leeched " + str(chosenitem[2][1]) + " health from the enemy.")
        print("Your health is now " + str(health) + ".")
        
    if (chosenitemkey.lower()) in stagemonsters[chosenmonsterA][0] and chosenitem in posessed_items:
        if "speed" in chosenitem[2]:
            killstage += chosenitem[2][1]
        print(stagemonsters[chosenmonsterA][4])        
        killstage += 1        
    
    if possibledamage > 0:
        if (chosenitemkey.lower()) not in stagemonsters[chosenmonsterA][0] or chosenitem not in posessed_items:
            health -= possibledamage
            killstage += orbofdeath
            print(stagemonsters[chosenmonsterA][3])
            print("Your health is now " + str(health) + ".")  
    
    if stagemonsters[chosenmonsterA] == poisonspider:
        if (chosenitemkey.lower()) not in stagemonsters[chosenmonsterA][0] or chosenitem not in posessed_items:
            print("A harmful poison chokes you. It will deal continuous damage.")
            poisontimer += 4
    
    if stagemonsters[chosenmonsterA] == witch:
        if (chosenitemkey.lower()) not in stagemonsters[chosenmonsterA][0] or chosenitem not in posessed_items:            
            cursetimer += 4
            tea *= -1
    
    if stagemonsters[chosenmonsterA] == earthelemental and (chosenitemkey.lower()) == "bs":
        if beginner_shield[2][1] >= 3:
            beginner_shield[2][1] -= 3
            print("Your shield was dented in the attack! It now blocks " + str(beginner_shield[2][1]) + " damage.")   
    
    if cursetimer > 0:
        cursetimer -= 1
        if cursetimer > 0: 
            print("The curse still haunts you.")
        else:
            print("The curse lifts, hooray!")
            tea *= -1   
    
    if poisontimer > 0:
        poisontimer -= 1
        print("You feel the effects of the poison.")
        health -= 10
        print("Your health is now " + str(health) + ".")   

#Item variable assignment (Each item is assigned the letters used to select it, a name, and properties)

nothing = ["null", "null", []]
iron_sword = ["is", "Iron Sword ", []]
wooden_wand = ["ww", "Wooden wand ", []]
beginner_shield = ["bs", "Beginner Shield ", ["block", 5]]
vampiric_wand = ["vw", "Vampiric Wand", ["leech", 10]]
bow_and_arrow = ["ba", "Bow and Arrow", ["speed", 0.5]]
lightning_sword = ["ls", "Lightning Sword", ["speed", 0.5]]

#Monster variable assignment (each monster name is assigned the items that can defeat it, an 
#encounter message, its damage, a defeat message, and a victory message)

    #Stage 1 monsters
goblin = [["is", "ww", "vw"], "\nYou encounter a fierce goblin! It wants blood...", 30, "Grrr...The goblin attacks!", "The goblin starts crying and leaves."]
skeleton = [["is"], "\nBefore you is an undead skeleton...It rattles.", 10, "The skeleton is not defeated! It throws a bone at yor head and leaves.", "The skeleton dies! ...again."]
arrow = [["bs"], "\nWhoosh! An arrow flies towards your head! What can you use to stop it?", 15, "Ouch! You couldn't stop the arrow.", "You circumvented the arrow, hooray!"]
bat = [["ww", "bs", "ba"], "\nA scary bat appears!", 5, "Yowch, it bit! It then flew away...", "No rabies for you! The bat was exterminated."]
slime = [["ww", "vw"], "\nGross, a slime monster appears!", 20, "The slime crawls on over you...it feels awful, but at least it leaves after.", "The slime turns into water and evaporates."]

    #Stage 2 monsters
willowisp = [["vw"], "\nA spooky ball of fire floats near.", 10, "It burns! IT BURNS!", "The spooky wisp stops burning. Your magic worked."] 
zombie = [["is", "ba"], "\nYou encounter a horrible zombie! It wants brains.", 40, "It takes a big bite! That's gotta hurt.", "The zombie dies! ...again."]
rollingboulder = [["te"], "\nAaah! A boulder is rolling right towards you! There's no way to break it..maybe block it?", 30, "Bang! The boulder hits you.", "You teleport away safely."]

    #Stage 3 monsters
ghoul = [["ww", "vw"], "\nA wispy ghost materializes in front of you.", 30, "The ghost screams at you, piercing your ears.", "If there's something strange, in ya neighborhood, who you gonna call?\nClearly you, because you beat the ghost."]
lightning = [["ls"], "\nYou hear thunder overhead...lightning is about to strike!", 15, "ZAP!", "You channel the lightning's energy and escape unharmed."]
poisonspider = [["ba"], "\nA tiny spider floats in front of you in a sticky web. It's harmless...right?", 5, "It bites you...then leaves. What did it do?", "The spider lets out a very tiny scream and dies."]

    #Stage 4 monsters
witch = [["ba", "ls"], "\nAn ugly hag is before you. She cackles and raises her wand!", 5, "She puts a curse on you! Healing directed towards you will be \ntransformed into damage for awhile, so be careful.", "The old hag disappears. Phew!"]
earthelemental = [["bs"], "\n\"GRAAA!\" An angry earth elemental waves its fists.", 20, "Bang! The elemental strikes.", "It smashes your shield, but you run away!"]

#Intro
posessed_items = [iron_sword, wooden_wand, beginner_shield]
print("Welcome to Dungeon Crawler! Beat enemies and survive.")
print("You start with 100 Health. Make sure to keep it above 0.")
print("Each item you posess can be used by inputting its keycode. This is not case sensitive. \nExample: yx (or YX)")
print("You posess an Iron Sword (is), a Wooden Wand (ww), and a Beginner's shield (bs).") 

#first stage, first monster generator
stagemonsters = [goblin, skeleton, arrow, bat, slime]
killstage = 0

while health > 0 and killedmonster1 < 7:
    chosenmonsterA = random.randint(0, 4)
    possibledamage = stagemonsters[chosenmonsterA][2]
    print(stagemonsters[chosenmonsterA][1])
    chosenitemkey = input("What item do you use? (input its keycode.) ")
    
    #Chosen item checker
    chosenitem = itemcheck()
            
    #defeat checker & item property checker
    defeatcheck()
    killedmonster1 += killstage
    killstage = 0
        
if health > 0:
    print("Yay, you beat stage 1! Onto stage 2...")
else:
    exit(" The monsters beat you! And this is the easiest stage...are you \nsure you understand this game?")

#First loot reward (inbetween stages 1 and 2)
print("\nYou feel powerful...after every stage, your strength will grow!")
upgrade1 = input("Input a single digit number. 1)Upgrade your shield 2)Drink a healing potion 3)Find a new item")
if upgrade1 == "1":
    print("Your shield now blocks 15 damage instead of 5! (Its keycode is still the same.)")
    beginner_shield[2][1] += 10
if upgrade1 == "2":
    health += 75 * tea
    print("You now have " + str(health) + " health remaining.")
if upgrade1== "3":
    print("You found a vampiric wand (vw)! This weapon will grant you health when defeating an enemy.")
    posessed_items.append(vampiric_wand)
    #print(posessed_items)

#second stage
stagemonsters = [skeleton, arrow, slime, willowisp, zombie, rollingboulder]
killstage = 0

while health > 0 and killedmonster2 < 7:
    chosenmonsterA = random.randint(0, 5)
    possibledamage = stagemonsters[chosenmonsterA][2]
    print(stagemonsters[chosenmonsterA][1])
    chosenitemkey = input("What item do you use? ")
    
    #Chosen item checker
    chosenitem = itemcheck()
        
    #defeat checker & item property checker
    defeatcheck()
    killedmonster2 += killstage
    killstage = 0
    
if health > 0:
    print("Stage 2 is complete.")
    #if health > 50 and upgrade1 == "3":
        #print("~The curse of the vampire falls upon you!\nThe wand punishes you for stealing its power.~")
        #health -= 30
        #print("Your health is now " + str(health) + ".")
else:
    exit(" The monsters beat you! Back to stage 1, I guess.")         
          
#Second loot reward (inbetween stages 2 and 3)
print("\nYou feel powerful...after every stage, your strength will grow!")
upgrade2 = input("Input a single digit number. 1)Upgrade your shield 2)Drink a healing potion 3)Find a new item")
if upgrade2 == "1":
    print("Your shield now blocks an additional 10 damage! (Its keycode is still the same.)")
    beginner_shield[2][1] += 10
if upgrade2 == "2":
    health += 75 * tea
    print("You now have " + str(health) + " health remaining.")
if upgrade2 == "3":
    print("You found a bow and arrow (ba)! This weapon can easily \ndestroy flying enemies and some others.")
    posessed_items.append(bow_and_arrow)
    #print(posessed_items)    

upgrade2B = input("You may upgrade yourself again. Input 1 to gain an offensive passive ability, or 2 to gain a defense passive ability.")
if upgrade2B == "1":
    killedmonster3 += 2
    killedmonster4 += 2
    print("You recieved the Scroll of Speed! You now don't have to \ndefeat as many monsters to clear a stage.")
if upgrade2B == "2":
    posessed_items.append("Regeneration Orb")
    print("You now have a regeneration orb! You will generate 30 health upon completing a stage.")    
    
#Third stage
stagemonsters = [willowisp, goblin, poisonspider, rollingboulder, lightning, poisonspider, ghoul]
killstage = 0

while health > 0 and killedmonster3 < 11:
    chosenmonsterA = random.randint(0, 6)
    possibledamage = stagemonsters[chosenmonsterA][2]
    print(stagemonsters[chosenmonsterA][1])
    chosenitemkey = input("What item do you use? ")
    
    #Chosen item checker
    chosenitem = itemcheck()
        
    #defeat checker & item property checker
    defeatcheck()
    killedmonster3 += killstage
    killstage = 0
    
if health > 0:
    if "Regeneration Orb" in posessed_items:
        health += 30 * tea
        print("The orb glows...your health is now " + str(health) + ".")
    print("Stage 3 is complete.")
else:
    exit(" The monsters beat you! And you were so close to the first boss...")         
          
#Stage 3 upgrades
print("\nThe next room you enter will be different...you feel scared. \nRight now, though, there is peace.")
health += 50 * tea
poisontimer = 0
print("Your health is now " + str(health) + ".")
upgrade4 = input("Input a single digit number. 1)Recieve an advantage over your next enemy 2)Upgrade your shield 3)Get a new item")
if upgrade4 == "1":
    print("You hear a terrifying scream from ahead of you. Something was just injured...")
    bosshealth1 -= 100
if upgrade4 == "2":
    print("Your shield now blocks an additional 10 damage! (Its keycode is still the same.)")
    beginner_shield[2][1] += 10
if upgrade4 == "3":
    print("You found a Lighning Sword (ls)! This amazing blade will electrify enemies.")
    posessed_items.append(lightning_sword)

    #Boss: Xentana, the Withering Banshee
poisondamage = 5
print("\nThe room  you enter is large, round, and humid. The floor is \ngrated, and you can see through it. There is acid under you.")
print("Suddenly, the ominous suspense is broken...an enormous ghoul \nemerges from the acid! It carries a green scythe dripping with \nslime. Its eyes and mouth are hollow an dark.")
print("It is Xentana, the Wayward Wither! Xentana commands the forces of disgust and rot.")

while health > 0 and bosshealth1 > 0:
    chosenattack = random.choice(["scythe", "charge", "sink", "poisonball"])
    
    if chosenattack == "scythe":
        print("\nThe ghoul swings its scythe at you!")
    elif chosenattack == "charge":
        print("\nXentana charges at you with a disgusting stare!")  
    elif chosenattack == "sink":
        print("\nXentana invisibly sinks into the acid below.")
    elif chosenattack == "poisonball":
        print("\nXentana releases a cloud of acidic dust into the air.")
    
    chosenitemkey = input("What item do you use? ")    
         
    #Chosen item checker
    chosenitem = itemcheck()
    
    #Attacks
    if chosenattack == "scythe":        
        if chosenitem == beginner_shield and chosenitem in posessed_items:
            print("Xentana staggers back. You blocked the scythe.")
        else:
            health -= 30
            print("The scythe pierces your stomach! Your health is now " + str(health) + ".")        
    
    elif chosenattack == "charge":
        if chosenitem == (iron_sword or lightning_sword) and chosenitem in posessed_items: 
            print("The sword stabs through Xentana's head and the ghoul dissapates, for a moment.")
            bosshealth1 -= 50
        else:
            health -= 30
            print("Ouch! Can a ghost really hit THAT hard? Your health is now " + str(health) + ".")
    
    elif chosenattack == "sink":
        if chosenitem == wooden_wand:
            if chosenitem in posessed_items: 
                print("The wand's magic reaches Xentana even through the thick, boiling acid. The ghoul screams.")
                bosshealth1 -= 50
                #if chosenitem == vampiric_wand:
                    #print("You leeched 10 Health from Xentana.")
                    #health += 10
        else:
            health -= 30
            print("Xentana erupts from the acid, striking you! Your health is now " + str(health) + ".")
            
    elif chosenattack == "poisonball":
        if chosenitem != beginner_shield and chosenitem in posessed_items: 
            print("You strike at Xentana while it is channeling its magic. However, the acidity in the air still increases.")
            if chosenitem == vampiric_wand:
                print("You leeched 10 Health from Xentana.")
                health += 10 * tea
            bosshealth1 -= 50
            poisondamage *= 2
        else:
            print("The acidity level in the air increases.")
            poisondamage *= 2
            
            #gradual poison 
    health -= poisondamage
    print("\nThe acid surrounding you feels akin to the poison from the previous chamber.\nYour health is now " + str(health) + ".")
    print("The poison dealt " + str(poisondamage) + " damage.")
    poisondamage += 5

if health > 0:
    if "Regeneration Orb" in posessed_items:
        health += 30 * tea
        print("The orb glows...your health is now " + str(health) + ".")
    print("\nXentana screams a horrible sound and slowly dissapates. The \nacid in the chamber sinks lower, lower, \nlower, until it is but wispy dust. There is peace.")
else:
    exit(" Thwarted by the Wayward Wither, eh? Try a gas mask. Ha!")

#Upgrade between Boss 1 and stage 4
upgrade2B = input("\nYou may upgrade yourself now. Input 1 to gain an offensive passive ability, or 2 to gain a defense passive ability.")
if upgrade2B == "1":
    orbofdeath += 0.5
    print("You recieved the Orb of Death! Getting damaged by enemies will still progress you through a stage.")
if upgrade2B == "2":
    tea *= 2
    print("You drank some Soothing Tea! Healing effects you recieve will now be doubled.")    

#Fourth stage
stagemonsters = [witch, willowisp, ghoul, lightning, earthelemental]
killstage = 0

while health > 0 and killedmonster4 < 11:
    chosenmonsterA = random.randint(0, 4)
    possibledamage = stagemonsters[chosenmonsterA][2]
    print(stagemonsters[chosenmonsterA][1])
    chosenitemkey = input("What item do you use? ")
    
    #Chosen item checker
    chosenitem = itemcheck()
        
    #defeat checker & item property checker
    defeatcheck()
    killedmonster4 += killstage
    killstage = 0
    
if health > 0:
    if "Regeneration Orb" in posessed_items:
        health += (30 * tea)
        print("The orb glows...your health is now " + str(health) + ".")
    print("Stage 4 is complete.")
    cursetimer = 0
    poisontimer = 0
else:
    exit(" The magical monsters beat you! Try a spell shield! Oh. wait...you don't...")    
    
#Upgrade between stage 4 and stage 5

     
    
