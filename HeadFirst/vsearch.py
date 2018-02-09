def search4vowels(word:str) -> set:
    """Return any vowels found in the word"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(phrase: str, letters: str) -> set:
    ''' This function finds the letters in the string passed '''
    return set(letters).intersection(set(phrase))
