# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

from collections import Counter

def find_uniq(arr):
    """
    Finds the unique number in an array where all numbers except one occur more than once.

    Args:
        arr (list): A list of numbers where all numbers except one occur more than once.

    Returns:
        int/float: The unique number that occurs only once in the array.
    """
    counts = Counter(arr)
    for k,v in counts.items():
        if v==1:
            return k

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
print(find_uniq([ 3, 10, 3, 3, 3 ]))
