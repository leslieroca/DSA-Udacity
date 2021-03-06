Explanation:

# TrieNode
Each TrieNode is initialized with a dictionary, when a char is inserted in the TrieNode, it creates a new entry in the
dictionary if the char didn't exist before, the value es a child TrieNode which will represent new words with a the same
common prefix ending in char `char`.

To search for suffixes, I iterated through the tree using DFS keeping the path, when a leaf node was reached I stored
the path built so far into the result list, this way I guaranteed to find all the suffixes.

# Trie

To insert new words, I added the character "$" to the end of the original word, this way complete words that prefix
of a bigger word could be identify as complete words in the Trie, for example: "ant" and "antonym". To add new words
to the Trie, starting from the root node, I iterated through each of the character in the word, inserting it
in the current node and moving to the new or existing child node created for that character.

To find the node representing the passed prefix, starting from the root I iterated through each of the character of
the prefix and moved the node's child represented by the current character, if the character didn't exist in the current
node, then return None, it meant no original word had the passed prefix.


Complexity:

# TrieNode

- insert, O(1), simply adding an entry into a dictionary.

- suffixes, O(|A|^n) where |A| is the size of the alphabet and n the length of the prefix. as each node could have |A|
children and the tree could have n levels.

# Trie

-  insert, O(n) where n is the length of the word, based on iterating through the word as selecting the next child node
   is O(1).
-  find, O(n) where n is the length of the prefixes, based on iterating through the word as selecting the next child node
   is O(1).


