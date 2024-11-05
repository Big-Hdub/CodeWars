# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or
# more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will
# be included only when more than one word is present.

# Examples:

# "Hey fellow warriors"  --> "Hey wollef sroirraw"
# "This is a test        --> "This is a test"
# "This is another test" --> "This is rehtona test"

def spin_words(sentence):
    """
    This function takes in a sentence as a string and returns a new sentence where
    words with five or more letters are reversed, while words with less than five
    letters remain unchanged.

    Args:
        sentence (str): The input sentence containing words separated by spaces.

    Returns:
        str: A new sentence with words of five or more letters reversed.

    Example:
        >>> spin_words("Hey fellow warriors")
        'Hey wollef sroirraw'
    """
    return " ".join([word if len(word) < 5 else word[::-1] for word in sentence.split()])
