"LRU Cache"

Explanation:

To design the Least Recently Used (LRU) Cache data structure, and keep the constant runtime while setting, getting
and also deleting the least recently used entries to set new ones when the cache was at its full capacity, I made use
of the data structure doubly LinkedList synchronized with a dictionary, on the LinkedList I kept the order of the
data usage and in the dictionary I kept the references to the nodes of the LinkedList for a constant look-up.



Complexity:

The run time complexity of the get() and set() methods of the LRU cache is O(1) or constant time

The space complexity is O(n), in this case, I'm making use of a LinkedList and a dictionary data structures, they booth
take the same amount of entries (n) so it will be O(2n) but that gets simplify to O(n).

