"File Recursion"

Explanation:

In order to find all files under a specific directory, I search for all the files in the File System using the DFS algorithm
to traverse recursively the tree since the File System has a tree structure, once I get a file I check if it has the
targeted suffix, if so, I added to the list to return.


Complexity:

The run time complexity is O(n) where n the size of the tree, in this case, all the nodes(directories and subdirectories)
needs to be visited in order to get to all the leaves (files).

The space complexity is O(d) where d is the depth of the tree.