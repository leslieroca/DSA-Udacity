
"""
Union and Intersection of Two Linked Lists

Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set
of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set
of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection,
respectively. Once you have completed the problem you will create your own test cases and perform your own run time
analysis on the code.

We have provided a code template below, you are not required to use it:

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

# Helper function to create a set of the values of a LinkedList.
def create_set(llist):

    node_value_set = set()

    current_node = llist.head
    if current_node is not None:
        while current_node.next:
            node_value_set.add(current_node.value)
            current_node = current_node.next

    return node_value_set


def union(llist_1, llist_2):
    # set_1 stores the unique elements of llist_1.
    set_1 = create_set(llist_1)
    # set_2 stores the unique elements of llist_2.
    set_2 = create_set(llist_2)

    # union_set stores the elements that are present in set_1, set_2 or in both.
    union_set = set_1 | set_2
    # instance of LinkedList class
    union_llist = LinkedList()

    for value in union_set:
        union_llist.append(value)


    return union_llist



def intersection(llist_1, llist_2):
    # set_1 stores the unique elements of llist_1
    set_1 = create_set(llist_1)
    # set_2 stores the unique elements of llist_2.
    set_2 = create_set(llist_2)

    # intersection_set stores the elements that are present in both set_1 and set_2.
    intersection_set = set_1 & set_2
    intersection_llist = LinkedList()

    for value in intersection_set:
        intersection_llist.append(value)

    return intersection_llist



# Test case 1.
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))   # Prints: 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
print (intersection(linked_list_1,linked_list_2))   # Prints: 4 -> 6 ->


# Test case 2.
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))      # Prints: 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print (intersection(linked_list_3,linked_list_4))    # Shouldn't print anything since there is not intersection.


# Test case 3.
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))      # Shouldn't print anything since we are passing empty LinkedLists
print (intersection(linked_list_5,linked_list_6))       # Shouldn't print anything since we are passing empty LinkedLists


# Test case 4.
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [1,1,1,1,1,1,1]
element_2 = [1,1,1,1]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))      # Prints: 1 ->
print (intersection(linked_list_7,linked_list_8))       # Prints: 1 ->


