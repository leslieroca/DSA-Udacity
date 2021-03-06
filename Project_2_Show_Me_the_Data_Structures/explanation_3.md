"Huffman Coding"


ENCODING

Explanation:
In order to encode the input data (string):

1. I first build and sort a list of tuples from lowest to highest frequencies, we do this by creating a dictionary
using the Counter subclass from collections and used it to create a list of tuples with the tow values being the key
and value(frequency)from the dictionary, and returned a sorted list by frequencies using the method sorted() with the
lambda expression.

2. Build the Huffman Tree using two queues. The fist queue will only contain the leaf nodes (the nodes having only one
character), the nodes will be pushed to the queue from lowest to highest frequencies assuring the node with the lowest
frequency is always at the front of the queue. The second queue will contain the inner nodes, which are created
by getting the two lowest frequencies of the nodes either from the first or the second queue, concatenating their
letters, adding their frequencies and setting the selected nodes as children, the new inner node is later pushed to
the second queue assuring the frequencies remains sorted in the queue from lowest(front) to highest(back).

3. Trim the Huffman Tree by traversing the tree with the DFS algorithm and setting the node's value with its prefix
value only, therefore removing the frequency value from memory.

4. To assign the binary code to each letter I do a full tree traversal using DFS, keeping the path in binary code
(0 for left and 1 for right), once a leaf is reached I store the letter as key and the current binary code as value in
a dictionary.

5. And finally create the binary code corresponding to the input string base on each character of the string and its
corresponding binary code from the mapping dictionary.



Complexity:
In order to analyze the time complexity of Encoding is necessary to analyze each of the steps separately. To build the
list of tuples we first create a dictionary using Counter that is constructed by iterating over the input string, that
takes linear time or O(n) where n is the length of the input string. Create the list of tuples from the dictionary takes
O(T) where T is the length of the input string alphabet, I'm going to assume that the input string alphabet is the ASCII
character, so T = 255 therefore complexity is O(255) which is constant time, no matter the length of the input.
Sorting the list will also be constant time since we only need to sort, in the worst-case scenario, 255 elements.
To build the Huffman tree we iterate over the list of tuples to create the first queue, that takes constant time as well.
I decided to use two queues since it allows to keep the lowest frequency at the front of the queues
making the look-up process O(1). Trimming the tree and assigning the binary code takes also constant time because the
number of nodes on the tree is bounded to the length of the alphabet meaning that the max number of nodes will be always
less or equal to 2T - 1.
To create the binary code is O(n) since we have to iterate over the characters of the input string

Finally the time complexity of encoding is: O(n) + O(1) + O(1) + O(1) + O(n) => O(n)


REQUIRED
Isn't this time complexity O(nlogn)?

This is not O(n log n) time complexity, It would have been if I have used a priority queue or min heap since a priority
queue gets sorted every time an element is popped or pushed to it. But I used TWO queues what allowed me to keep the
lowest frequencies always at the front of the queues without the need to have the queues sorted.


The space complexity is O(1) because the number of nodes and the size of the mapping dictionary is bounded to the size
of the alphabet which constant no matter the size of the input.



DECODE:

Explanation:
To decode the data we traverse the Huffman tree following the path on the data (binary code), once a leaf (a single letter)
is reached, we store the letter in a list and start iterating the tree from the root again continuing in data from where
we left.

Complexity:
The runtime is O(n * H) where n is the length of the binary code and H is the height of the Huffman tree, H is bounded to the length
of the alphabet as explained before therefore, H is constant so, the time complexity of decoding is O(n)

In order to build the decoded string we use a list to store each character so, the space complexity is O(n).