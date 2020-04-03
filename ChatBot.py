from random import*
# --- Define your functions below! ---
birdSpecies = ["Peregrine Falcon", "Golden Eagle", "Red Tailed Hawk", "American Kestrel", "Bald Eagle"]
peregrine = ["the Peregrine Falcon is the fastest animal in the world!", "the Peregrine Falcon migrates hundreds of miles every year!", "the Peregrine Falcon is known for its signature 'mustache markings' on its face!"]
goldenEagle = ["the Golden Eagle is the most widley distributed raptor in the world!", "the Golden Eagle lives on every continent but Antarctica!", "the Golden Eagle is one of three American raptors that have feathers that extend to its talons!", "Despite its impressive size, the Golden Eagle does not hunt large animals, as it prefers smaller rodents!"]
redTailedHawk = ["there are approximatly 1 million Red Tailed Hawks in North America!", "the Red Tailed Hawk is commonly seen near highways!", "the Red Tailed Hawk is considered a buzzard!"]
kestrel = ["the American Kestrel is the smallest species of falcon in North America!", "the American Kestrel is the only raptor in North America that has differently colored males and females!", "like the Osprey, the American Kestrel hovers when it is hunting!"]
baldEagle = ["the Bald Eagle has scaley talons that it uses to catch slippery fish!", "the Bald Eagle is an oppurtunistic hunter, meaning it will hunt and consume nearly everything, including roadkill!", "the Bald Eagle is the national animal of the United States of America!"]

validInputPositive = ["yes", "yeah", "yup", "yea", "okay", "ok", "sure"]
validInputNegative = ["no", "nope"]

def chatBotIntroduction():
    print("Hello, my name is Birdie.")
    name = input("What is your name? ")
    print("Nice to meet you, ", name)
    print("I know a lot about birds!")

def isValidInput(answer, answerList):
    if(answer in answerList):
        return True

def whatBird():
    validInput = False
    while(validInput == False):
        randomBird = randint(0, len(birdSpecies)-1)
        print("I would like to tell you a fact about the ", birdSpecies[randomBird])
        answer = input("Would you like to learn about this bird? ")
        if(isValidInput(answer, validInputPositive)):
            print("Great!")
            return randomBird

        if(isValidInput(answer, validInputNegative)):
            print("Okay, I will pick a different bird.")
            validInput = False

        elif not(isValidInput(answer, validInputPositive)) & (isValidInput(answer, validInputNegative)):
            print("That is not a valid input")
            validInput = False


def birdFact(randomBird):
    randomPeregrineFact = randint(0, len(peregrine)-1)
    randomGoldenEagleFact = randint(0, len(goldenEagle)-1)
    randomRedTailedHawkFact = randint(0, len(redTailedHawk)-1)
    randomKestrelFact = randint(0, len(kestrel)-1)
    randomBaldEagleFact = randint(0, len(baldEagle)-1)

    if(randomBird == 0):
        print("Did you know that ", peregrine[randomPeregrineFact])

    if(randomBird == 1):
        print("Did you know that ", goldenEagle[randomGoldenEagleFact])

    if(randomBird == 2):
        print("Did you know that ", redTailedHawk[randomRedTailedHawkFact])

    if(randomBird == 3):
        print("Did you know that ", kestrel[randomKestrelFact])

    if(randomBird == 4):
        print("Did you know that ", baldEagle[randomBaldEagleFact])




#def processInput(answer):
#    if answer == "hi":
#        say_greeting()
#    else:
#        say_default()
#
#def say_greeting():
#    print("What's up?")
#
#def say_default():
#    print("That's cool!")



# --- Put your main program below! ---
def main():
    chatBotIntroduction()
    while(True):
        birdSpecies = whatBird()
        birdFact(birdSpecies)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
