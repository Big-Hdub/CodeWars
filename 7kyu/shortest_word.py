# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

from numpy import short


def find_short(s):
    """
    Finds the length of the shortest word in a given string.

    Args:
        s (str): A string containing multiple words separated by spaces.

    Returns:
        int: The length of the shortest word in the string.
    """
    # words = s.split()
    # shortest_length = len(words[0])
    # for i in range(1, len(words)):
    #     if len(words[i]) < shortest_length:
    #         shortest_length = len(words[i])
    # return shortest_length # l: shortest word length
    return min(len(word) for word in s.split())
