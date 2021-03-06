"Blockchain"

Explanation:

In order to append a new block to the blockchain, I load all the existing blocks into a LinkedList
data structure, each node of the LinkedList contains a blockchain block and a pointer to the next node in the LinkedList.
The LinkedList is built under the invariant that the previous_hash value in the next node's block is a unique hash value
that identifies the current node's block. The hash value for a block is defined by the sha256 hash value of the
string formed by the block timestamp value and its data, given the assumptions blocks are created once at a time, we can
be sure each hash value will be unique.


Complexity:

The only operation created in the Blockchain class is append_block which is constant as each blockchain instance has a
reference to the LinkedList tail, so the run time complexity is O(1).

The space complexity of building a blockchain is O(n) since we need to build a LinkedList, n is the length of the LinkedList.
