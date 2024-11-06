# Once upon a time, on a way through the old wild mountainous west,…
# … a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

# Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

# How I crossed a mountainous desert the smart way.
# The directions given to the man are, for example, the following (depending on the language):

# ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
# or
# { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
# or
# [North, South, South, East, West, North, West]
# You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

# ["WEST"]
# or
# { "WEST" }
# or
# [West]
# Other examples:
# In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away.

# The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [] (nil in Clojure).

# In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

# Task
# Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

# Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
# if you want to translate, please ask before translating.

def dir_reduc(arr):
    """
    Reduces a list of directions by eliminating consecutive pairs of opposite directions.

    Args:
        arr (list of str): A list of directions, where each direction is one of 'NORTH', 'SOUTH', 'EAST', or 'WEST'.

    Returns:
        list of str: A reduced list of directions with all consecutive opposite direction pairs removed.

    Example:
        >>> dir_reduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST'])
        ['WEST']
        >>> dir_reduc(['NORTH', 'WEST', 'SOUTH', 'EAST'])
        ['NORTH', 'WEST', 'SOUTH', 'EAST']
    """
    # initialize dictionary of opposites
    opposites = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }
    # Initialize a list to store the reduced directions
    reduced = []
    # Iterate through the given directions
    for direction in arr:
        # If the reduced list is empty or the last direction in the reduced list is not the opposite of the current direction
        if not reduced or reduced[-1] != opposites[direction]:
            # Add the current direction to the reduced list
            reduced.append(direction)
        else:
            # Remove the last direction from the reduced list
            reduced.pop()
    return reduced

a=["NORTH", "WEST", "SOUTH", "EAST"]
print(dir_reduc(a)) # ["NORTH", "WEST", "SOUTH", "EAST"]

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"] # ['WEST']
print(dir_reduc(a)) # ['WEST']

a = ["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH","WEST", "EAST"] # ['NORTH', 'NORTH']
print(dir_reduc(a)) # ['NORTH', 'NORTH']

a = [] # []
print(dir_reduc(a)) # []

a=["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"] # []
print(dir_reduc(a)) # []

a = ["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","NORTH"] # ["NORTH"]
print(dir_reduc(a)) # ["NORTH"]

a = ["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"] # ["EAST", "NORTH"]
print(dir_reduc(a)) # ["EAST", "NORTH"]

a = ["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"] # ["NORTH", "EAST"])
print(dir_reduc(a)) # ["NORTH", "EAST"]

a = ["NORTH", "WEST", "SOUTH", "EAST"] # ["NORTH", "WEST", "SOUTH", "EAST"])
print(dir_reduc(a)) # ["NORTH", "WEST", "SOUTH", "EAST"]

a = ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH']
print(dir_reduc(a)) # ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH']
