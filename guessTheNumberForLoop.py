#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

for guesses in range(3):
	guess = input("Guess a number between 1 and 20 (inclusive): ")
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!")
	else:
		guess = int(guess) # converts a string to an integer

	if guesses == 3 & guess != aRandomNumber:
		print("You ran out of guesses!")
		break
	if guess == aRandomNumber:
		print("Great guess! You have guessed my number!")
		break
	if guess < aRandomNumber:
		print("My secret number is greater than your guess")
	elif guess > aRandomNumber:
		print("My secret number is less than your guess")
