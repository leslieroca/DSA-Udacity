"""
Finding the Square Root of an Integer

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:

"""


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    assert number >= 0, "negatives numbers do not have a square root"

    left, right = 0, number

    while left < right:
        mid = left + (right - left) // 2
        power = mid * mid
        power_next = (mid + 1) * (mid + 1)

        if power == number or (power < number and power_next > number):
            return mid

        if power > number:
            right = mid - 1
        else:
            left = mid + 1

    return left

# Test Cases.
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (123456789 == sqrt(15241578750190521)) else "Fail")

# Handling negative numbers test case.
try:
    sqrt(-9)
    print("Fail")
except AssertionError:
    print("Pass")

