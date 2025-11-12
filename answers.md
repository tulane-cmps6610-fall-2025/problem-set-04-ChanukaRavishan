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

```python

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

```

This approch preserves O(n) due to Node i is at height h(i) (distance to a leaf). A sift_down from i costs Θ(h(i))

$$\sum_{h=0}^{logn} \frac{n}{2^{h+1}} * O(h) = n * \sum_{h > 0} \frac{h}{2^(h+1)} = O(n)$$


- **2b.**

when sequential span (no parallelism): the loop is inherently sequential → Θ(n) span.

Run all sift_downs for nodes on the same level in parallel, proceeding level by level from bottom to top. At level with height h, each sift_down takes Θ(h) time and they don’t interfere across disjoint subtrees. The span is then

$$\sum_{h=1}^{logn} O(h) = O((logn)^2)$$


- **3a.**

For denominations that are powers of 2 (1, 2, 4, 8, …, 2^k), the greedy algorithm is:

```python
def make_change(N):
    coins = []
    while N > 0:
        largest = 2^⌊log2(N)⌋ # largest power of 2 ≤ N
        coins.append(largest)
        N = N - largest
    return coins
```

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

Providing a counter example where our already devised algorithm fail in Fortuito,

Let the denominations be `{1, 3, 4}` and let `N = 6`.  
The greedy approach takes the largest coin ≤ 6, i.e., `4`, leaving `2`, then uses `1 + 1` → **3 coins** (`4+1+1`).  
But the optimal solution uses **2 coins**: `3 + 3`.  

Therefore, the greedy choice is not always optimal for arbitrary denominations.


- **4b.**

Optimal substructure property

Suppose we have an optimal solution `S` for `N` whose last coin is `dj`, and suppose (for contradiction) that the multiset of coins `S'` used to sum to `N − dj` is *not* optimal for `N − dj`. Then there exists another solution `T` for `N − dj` using fewer coins than `S'`. Replacing `S'` in `S` by `T` yields a solution for `N` with fewer coins than `S`, contradicting the optimality of `S`. Hence `S'` must be optimal.  

This proves the problem has **optimal substructure** enven when it doesnt have greedy choice property.




- **4c.**

The subproblem: `OPT(x) = min_{dj ≤ x} (1 + OPT(x − dj))`, with `OPT(0) = 0` and `OPT(x) = +∞` if no coin fits.

**Bottom-up DP :**

```python
def min_coins(D, N):
    INF = 10**9
    dp = [INF] * (N + 1)
    dp[0] = 0
    for x in range(1, N + 1):
        best = INF
        for d in D:
            if d <= x and dp[x - d] + 1 < best:
                best = dp[x - d] + 1
        dp[x] = best
    return dp[N] if dp[N] < INF else None

```
Work: Θ(kN) in the worst case for both versions (k = |D|).

Span: with the straightforward order (filling x = 1…N), each state depends on smaller x, so the span is Θ(N). 
    If we parallelize the inner min across the k coins, per-state reduction takes Θ(log k) span, so total span is Θ(N + log k).

- **5a.**

We have tasks `a_i = (s_i, f_i, v_i)` and want a maximum-value subset of **non-overlapping** tasks.

Yes, the optimal substructure property holds

Let `OPT(t)` be the maximum value achievable using only tasks that finish at or before time `t`.  

then Sorting tasks by non decreasing finish time: `f_1 ≤ f_2 ≤ … ≤ f_n`.  

For task `i`, we can define `p(i)` as the largest index `< i` with `f_{p(i)} ≤ s_i`.

we need to prove, In an optimal solution for the prefix `1..i`, either task `i` is excluded, or it is included and the remaining tasks must be an optimal solution for `1..p(i)`.

Proof

Suppose an optimal solution for `1..i` includes task `i`. Any other included task must end by `s_i`, hence must be among `1..p(i)`. If those tasks were not optimal for `1..p(i)`, we could replace them with a better solution for `1..p(i)`, increasing the total—contradiction. If the optimal solution excludes `i`, its value is exactly `OPT(i-1)`. ∎

This yields the recurrence:

\[

OPT(i) \;=\; \max\big( v_i + OPT(p(i)),\; OPT(i-1) \big), \qquad OPT(0)=0 .

\]



- **5b.**




- **5c.**


**Bottom-up algorithm.**

1. Sort tasks by `f_i`.
2. Pre compute `p(i)` for each `i` by binary searching on the `f`’s.
3. Fill `OPT[0..n]` with the recurrence; keep `choice[i]` to reconstruct the set.

```python


def weighted_interval_scheduling(tasks):

    # tasks: list of (s, f, v)

    # considering finish time
    tasks = sorted(tasks, key=lambda x: x[1])
    s = [0] + [t[0] for t in tasks]
    f = [0] + [t[1] for t in tasks]
    v = [0] + [t[2] for t in tasks]
    n = len(tasks)

    # array p(i)   
    finishes = f[:]  # thid is already sorted
    p = [0]*(n+1)
    for i in range(1, n+1):
        # rightmost j<i with f_j <= s_i
        j = bisect_right(finishes, s[i], 0, i) - 1
        p[i] = j

    # DP
    OPT = [0]*(n+1)
    take = [False]*(n+1)
    for i in range(1, n+1):
        take_val = v[i] + OPT[p[i]]
        skip_val = OPT[i-1]
        if take_val > skip_val:
            OPT[i] = take_val
            take[i] = True
        else:
            OPT[i] = skip_val