import unittest

# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

def disemvowel(string_):
    """
    Remove all vowels from the input string.

    Parameters:
    string_ (str): The input string from which vowels will be removed.

    Returns:
    str: A new string with all vowels removed.
    """
    return ''.join(char for char in string_ if char.lower() not in 'aeiou')
