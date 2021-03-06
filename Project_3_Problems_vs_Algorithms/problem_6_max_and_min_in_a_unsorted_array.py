"""
Max and Min in a Unsorted Array

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run
in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?

"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) == 0:
        return ()

    smallest, largest = float('inf'), float('-inf')
    for e in ints:
        if e < smallest:
            smallest = e
        if e > largest:
            largest = e
    return (smallest, largest)



## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
print ("Pass" if (() == get_min_max([])) else "Fail")


l_2 = [i for i in range(0, 10001)]  # a list containing 0 - 10000
random.shuffle(l_2)
print ("Pass" if ((0, 10000) == get_min_max(l_2)) else "Fail")


print ("Pass" if ((0, 0) == get_min_max([0,0,0,0,0,0,0])) else "Fail")
print ("Pass" if ((1, 1) == get_min_max([1,1,1,1,1])) else "Fail")
print ("Pass" if ((False, True) == get_min_max([True, False])) else "Fail")  # True is equal to 1 and False to 0.


# Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)? YES!
