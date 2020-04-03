word = input("Type a word for someone to guess: ")

# Converts the word to lowercase
word = word.lower()

# Checks if only letters are present
if(word.isalpha() == False):
	print("That's not a word!")


# Some useful variables
guess = []
maxfails = 7
validGuess = False

while(validGuess == False):
	for i in range(len(word)):
		print("_")

	guess = input("Guess a letter: ")
	if(word.isalpha() == True):
		validGuess = True

	elif(word.isalpha() == False):
		validGuess = False

while(maxfails > 0):
	if(guess in word == True):
		print("You are correct!")

		maxfails -= 1

	if(guess in word == False):
		print("You are incorrect!")
		maxfails -= 1

#	elif(word.isalpha() == False):
#		validGuess = False

if(maxfails == 0):
	print("You did not guess the word. The word was: " + word + "Try again!")
