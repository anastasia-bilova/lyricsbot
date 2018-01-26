"""
Custom implementation of built-in Python method.
"""


def join(sequence, separator):
    """
    Return a string which is the concatenation of the strings in iterable.
    With separator between elements.
    """
    string = ''

    for letter in sequence:
        string += letter + separator

    if separator == '':
        return string

    return string[:-1]


def split(string, separator):
    """
    Return a list of the words in the string, using separator as the delimiter string.
    """

    if separator == '':
        raise ValueError('Empty separator')

    if separator is None:
        separator = ' '

    sequence, word = [], ''
    string += separator
    for letter in string:
        if letter is not separator:
            word += letter
        else:
            sequence.append(word)
            word = ''

    return sequence
