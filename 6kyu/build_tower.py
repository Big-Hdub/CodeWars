# Build Tower
# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.
# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]

def tower_builder(n):
    # return [f"{' ' * (n - i - 1)}{'*' * (2 * i + 1)}{' ' * (n - i - 1)}" for i in range(n)]
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

print(tower_builder(3)) # ["  *  ", " *** ", "*****"]
