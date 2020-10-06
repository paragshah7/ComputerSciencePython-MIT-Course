def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """

    newWord = ''
    for word in secretWord:
        if word in lettersGuessed:
            newWord += word
        else:
            newWord += '_ '
    print(newWord)
    return newWord


getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])