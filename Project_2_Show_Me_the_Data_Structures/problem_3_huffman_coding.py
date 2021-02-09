"""
Huffman Coding
A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding
schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each
character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be
visualized on a binary tree with each encoded character being stored on leafs.

There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building a Huffman tree,
encoding the data, and, lastly, decoding the data.

Here is one type of pseudocode for this coding schema:

Take a string and determine the relevant frequencies of the characters.
Build and sort a list of tuples from lowest to highest frequencies.
Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters.
(This is the heart of the Huffman algorithm.)
Trim the Huffman Tree (remove the frequencies from the previously built tree).
Encode the text into its compressed form.
Decode the text from its compressed form.
You then will need to create encoding, decoding, and sizing schemas.

For Example:

"""

import sys
from collections import Counter
from collections import deque

"""Class Node"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)


"""Build and sort a list of tuples from lowest to highest frequencies."""
def char_frequency(string):
    frequencies_list = list()
    frequencies_dict = Counter(string)

    for key in frequencies_dict:
        frequencies_list.append((key, frequencies_dict[key]))

    return sorted(frequencies_list, key=lambda x: x[1])


"""Build the Huffman Tree."""
def create_huffman_tree(string):
    # If string length in 1
    if len(string) == 1:
        return Node(string)

    frequencies_list = char_frequency(string)
    leaf_nodes_queue = deque()
    inner_nodes_queue = deque()

    for tuple in frequencies_list:
        leaf_nodes_queue.append(Node(tuple))

    while len(leaf_nodes_queue) > 0 or len(inner_nodes_queue) > 1:
        # Set node1
        freq_leaf = leaf_nodes_queue[0].value[1] if len(leaf_nodes_queue) > 0 else float('inf')
        freq_inner = inner_nodes_queue[0].value[1] if len(inner_nodes_queue) > 0 else float('inf')
        node1 = leaf_nodes_queue.popleft() if freq_leaf <= freq_inner else inner_nodes_queue.popleft()

        # Set node2
        freq_leaf = leaf_nodes_queue[0].value[1] if len(leaf_nodes_queue) > 0 else float('inf')
        freq_inner = inner_nodes_queue[0].value[1] if len(inner_nodes_queue) > 0 else float('inf')
        node2 = leaf_nodes_queue.popleft() if freq_leaf <= freq_inner else inner_nodes_queue.popleft()

        # Create inner nodes
        inner_tuple = ((node1.value[0] + node2.value[0]), (node1.value[1] + node2.value[1]))
        inner_node = Node(inner_tuple)
        # Set inner nodes children
        inner_node.left = node1
        inner_node.right = node2

        inner_nodes_queue.append(inner_node)

    root = inner_nodes_queue.popleft()
    return root

"""Trim the Huffman Tree (remove the frequencies from the previously built tree)."""
def trim_huffman_tree(node):
    if node is None:
        return

    node.value = node.value[0]
    trim_huffman_tree(node.left)
    trim_huffman_tree(node.right)



"""Assigning a binary code to each letter, using shorter codes for the more frequent letters."""
def assign_binary_code(root):
    map = dict()

    def traverse_to_build_map(node, binary_code):
        if node is None:
            return

        if node.left is None and node.right is None:
            map[node.value] = binary_code
            return

        traverse_to_build_map(node.left, binary_code + "0")
        traverse_to_build_map(node.right, binary_code + "1")

    traverse_to_build_map(root, "")
    return map


"""Encode the text into its compressed form."""
def huffman_encoding(string):
    # If string is empty, return en empty string and a tree value None.
    if len(string) == 0:
        return ("", None)

    root_node = create_huffman_tree(string)
    trim_huffman_tree(root_node)
    letter_binary_code_map = assign_binary_code(root_node)

    encoded = [letter_binary_code_map[char] for char in string]

    return ("".join(encoded), root_node)


def huffman_decoding(data,tree):
    if tree is None: # Not encoding was made because original string was empty.
        return data

    if len(data) == 0: # tree has just one node, original string had just one letter.
        return tree.value

    decoded = []

    current_node = tree
    for bit in data:
        if bit == "0":
            current_node = current_node.left
        else:  # bit == "1"
            current_node = current_node.right

        if current_node.left is None and current_node.right is None:  # current_node is a leaf
            decoded.append(current_node.value)
            current_node = tree

    return "".join(decoded)



if __name__ == "__main__":
    codes = {}

    # Test case # 1
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))     # 69
    print ("The content of the data is: {}\n".format(a_great_sentence))         # The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))        # 36
    print ("The content of the encoded data is: {}\n".format(encoded_data))     # 0110111011111100111000001010110000100011010011110111111010101011001010

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))      # 69
    print ("The content of the decoded data is: {}\n".format(decoded_data))         # The bird is the word


    # Test case # 2
    a_great_sentence = "A"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))         # 50
    print ("The content of the data is: {}\n".format(a_great_sentence))         # A

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # '' cannot be parsed to int.
    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))     # Empty

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))         # 50
    print ("The content of the decoded data is: {}\n".format(decoded_data))         # A

    # Test case # 3
    a_great_sentence = ""

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))  # 50
    print("The content of the data is: {}\n".format(a_great_sentence))  # A

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # '' cannot be parsed to int.
    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))  # Empty

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))  # 50
    print("The content of the decoded data is: {}\n".format(decoded_data))  # A
