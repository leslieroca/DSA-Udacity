"Union and Intersection"

Explanation:

To solve the union_and_intersection problem I create a helper function named create_set that takes-in a LinkedList and
return a set of the values of each node in the LinkedList. I use this helper function either to create the union
LinkedList (Once I get the sets of the values of the LinkedLists I create a union with both sets using the '|' operator
and iterate over that union creating a new LinkedList withe the values of this set) and the intersection
LinkedList (Once I get the sets of the values of the LinkedLists I create an intersection of the sets using the '&'
operator and iterate over that intersection creating a new LinkedList with the values of this set).



Complexity:

The run time complexity is O(n + m) where n and m are the sizes of the original LinkedLists
The space complexity is also O(n + m) where n and m are the sizes of the original LinkedLists