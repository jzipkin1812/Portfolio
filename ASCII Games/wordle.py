import random

#Count lines in file
inFile = open("wordle.txt", "r")
ctr = 0
for line in inFile:
	ctr += 1
selectword = random.randint(1, ctr)
inFile.close()

#Select line
inFile = open("wordle.txt", "r")
ctr = 0
for line in inFile:
	ctr += 1
	if ctr == selectword:
		selectword = line[0 : 5]

guessed = "      "
win = False
score = 0
tries = 6
while guessed != selectword:
	for i in range(len(guessed)):
		if selectword[i] == guessed[i]:
			print(selectword[i], end = " ")
		elif guessed[i] in selectword:
			print("*", end = " ")
		else:
			print("_", end = " ")
	guessed = input("\nEnter your guess: ")
