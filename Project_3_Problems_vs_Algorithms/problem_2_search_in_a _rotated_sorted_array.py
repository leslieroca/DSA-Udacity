"""
Search in a Rotated Sorted Array

You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with:
"""

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    n = len(input_list)

    # If list is empty the target won't be found.
    if n == 0:
        return -1

    def max_element_index():
        # Search for the position where the initial part of the list stop increasing

        # If the list has only one element then the max element index is 0 which is the first element.
        if n == 1:
            return 0

        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if input_list[mid] > input_list[(mid + 1) % n]:
                return mid
            if input_list[mid] < input_list[0]:
                right = mid - 1
            else:
                left = mid + 1

    def binary_search_subarray(from_, to):
        left, right = from_, to
        while left <= right:
            mid = left + (right - left) // 2
            if input_list[mid] == number:
                return mid
            if input_list[mid] < number:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    max_index = max_element_index()
    if input_list[0] <= number <= input_list[max_index]:
        return binary_search_subarray(0, max_index)

    return binary_search_subarray(max_index + 1, n - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 1])
test_function([[1], 1])
test_function([[1], 2])
test_function([[1, 2], 1])
test_function([[2, 1], 1])
test_function([[1, 2], 3])
test_function([[2, 1], 3])

