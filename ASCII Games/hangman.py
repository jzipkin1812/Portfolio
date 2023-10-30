import random
import os

#Count lines in file
inFile = open(os.getcwd() + "Hangman.txt", "r")
ctr = 0 
for line in inFile:
	ctr += 1
selectword = random.randint(1, ctr)
inFile.close()

#Select line
inFile = open(os.getcwd() + "Hangman.txt", "r")
ctr = 0
for line in inFile:
	ctr += 1
	if ctr == selectword:
		selectword = line

#make it into a list, initialize
nolistword = selectword
#print(nolistword)
selectword = list(selectword)
if "\n" in selectword:
	selectword.remove("\n")
win = False
score = 0
tries = 9
#print how many chrs
for i in selectword:
	print("_", end = " ")
print("")

guessed = []
for i in selectword:
	guessed.append("_")
#Game loop
while win == False and tries > 0:
	guessright = False
	letter = input("Guess a letter: ")
	for let in selectword:
		if let == letter:
			guessright = True
			if guessed[selectword.index(let)] == "_":
				score += 1
			guessed[selectword.index(let)] = letter
			
			#loop for double letters
			if guessright == True:
				for contlet in range(selectword.index(let), len(selectword)):
					if selectword[contlet] == letter:
						if guessed[contlet] == "_":
							score += 1
						guessed[contlet] = letter
	#deplete tries
	if guessright == False:
		tries -= 1
		print(str(tries) + " tries left!")
	#print the word
	for e in guessed:
		print(e, end = " ")
	if score >= len(selectword):
		win = True
	
	print("")
if tries > 0:
	print("You win! The word was " + (nolistword.capitalize()) + ".")
else:
	print("You lose! The word was " + (nolistword.capitalize()) + ".")
