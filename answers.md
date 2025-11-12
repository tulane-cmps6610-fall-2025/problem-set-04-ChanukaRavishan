# CMPS 6610 Problem Set 04
## Answers

**Name:**_________________________


Place all written answers from `problemset-04.md` here for easier grading.




- **1d.**

File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length
----------------------------------------------------------------------
f1.txt    | 1340 |  826 | 0.61
alice29.txt    |1039367  |676374 | 0.65
asyoulik.txt    | 876253| 606448| 0.68
grammar.lsp    | 26047| 17356| 0.67
fields.c    | 78050| 56206| 0.72



- **1d.**

Huffman coding is consistently more efficient than fixed-length coding, all the files got reduced to on average about 0.4 of the total size.



- **2a.**

Approch: Treat the array A[1…n] as an almost complete binary tree (children of i are 2i and 2i+1)
        Then run “sift-down" from every internal node.

        This approch preserves O(n) due to Node i is at height h(i) (distance to a leaf). A sift_down from i costs Θ(h(i))

'''

def build_min_heap(A):
    n = len(A) - 1           # using 

    for i in range(n//2, 0, -1):
        sift_down(A, i, n)   # restore min-heap in subtree 
                                # rooted at i

def sift_down(A, i, n):
    while 2*i <= n:
        c = 2*i
        if c+1 <= n and A[c+1] < A[c]:
            c += 1
        if A[c] < A[i]:
            A[i], A[c] = A[c], A[i]
            i = c
        else:
            break


'''


- **2b.**




- **3a.**



- **3b.**




- **3c.**



- **4a.**



- **4b.**




- **4c.**


- **5a.**



- **5b.**




- **5c.**
