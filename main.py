import math, queue
from collections import Counter
import numpy as np

####### Problem 1 #######

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")

    if p.qsize() == 0:
        return None
    if p.qsize() == 1:
        # duplicate the only node so that we have a valid tree
        only = p.get()
        dummy = TreeNode(None, None, (0, ""))
        root = TreeNode(only, dummy, (only.data[0], ""))
        return root

    while (p.qsize() > 1):
        x = p.get()
        y = p.get()
        z = TreeNode(x, y, (x.data[0] + y.data[0], ""))
        p.put(z)

    # return root of the tree
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):

    if node is None:
        return code
    
    # leaf both children None and character not empty
    if node.left is None and node.right is None and node.data[1] != "":
        # if there's only one symbol, give it "0"
        code[node.data[1]] = prefix if prefix != "" else "0"
        return code
    
    if node.left is not None:
        get_code(node.left, prefix + "0", code)
    if node.right is not None:
        get_code(node.right, prefix + "1", code)
    return code


# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    if not f:
        return 0
    n = len(f)  # alphabet size
    bits = math.ceil(math.log2(n)) if n > 1 else 1
    total_symbols = sum(f.values())
    return bits * total_symbols


# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    
    total = 0
    if not C or not f:
        return 0
    for ch in f.keys():
        if ch in C:
            total += f[ch] * len(C[ch])
    return total


'''
f = get_frequencies('f1.txt')
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))

'''

if __name__ == "__main__":
    filenames = ['f1.txt', 'alice29.txt', 'asyoulik.txt', 'grammar.lsp', 'fields.c']
    for fname in filenames:
        f = get_frequencies(fname)
        fixed_cost = fixed_length_cost(f)
        T = make_huffman_tree(f)
        C = get_code(T)
        huff_cost = huffman_cost(C, f)
        print("File: %s" % fname)
        print("  Fixed-length cost:  %d" % fixed_cost)
        print("  Huffman cost:       %d" % huff_cost)
