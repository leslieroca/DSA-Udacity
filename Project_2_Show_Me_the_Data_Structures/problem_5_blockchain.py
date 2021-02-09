"""
Blockchain

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how
it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous
block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time
when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.


We can break the blockchain down into three main parts.

First is the information hash:

"""
import hashlib
import time



# def calc_hash(self):
#       sha = hashlib.sha256()
#
#       hash_str = "We are going to encode this string of data!".encode('utf-8')
#
#       sha.update(hash_str)
#
#       return sha.hexdigest()

# We do this for the information we want to store in the block chain such as transaction time, data, and information
# like the previous chain.

# The next main component is the block on the blockchain:

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash

    def __repr__(self):
        return str((self.timestamp, self.data, self.previous_hash))

# Above is an example of attributes you could find in a Block class.

# Finally you need to link all of this together in a block chain, which you will be doing by implementing it in a
# linked list. All of this will help you build up to a simple but full blockchain implementation!


class BlockchainNode:

    def __init__(self, block):
        self.block = block
        self.next = None


    def __repr__(self):
        return str(self.block)


class Blockchain:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_block(self, data):
        # Do not create block is data is None.
        if data is None:
            return

        previous_hash = None if self.head is None else self.calc_previous_hash()
        block = Block(time.time(), data, previous_hash)

        node = BlockchainNode(block)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def calc_previous_hash(self):
        # Block hash is defined by the sha256 hash value of the string formed by the block timestamp and its data.
        sha = hashlib.sha256()
        block_info = "%f%s" % (self.tail.block.timestamp,  self.tail.block.data)
        block_info_encoded = block_info.encode('utf-8')
        sha.update(block_info_encoded)
        return sha.hexdigest()

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(current)
            current = current.next
        return str(result)




# Test case 1.
chain = Blockchain()

chain.append_block("+100")
chain.append_block("-50")
chain.append_block("+100")
chain.append_block("-150")

print(chain)  # Prints: [(1606239118.2675881, '+100', None), (1606239118.2685719, '-50', '0ef9403b7264ab3c98f7a986a40c18baae61a42f4a3f5189d861e850956975b3'), (1606239118.268594, '+100', '7659e952243cf9852426a24a788f9be836a34d8ee122bf89d103c41000ec44c0'), (1606239118.2686012, '-150', 'f5e6c24a37d84f9bb0f88ce58e32bf46aabb186090d34ef4b3515b2b70fd6e52')]

# Test case2.
chain = Blockchain()

chain.append_block(None)
chain.append_block("A")

print(chain)    # Prints: [(1607837943.449995, 'A', None)]

# Test case 3.
chain = Blockchain()

chain.append_block("")
chain.append_block("")
chain.append_block("")
chain.append_block("")

print(chain)    # Prints: [(1607837943.450005, '', None), (1607837943.4500108, '', 'ebc98537a620e797da26b697fd36636b401970e1bb3bf3383860bc70018adfed'), (1607837943.450015, '', '76146bdd5c2e67a8a921520c0e4a40dedaffd7a407a8c4906238ba5d87685c77'), (1607837943.450018, '', '7db6f5ad93abe96df88b789151ae7d90c65155498a116701a9bb463ab8a764ee')]
