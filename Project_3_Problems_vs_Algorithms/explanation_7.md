Explanation:

# RouteTrieNode
Each RouteTrieNode is initialized with a dictionary, when a path part is inserted in the RouteTrieNode, it creates a
new entry in the dictionary if the path part didn't exist before.

A RouteTrieNode with a None handler will represent inner Nodes in the Trie whereas a node with a not None handler
represents a leaf node, meaning there's a handler for such path.

# RouteTrie

First, a leaf node is directly added as child of the root node to represent the root path, this leaf node has the
root handler.

To insert a new path, starting from the root node, I iterated through each of the part parts stopping at the second
to last and inserting it in the current node and moving to the new or existing child node created for that part, lastly
the last part is added as a leaf node with the passed handler.


To find the handler for the passed path, starting from the root I iterated through each of the path parts of
and moved the node's child represented by the current part, if the part didn't exist in the current
node, then return None, it means there's no handler for the passed path. if the final part is reached the return
the current node's handler.

# Router

Router relies mostly in the  RouteTrie data structure, the only logic specific to the Router class is splitting the
original path into path parts, to do so, and taking into account that /about path is the same as '/about/ path, first
step is to remove the last '/' if exist, second step is to remove first '/' as it's always there, lastly I split the
string by '/' returning a list of all the path parts.

Also, in lookup, when the a handler dos not exist, then the 'not_found_handler' passed at construction is returned
rather than returning None.


Complexity:

# TrieNode

- insert, O(1), simply adding an entry into a dictionary.


# RouteTrie

-  insert, O(n) where n is the number of path parts.
-  find, O(n) where n is the number of the path parts.

# Router

- add_handler, O(m) where m is the length of the path
- lookup, O(m) where m is the length of the path




