import string


def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    alphabets = string.ascii_lowercase
    for letter in lettersGuessed:
        if letter in alphabets:
            print(letter)
            alphabets = alphabets.replace(letter, '')
            print(alphabets)
    return alphabets


getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])
