"""
Least Recently Used Cache

We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however,
the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add
a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put()
operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache.
An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches
its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full,
you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

Here is some boiler plate code and some example test cases to get you started on this problem:

"""

class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0


    def append(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node

        self._length += 1


    def delete(self, node):
        # node is the only node in the LinkedList
        if self.head == self.tail == node:
            self.head = None
            self.tail = None
        # node is the first node of the LinkedList.
        elif self.head == node:
            self.head = node.next
            node.next.prev = None
        # node is the last node of the LinkedList.
        elif self.tail == node:
            self.tail = node.prev
            node.prev.next = None
        # node is an inner node.
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        self._length -= 1


    def __len__(self):
        return self._length



class LRU_Cache(object):


    def __init__(self, capacity):
        # Initialize class variables.
        self.capacity = capacity
        self.l_list = LinkedList()
        self.d = dict()


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.d:
            return -1

        node = self.d[key]
        self.l_list.delete(node)
        self.l_list.append(node)

        return node.value

    def set(self, key, value):

        # If capacity == 0.
        if self.capacity == 0:
            return

        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        # If key is present in the cache, remove corresponding node from LinkedList
        # to avoid duplicate nodes with same key.
        if key in self.d:
            self.l_list.delete(self.d[key])

        # Delete the oldest item when the cache reaches its capacity.
        if len(self.l_list) == self.capacity:
            first_node = self.l_list.head
            self.l_list.delete(self.l_list.head)
            del self.d[first_node.key]


        node = Node(key, value)
        self.l_list.append(node)
        self.d[key] = node


# Test Case 1.
our_cache = LRU_Cache(3)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)

our_cache.get(1)        # returns 1
our_cache.get(3)        # returns 3

our_cache.set(4, 4)

print(our_cache.get(3))     # prints 3


# Test Case 2.
our_cache = LRU_Cache(3)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)

our_cache.get(2)        # returns 2
our_cache.get(1)        # returns 1

our_cache.set(4, 4)

print(our_cache.get(3))     # prints -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(4))     # prints 4


# Test Case 3.
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

our_cache.get(1)        # returns 1
our_cache.get(2)        # returns 2
our_cache.get(9)        # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))     # prints -1 because the cache reached it's capacity and 3 was the least recently used entry


# Test Case 4.
our_cache = LRU_Cache(1)

our_cache.set(1, 1)
print(our_cache.get(1))      # prints 1

our_cache.set(2, 2)
our_cache.set(1, 3)          # (1, 1) is removed to avoid duplicates

print(our_cache.get(2))      # prints -1 because the cache reached it's capacity and 2 was the least recently used entry
print(our_cache.get(3))      # prints -1 because 3 is not present in the cache
print(our_cache.get(1))      # prints 3



# Test Case 5.
our_cache = LRU_Cache(6)

print(our_cache.get(1))      # prints -1 because the cache is empty, not value have been set yet


# Test Case 6.
our_cache = LRU_Cache(0)

our_cache.set(1, 1)         # returns -1 because the cache size is 0, so, not value can be set.

