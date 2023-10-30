import random

#improved input
def myInput(message):
    userInput = input(message)
    if userInput.isdigit():
        return(int(userInput))
    else:
        return(userInput.lower())
#intro
print("Welcome to the Egg Drop Heist!")
print("To learn this game's rules visit https://www.youtube.com/watch?v=NGtt7GJ1uiM")

status = "undecided"
towerHeight = 100
testEggs = 8
timestested = 0
bestFloor = random.randint(1, towerHeight)

print("Tower height: " + str(towerHeight) + " Eggs left: " + str(testEggs) + "\n")
print("To make your final guess, input Final.")

while (status != "win") and (status != "lose"):
    if testEggs > 0:
        testFloor = myInput("What floor to test? You have tested " + str(timestested) + " times. ")
    
    if testFloor == "final" or testEggs < 1:
        #do a final guess
        if testFloor == "final":
            final = myInput("What is the best floor? ")
        else:
            final = myInput("It broke, no eggs left! What is the best floor? ")
        if final == bestFloor:
            status = "win"
        else:
            status = "lose"

    elif (str(testFloor).isdigit()) and testFloor <= towerHeight:
        #do a normal guess
        if testFloor > bestFloor:
            testEggs -= 1
            print("The egg broke! Eggs left: " + str(testEggs))
            timestested += 1
        else:
            print("It didn't break!")
            timestested += 1
    else:
        print("Invalid input.")

#ending
if status == "win":
    print("You found the best floor and escaped with the prized egg! Yay!")
    print("Times tested: " + str(timestested))
else:
    print("Oh, no! Wrong answer! The best floor was " + str(bestFloor) + ".")
