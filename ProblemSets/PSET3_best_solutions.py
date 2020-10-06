# p1:

def isWordGuessed(secretWord, lettersGuessed):
    # return set(secretWord) == set(c for c in lettersGuessed if c in secretWord)
    return all (c in lettersGuessed for c in secretWord)
# p2:

def getGuessedWord(secretWord, lettersGuessed):
    return "".join(c if c in lettersGuessed else "_ " for c in secretWord)
# p3:

from string import ascii_lowercase

def getAvailableLetters(lettersGuessed):
    return "".join(sorted(set(ascii_lowercase) - set(lettersGuessed)))
    # return "".join(c for c in ascii_lowercase if c not in lettersGuessed)
# p4:

def hangman(secretWord):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    print("-" * 80)

    guesses = 8
    guessed = list()

    while guesses:

        print("You have {} guesses left.".format(guesses))
        print("Available letters: {}".format(getAvailableLetters(guessed)))
        choice = input("Please guess a letter: ").lower()

        if choice in set(guessed):
            print("Oops! You've already guessed that letter: ", end="")
        elif choice not in secretWord:
            print("Oops! That letter is not in my word: ", end="")
            guesses -= 1
        else:
            print("Good guess: ", end="")

        guessed.append(choice)
        print(getGuessedWord(secretWord, guessed))
        print("-" * 80)

        if isWordGuessed(secretWord, guessed):
            print("Congratulations, you won!")
            break

    else:
        print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))