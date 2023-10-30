import math
import random
print("Welcome to upgrade wars! Player 1's turn.\n")
#variables for resources
#Player 1
player1 = {
    "health" : 600,
    "maxhealth" : 750,
    "mana" : 300,
    "manamax" : 300,
    "energy" : 400,
    "energymax" : 400,
    "upgrades" : [],
    "weakenmod" : 1,
    "xType" : "",
    "reX" : 0,
        
}

#Player 2
player2 = {
    "health" : 600,
    "maxhealth" : 750,
    "mana" : 300,
    "manamax" : 300,
    "energy" : 400,
    "energymax" : 400,
    "upgrades" : [],
    "weakenmod" : 1,
    "xType" : "",
    "reX" : 0,

}
abilitynames1 = {

}
abilitynames2 = {

}
#Convenience functions
def downToMax():
    global player1, player2
    if player1["mana"] > player1["manamax"]:
        player1["mana"] = player1["manamax"]
    if player1["energy"] > player1["energymax"]:
        player1["energy"] = player1["energymax"]
    if player1["health"] > player1["maxhealth"]:
        player1["health"] = player1["maxhealth"]    

    if player2["mana"] > player2["manamax"]:
        player2["mana"] = player2["manamax"]
    if player2["energy"] > player2["energymax"]:
        player2["energy"] = player2["energymax"]
    if player2["health"] > player2["maxhealth"]:
        player2["health"] = player2["maxhealth"]
def error(resource):
    print("Not enough " + resource + ".")
def userPlayer(num):
    if num == 1:
        return(player1)
    else:
        return(player2)
def opponentPlayer(num):
    if num == 2:
        return(player1)
    else:
        return(player2)
def userAb(num):
    if num == 1:
        return(abilitynames1)
    else:
        return(abilitynames2)
def opponentAb(num):
    if num == 2:
        return(abilitynames1)
    else:
        return(abilitynames2)
def displayStats(player = 0):
    global player1, player2
    print("\nPlayer 1 has " + str(player1["health"]) + " health and " + str(player1["mana"]) + " mana.\nPlayer 2 has " + str(player2["health"]) + " health and " + str(player2["mana"]) + " mana.\n")
def displayEnergy(player = 0):
    global player1, player2
    print("Player 1 has " + str(player1["energy"]) + " energy.\nPlayer 2 has " + str(player2["energy"]) + " energy.\n")
def damage(player, amount, resource = "health"):
    global player1, player2
    if resource == "health":
        opponentPlayer(player)[resource] -= (amount * opponentPlayer(player)["weakenmod"])
        if opponentPlayer(player)["xType"] == "zeal":
            opponentPlayer(player)["reX"] = int(opponentPlayer(player)["reX"] + amount * 0.3)
    else:
        opponentPlayer(player)[resource] -= (amount)
def heal(player, amount):
    global player1, player2
    userPlayer(player)["health"] += (amount)
def cost(player, amount, resource = "mana"):
    global player1, player2
    if userPlayer(player)[resource] >= amount:
        userPlayer(player)[resource] -= amount
        return True
    else:
        error(resource)
        return False
def statx(player = 0):
    global player1, player2
    if userPlayer(player)["xType"] != "":
        print("Player " + str(player) + " has " + str(userPlayer(player)["reX"]) + " " + str(userPlayer(player)["xType"]) + ".")

#defining ability functions
def unleashZeal(player):
    global player1, player2
    if cost(player, 100, "mana") and userPlayer(player)["xType"] == "zeal":
        print("Player " + str(player) + " used Unleash Zeal!")
        heal(player, userPlayer(player)["reX"])
        userPlayer(player)["reX"] = 0
def slash(player):
    global player1, player2
    if cost(player, 100, "mana"):
        damage(player, 50)
        print("Player " + str(player) + " used Slash!")
        downToMax()

def restore(player):
    global player1, player2
    if cost(player, 150, "mana"):
        heal(player, 50)
        print("Player " + str(player) + " used Restore!")
        downToMax()

def righteousHammer(player):
    global player1, player2
    if cost(player, 100, "mana"):

        #damage
        damage(player, userPlayer(player)["dmg56"])

        #mana damage
        opponentPlayer(player)["mana"] -= userPlayer(player)["manadmg56"]

        #heal for mana
        heal(player, ( userPlayer(player)["manadmg56"] * userPlayer(player)["healthsteal56"] ))
        print("Player " + str(player) + " used Righteous Hammer!")
        downToMax()
        
#Abilities owned by each player
abilitynames1 = {
    "slash" : slash,
    "stats" : displayStats,
    "energy" : displayEnergy,
    "restore" : restore,
    "statx" : statx,
}

abilitynames2 = {
    "slash" : slash,
    "stats" : displayStats,
    "energy" : displayEnergy,
    "restore" : restore,
    "statx" : statx,
}

#Upgrade functions
def meditation(player):
    global player1, player2
    if cost(player, 25, "energy"):
        userPlayer(player)["xType"] = "zeal"
        userPlayer(player)["reX"] = 0

def healingPotion(player):
    global player1, player2
    if cost(player, 200, "energy"):
        userPlayer(player)["maxhealth"] += 200
        userPlayer(player)["health"] += 200
        print(str(player) + " USED A HEALING POTIONNNNNNNNNNNNNNNNNNNNNNNNNN")

def righteousHammerAdd(player):
    global player1, player2, abilitynames1, abilitynames2
    if cost(player, 50, "energy"):
        userAb(player)["righteous hammer"] = righteousHammer
        userPlayer(player)["dmg56"] = 25
        userPlayer(player)["manadmg56"] = 25
        userPlayer(player)["healthsteal56"] = 0

def goldenFoundry(player):
    global player1, player2, abilitynames1, abilitynames2
    if cost(player, 100, "energy") and 56 in userPlayer(player)["upgrades"]:
        userPlayer(player)["dmg56"] += 50

def brandOfSunlight(player):
    global player1, player2, abilitynames1, abilitynames2
    if cost(player, 150, "energy") and 56 in userPlayer(player)["upgrades"] and not(59 in userPlayer(player)["upgrades"]):
        userPlayer(player)["healthsteal56"] = 1.2

def unleashZealAdd(player):
    global player1, player2, abilitynames1, abilitynames2
    if cost(player, 25, "energy") and userPlayer(player)["xType"] == "zeal":
        userAb(player)["unleash zeal"] = unleashZeal
ups = {
    1 : healingPotion,
    56 : righteousHammerAdd,
    57 : goldenFoundry,
    58 : brandOfSunlight,
    16 : meditation,
    17 : unleashZealAdd
}

#phases
def upgrade_phase(player):
    global player1, player2, ups
    upnum = ""

    while (upnum.lower()) != "end": 
        try:
            upnum = input("What number upgrade will you buy? You have " + str(userPlayer(player)["energy"]) + " energy left. ")
            while (upnum.lower()) != "end":
                if not(int(upnum) in userPlayer(player)["upgrades"]): 
                    ups[int(upnum)](player)
                    userPlayer(player)["upgrades"].append(int(upnum))
                upnum = input("What number upgrade will you buy? You have " + str(userPlayer(player)["energy"]) + " energy left. ")
        except:
            print("That's not a valid input.")
def main_turn(player):
    global player1, player2, abilitynames1, abilitynames2
        
    ability = (input("Player " + str(player) + "'s turn. Select an ability, END to move on: ").lower())
    while ability != "end":
        for i in userAb(player):
            if i == ability:
                userAb(player)[i](player)
        ability = (input("Player " + str(player) + "'s turn. Select an ability, END to move on: ").lower())


def regeneration_phase(player):
    global player1, player2
    userPlayer(player)["mana"] += 150
    userPlayer(player)["energy"] += 75
    if userPlayer(player)["mana"] > userPlayer(player)["manamax"]:
        userPlayer(player)["mana"] = userPlayer(player)["manamax"]
    if userPlayer(player)["energy"] > userPlayer(player)["energymax"]:
        userPlayer(player)["energy"] = userPlayer(player)["energymax"]
    downToMax()
    displayStats()
    displayEnergy()

def level_up(player):
    global player1, player2
    if player == 1:
        player1["energymax"] += 25
        print("Player 1's max energy increased by 25! Level up!")
    elif player == 2:
        player2["energymax"] += 25
        print("Player 2's max energy increased by 25! Level up!")

def clear(player):
    global player1, player2
    userPlayer(player)["weakenmod"] = 1
    print("End of player " + str(player) + "s turn.\n")
    
#Main loop
while True:
    for i in [1, 2]:
        upgrade_phase(i)
        main_turn(i)
        regeneration_phase(i)
        level_up(i)
        clear(i)

    if opponentPlayer(1)["health"] <= 0:
        print("Player " + str(1) + " wins")
        break 

    if opponentPlayer(2)["health"] <= 0:
        print("Player " + str(2) + " wins")
        break 
