# Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the
# string is valid, and false if it's invalid.

# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

# What is considered Valid?
# A string of braces is considered valid if all braces are matched with the correct brace.

# Examples
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False

def valid_braces(string):
    """
    This function takes in a string of braces and determines if the order of the braces is valid. It returns True if the string
    is valid and False if it is invalid.

    Args:
        string (str): A string of braces containing parentheses, brackets, and curly braces.

    Returns:
        bool: True if the string is valid, False if it is invalid.

    Example:
        >>> valid_braces("(){}[]")
        True
        >>> valid_braces("([{}])")
        True
        >>> valid_braces("(}")
        False
        >>> valid_braces("[(])")
        False
        >>> valid_braces("[({})](]")
        False
    """
    stack = []
    for brace in string:
        if brace in '([{':
            stack.append(brace)
        else:
            if not stack:
                return False
            if stack[-1] == '(' and brace == ')' or stack[-1] == '[' and brace == ']' or stack[-1] == '{' and brace == '}':
                stack.pop()
            else:
                return False
    return not stack
