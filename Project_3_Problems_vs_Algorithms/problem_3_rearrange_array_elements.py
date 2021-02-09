"""
Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is maximum.
Return these two numbers. You can assume that all array elements are in the range [0, 9].
The number of digits in both the numbers cannot differ by more than 1.
You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there
are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
"""


def heapify(list):
    for i in range(1, len(list)):
        # Move up list[i] until the heap invariant is satisfied.
        j = i
        while j > 0:
            parent_index = j // 2 if j % 2 == 1 else (j - 1) // 2
            # if parent's value is smaller than the node's value, then the heap invariant is already satisfied.
            if list[parent_index] <= list[j]:
                break
            else:
                list[j], list[parent_index] = list[parent_index], list[j]
                j = parent_index


def heappop(list):
    assert list, "list cannot be None or empty"

    popped = list[0]
    list[0] = list[len(list) - 1]
    list.pop()
    i = 0
    while i * 2 + 1 < len(list):
        # Makes the left child the default as it's guaranteed that it exists.
        child_to_compare_index = i * 2 + 1
        # If a right child exists, compare it's value with the left child's value, if smaller then use the right
        # child index.
        if (i * 2 + 2 < len(list)):
            if list[i * 2 + 2] < list[child_to_compare_index]:
                child_to_compare_index = i * 2 + 2
        # Compare the parent's value with the smallest of its child values.
        if list[i] <= list[child_to_compare_index]:
            # If parent's value is smaller or equal then there's no need for further arrangement as the heap invariant
            # is already satisfied.
            break
        else:
            # If child's value is smaller than parent's value then swap their positions and continue the process
            # until the heap invariant is satisfied.
            list[i], list[child_to_compare_index] = list[child_to_compare_index], list[i]
            i = child_to_compare_index

    return popped


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    assert input_list, "list cannot be None or empty"
    assert len(input_list) > 1, "list needs to have at least two elements so we can form the two numbers"

    heapify(input_list)
    a, b, pow_10 = 0, 0, 1
    while input_list:
        a += (heappop(input_list) * pow_10)
        if input_list:
            b += (heappop(input_list) * pow_10)
        pow_10 *= 10
    return (a, b)




def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 2], [1, 2]])
test_function([[0, 0], [0, 0]])

try:
    rearrange_digits([])
    print("Fail")
except AssertionError:
    print("Pass")

try:
    rearrange_digits([1])
    print("Fail")
except AssertionError:
    print("Pass")








