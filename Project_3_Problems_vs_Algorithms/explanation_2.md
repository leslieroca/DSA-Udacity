Explanation:
I realized that starting from the beginning (position 0) the next values will be bigger than the first until it
reaches the max value in the list, and then the next values will be smaller that the first element, with this scenario
we could use binary search to find the index of the maximum value in the list, if the value is bigger than the first
value we move to the right part, if the value is smaller we move to the left part.

Once, we have the index of the maximum value, then we could partition the array in two sorted sub-arrays and perform the
traditional binary search two find the target


Complexity:
Time Complexity is O(log n) where n is the length of the list.

Each call uses O(1) space, the maximum depth of the recursive tree is O(log n), so the space complexity is O(logn)

