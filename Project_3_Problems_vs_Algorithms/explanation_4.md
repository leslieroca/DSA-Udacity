Explanation:
Doing only one traversal over the list I set 3 pointers: front(starts with value 0 representing index 0, increases its value
by 1 every time a 0 is found and switched to its current position or if the value on its position is equal to 0),
runner(starts at the beginning of the list and will traverse the list looking for 0s and 2s to switch with the front and
back sorting the list values), back(starts with value equal to the length of the list and will decrease by 1 every time
a 2 is found by the runner and switched positions or if the value on its current position is already 2), that way the
values 0s will be switched to the front of the list, the 2s to the back making the 1s remain in the middle.


Complexity:
The time complexity is O(n) where n is the number of element in the list, we have to iterate over the complete list.
The space complexity is O(1), we don't use any extra memory.