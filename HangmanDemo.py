word = input("Type a word for someone to guess: ")

# Converts the word to lowercase
word = word.lower()

# Checks if only letters are present
if(word.isalpha() == False):
	print("That's not a word!")

secret_word = []
for letter in word:
	secret_word.append("_")

# Some useful variables
guesses = []
maxfails = 7

while (maxfails > 0):
	for letter in secret_word:
		print(letter)

	print("These are the letters you have already guessed:")
	print(guesses)

	print("You have ", maxfails, "tries left.")

	guess = input("Guess a letter: ")

	if (len(guess) == 1):
		#twoLetters = True
		#while(twoLetters):
		#	secret_word[word.index(guess)] = guess
			# remove letter from string.          word[word.index(guess)] = "-"
		#	if not (guess in word):
		#		twoLetters = False
		if (guess in word):
			print("Yes, that is in the word!")
			secret_word[word.index(guess)] = guess
		else:
			print("No, that is not in the word.")
			maxfails -= 1
			guesses.append(guess)
	else:
		maxfails -= 1
