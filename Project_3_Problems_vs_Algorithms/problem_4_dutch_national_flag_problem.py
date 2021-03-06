"""
Dutch National Flag Problem

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any
sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be
an O(n) solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:
"""

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    front, runner, back  = 0, 0, len(input_list)

    while runner < back:

        if input_list[runner] == 0:
            # Swap elements to keep 0 at the front of the input_list.
            input_list[runner], input_list[front] = input_list[front], 0
            runner += 1
            front += 1

        elif input_list[runner] == 1:
            runner += 1

        else:    # input_list[runner] == 2
            # Swap elements to keep 2 at the back of the input_list.
            input_list[runner], input_list[back -1] = input_list[back -1], 2
            back -= 1


    return input_list





def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")

    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([1, 2, 0])
test_function([2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
# Even works for this cases
test_function([2, 2, 2, 1, 1, 1, 1])
test_function([1, 1, 0, 0, 0, 1])
test_function([2, 2, 0, 0, 2, 2])

