# Museum Maze
# Period 1
# Javin Zipkin
import sys
print("Welcome to the Belmont Maze Museum. Find the exit and escape.\nYou may move in cardinal directions or input interact to interact with your surroundings.\nIn specific cases, you may be able to input secret actions such as codes.")
print("Examples of valid input: \neast \nwest \nnorth \nsouth \ninteract \n[insert your secret code here]")
print("Finally, Zoom out codeskulptor to 100% or 90%! \nAnything larger will obscure text.")

currentlocation = [3, 1] # [East/West, North/South]
money = 0
moneyleft = True
greengem = False
earthtotem = False

#Each room has its location, valid movements, and display text
planetarium3 = [[1, 1], ["east", "north", "interact"], "\nIn this final room of the Planetarium, models of comets \nand other objects are shown. There's a model asteroid circling the room."]
giftshop = [[2, 1], ["east", "interact"], "\nYou've arrived in the gift shop! Small gizmos and \nwondorous books line every shelf."]
enterance = [[3, 1], ["west", "east", "north", "south"], "\nYou find yourself in the museum's enterance."]
galleryA = [[4, 1], ["west", "east", "north"], "\nA gallery full of sculptures surrounds you. Some are made of clay,\nsome wood, some glass, and one is made of toothpicks!"]
helpdesk = [[5, 1], ["west", "interact", "north"], "\nA sign above reads \"INFORMATION\". There's also a small desk."]
galleryB = [[3, 2], ["west", "east", "south", "north"], "\nA gallery full of cubist art surrounds you. \nPuzzling pastel paintings amaze and confuse you."]
planetarium2 = [[1, 2], ["south", "north"], "\nThis room contains a rotating model of Jupiter, complete with a holographic storm. Wow!"]
planetarium1 = [[1, 3], ["east", "south", "interact"], "\nYou come to the enterance of the Planetarium. In this first room, \na model of Earth is shown as well as a map of constellations."]
ticketzone = [[2, 2], ["north", "east", "interact"], "\nA large banner reads TICKET ZONE above. \nThere is a machine you can use to buy tickets to special exhibits."]
mainhall = [[2, 3], ["north", "south", "interact", "east"], "\nYou arrive in the main hall of the museum. \nThere is a directory and beautiful marble pillairs."]
atm = [[4, 2], ["west", "south", "east", "north", "interact"], "\nYou come to a small room with an ATM and not much else."]
egyptGate = [[2, 4], ["south", "interact"], "\nA large sphinx sculpture is here. There's no place to insert a ticket, \nbut there's a door and a small slot for something smooth and round."]
egypt1 = [[1, 4], ["east", "north"], "\nYou come to a dimly lit tomb. Models of mummified cats \nrest in the corners. It seems no one's been here in a long time..."]
egypt2 = [[1, 5], ["east", "south", "interact"], "\nYou can now see the exit of the tomb. Light shines through \na door to the east. There's also a golden scarcophagus."]
egypt3 = [[2, 5], ["south", "west"], "\nThe stairs leading out of the tomb lead you to the top \nof the sphinx sculpture! You can slide down it by moving south. "]
galleryc = [[4, 3], ["south"], "\nThis gallery is a display of human evolution. \nPosters with different iterations of our species line the wall."]
galleryd = [[5, 2], ["south", "west"], "\nThis dark gallery is full of soothing lights. Rainbows of mixing color amaze you. \nYou've never seen such beauty in simple color before..."]
exitT = [[3, 5], ["east", "interact", "north"], "\nCongratulations, it's the exit of the museum! A golden \ntrophy rests on the podium for you to claim."]                                                                                                               
jungle1 = [[3, 3], ["south"], "\nYou come to the enterance of the Rainforest exhibit. \nIt's suddenly really humid, and a butterfly lands on your shoulder."]
jungle2 = [[3, 4], ["south", "east"], "\nIn this room, a scarlet macaw perches on a branch. Fire ants crawl on a rock below."]
jungle3 = [[4, 4], ["west", "north"], "\nThis room has a zipline in it! Amazing! You can fly above a man-made waterfall."]
jungle4 = [[4, 5], ["south", "interact"], "\nYou can see the door to the exit of the museum to the west! \n...It's locked. All there is in this room is a strange totem."]


allrooms = [jungle1, jungle2, jungle3, jungle4, exitT, galleryd, galleryc, egypt3, egypt2, egyptGate, egypt1, atm, enterance, galleryA, planetarium3, giftshop, helpdesk, galleryB, planetarium1, planetarium2, ticketzone, mainhall]

#Interact with Rooms definition
def interact(currentroom):
    global money
    global moneyleft
    global planetarium1
    global greengem
    global earthtotem
    
    if currentroom == helpdesk:
        print("You ask for help, but no one's at the desk...You see a safe, though. It has a number combo lock.")
    
    elif currentroom == giftshop:
        if earthtotem == False:
            print("Nothing here is useful except for one thing. The Exit Key! A clerk at the counter says \nyou can have it if you exchange it for an Earth Totem. Whatever that means.")
        else:
            earthtotem = False
            print("You exchange your earth totem for an Exit Key! \nOnly one more thing left to do- find the exit!")
            jungle4[1].append("west")
    
    elif currentroom == atm:
        if moneyleft == True:
            print("You got a few bucks from the ATM.")
            money += 5
            print("Your money is now $" + str(money))
            moneyleft = False
        else:
            print("There's no money left in your account.")
    
    elif currentroom == mainhall:
        print("\nYou look at the directory. It says:\nPLANETARIUM: WEST \nANCIENT EGYPT GALLERY: NORTH WEST \nGIFT SHOP: SOUTH")
    
    elif currentroom == ticketzone:
        if money >= 5:
            choice = input("Input 1 to buy a Planetarium Ticket and input 2 to buy a Rainforest Ticket.")
            if choice == "1":
                print("You bought a Planetarium ticket for 5 dollars.")
                money -= 5
                mainhall[1].append("west")

            elif choice == "2":
                if money >= 10:
                    print("You bought a Rainforest ticket for 10 dollars.")
                    money -= 10
                    jungle1[1].append("north")
                else:
                    print("Sorry, not enough money.")
            else:
                print("Invalid input.")
        else:
            print("...But you don't have enough cash to buy anything.")
        
    elif currentroom == planetarium1:
        print("\nYou look closely at the constellations.  There are five shown. \nThe first constellation has 5 stars. \nThe next has 8, then 11, then 9, then 9.")
    
    elif currentroom == planetarium3:
        print("You look closely at the asteroid model. It moves in an ELIPSE.")
    
    elif currentroom == egyptGate:
        if greengem == True:
            print("You slide your gem into the slot and the door opens. You may now enter the maw of the sphinx.")
            egyptGate[1].append("west")
            greengem = False
        else:
            print("There's nothing to do...")
    
    elif currentroom == egypt2:
        print("The sarcophagus's eyes glow. A voice in your head screams... \"THE SACRED SHAPE IS THE KEY!\"")
        password = input("What is the sacred shape?")
        if (password.lower()) == "elipse":
            money += 10
            print("The sarcophagus opens. You find riches inside. You now have 10 more dollars.")
        else:
            print("The voice in your head screams once more... \n\"SHAME! THE SACRED SHAPE WAS NOT UTTERED FROM YOUR USELESS TONGUE.\"")
    
    elif currentroom == jungle4:
        earthtotem = True
        print("With incredible force, you wrench the totem from the ground. It's yours, for now.")

#'Which room am I in?' function definition
def findMyRoom(currentlocation):
    for room in allrooms:
        if room[0] == currentlocation:
            print(room[2])
            return room

#MoveToRoom function definition
def moveToRoom(currentlocation, currentroom):
    global greengem
    proposedlocation = currentlocation
    moveinput = input("Would you like to move east west north or south or interact?")
    if (moveinput.lower()) == "west" and (moveinput.lower()) in currentroom[1]:
        proposedlocation[0] -= 1
    elif (moveinput.lower()) == "east" and (moveinput.lower()) in currentroom[1]:
        proposedlocation[0] += 1
    elif (moveinput.lower()) == "north" and (moveinput.lower()) in currentroom[1]:
        proposedlocation[1] += 1
    elif (moveinput.lower()) == "south" and (moveinput.lower()) in currentroom[1]:
        proposedlocation[1] -= 1
    elif (moveinput.lower()) == "interact" and (moveinput.lower()) in currentroom[1]:
        interact(currentroom)
        
    if (moveinput.lower()) in currentroom[1]:
        return proposedlocation
    elif (moveinput.lower()) == "581199" and currentroom == helpdesk and greengem == False:
        print("The safe cracks open. A smooth green gem is found inside. You take it.")
        greengem = True
        return currentlocation
    else:
        if (moveinput.lower()) != 'interact':
            print("You can't go that way.")
        else:
            print("You can't interact with this room.")
        return currentlocation
    

#Full game loop
while currentlocation != [3, 0] and currentlocation != [3, 6]:
    currentroom = findMyRoom(currentlocation)
    currentlocation = moveToRoom(currentlocation, currentroom)
print("You exited the museum. Thanks for playing!")