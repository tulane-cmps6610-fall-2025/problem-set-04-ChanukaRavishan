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

This approch preserves O(n) due to Node i is at height h(i) (distance to a leaf). A sift_down from i costs Θ(h(i))

$$\sum_{h=0}^{logn} \frac{n}{2^{h+1}} * O(h) = n * \sum_{h > 0} \frac{h}{2^(h+1)} = O(n)$$


- **2b.**

when sequential span (no parallelism): the loop is inherently sequential → Θ(n) span.

Run all sift_downs for nodes on the same level in parallel, proceeding level by level from bottom to top. At level with height h, each sift_down takes Θ(h) time and they don’t interfere across disjoint subtrees. The span is then

$$\sum_{h=1}^{logn} O(h) = O((logn)^2)$$


- **3a.**

For denominations that are powers of 2 (1, 2, 4, 8, …, 2^k), the greedy algorithm is:

function make_change(N):
    coins = []
    while N > 0:
        largest = 2^⌊log2(N)⌋ # largest power of 2 ≤ N
        coins.append(largest)
        N = N - largest
    return coins

Intuition: At each step, choose the largest coin denomination (2^i) that does not exceed the remaining amount. Repeat until the remaining value becomes zero.



- **3b.**

The algorithm is optimal because the system of denominations {1, 2, 4, …, 2^k} satisfies both greedy choice and optimal substructure properties.

- **Greedy choice property:**  
  Choosing the largest power of 2 ≤ N always reduces the remaining amount optimally, since smaller denominations cannot combine to equal that same coin.

- **Optimal substructure:**  
  After taking the largest coin, the problem reduces to finding an optimal solution for the remaining amount (N − 2^i), which is structurally identical to the original problem.

Each amount N can be uniquely expressed as the sum of distinct powers of 2.  
Thus, the greedy algorithm effectively constructs the binary representation of N.



- **3c.**

*Work:** Θ(log N)  
  Each iteration removes the largest power of 2, and since there are at most log₂(N) denominations, the loop runs O(log N) times.

- **Span:** Θ(log N)  
  Each step depends on the result of the previous subtraction, so there’s no parallelism beyond O(1) per step.  
  Hence, total span is also Θ(log N).


- **4a.**



- **4b.**




- **4c.**


- **5a.**



- **5b.**




- **5c.**
