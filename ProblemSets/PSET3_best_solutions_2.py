# # PS3-1
#
# return set(lettersGuessed) >= set(secretWord)
# return all(c in lettersGuessed for c in secretWord)
#
# # PS3-2
#
# return ''.join(c if c in lettersGuessed else '_' for c in secretWord)
# PS3-3
#
# return ''.join(sorted(set('abcdefghijklmnopqrstuvwxyz') - set(lettersGuessed)))
# return ''.join(c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in lettersGuessed)
# PS3-4
#
# def hangman(secretWord):
#     print("Welcome to the game, Hangman!")
#     print("I am thinking of a word that is", len(secretWord), "letters long.")
#     guesses, guessed = 8, []
#     while guesses > 0:
#         ltrs = getAvailableLetters(guessed)
#         print("---\n" "You have", guesses, "guesses left.\n")
#         guess = input("Available letters: " + ltrs + "\nPlease guess a letter: ")
#         if guess not in ltrs:
#             print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, guessed))
#         else:
#             guessed += [guess]
#             if guess in secretWord:
#                 print('Good guess:', getGuessedWord(secretWord, guessed))
#                 if isWordGuessed(secretWord, guessed):
#                     guesses = -2020
#             else:
#                 print("Oops! That letter is not in my word:", getGuessedWord(secretWord, guessed))
#                 guesses -= 1
#     print("---\n" "Congratulations, you won!") if guesses == -2020 else \
#     print("---\n" "Sorry, you ran out of guesses. The word was " + secretWord + ".")