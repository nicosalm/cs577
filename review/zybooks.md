# Zybooks Exercises (CS 577) 

### 2.5.1
```py
def reverseArr(A):
    s = new Stack()
    for elem in A:
        stack.push(A.pop())
    while stack not empty:
        A.append(stack.pop())
```
This algorithm has a runtume of `O(n)`.

### 2.5.2
```py
def reverseArrQ(A):
    q = new Queue()
    for elem in A:
        q.enqueue(A.pop())
    while q not empty:
        A.append(0, queue.dequeue())
    return A
```
This algorithm has a runtime of `O(n^2)` because append is in `O(n)`.

### 2.5.8
#### 2.5.8a 
    Proof by Induction. When a tree has a single node and one level, p(v) = 1 ≤ 2 - 1 = 1
    which is true. If we add a level to a tree, we either (a) do not change
    the level or (b) increase the level by 1. If not change, p(v) ≤ 2^{(n+1)/2} ≤ 2^{(n+2)/2} which holds.
    If we increase the level by one, then p(v) = p(v) + 1. If this happens, then
    p(v) + 1 ≤ 2^{(n+1)/2}-2 = p(v) + 1 ≤ 2^(n/2) + 2 = 2^n + 1 => the theorem
    is true.
#### 2.5.8b
|
|
|
|
### 2.5.14
```py
recurse(n):
    if n is 1:
        return [1]
    c = recurse(n-1)
    for i in c:
        c.append(i.append(n))
    c.append(n)
    return c
```

This algorithm is in `O(n!)`

### 2.5.32
```py
def findLCA(x,y,T,node)
    if x on left and y on right of node:
        return node
    if x + y on left of node:
        return findLCA(x, y, T, node.left)
    else:
        return findLCA(x, y, T, node.right)
```

`O(logn)` if search occurs in `O(1)`, else `O(nlogn)`

### 2.5.33
```python
def biggestDiameter(T):
    x = deepest node on left subtree
    y = deepest node on right subtree
    return d_x + d_y - 2
```

`O(logn)` runtime.

### 3.5.8
|
|
|
|
### 3.5.18
We have a couple of cases. In case (1), a tree with 1 node with height(tree) = 1
the theorem holds (log2); (2) if we add a node to a tree w/ n nodes that increase
the height by 1 => log((n+1)+1). Also height ≥ log(n+1) => height + 1 ≥ log(n+2).
So the theorem holds.

### 3.5.32
```py
def foo(n, m):
    a = []
    for i in [1:n]:
        if m >= n: 
            m = m % n
        a.append([1:n][m])
    return a
```

### 4.7.21
We can make transformations to an arbitrary node by letting tree.root
and all successive left children of root be the initial elements of the chain. 
For each chainelement.right, a left rotation adds chainelement.right to 
the chain. Ultimately, we make the chain in `O(n)`.

### 4.7.27
|
|
|
|
### 4.7.42
Create [dogs] list in a natural ordering from youngest to oldest age. Store dogs
in a map with age as a key. Add new dogs -> `O(n)`. Remove dogs -> `O(1)`.

### 4.7.43
Create a BST ordered by employee.name and add all employees -> `O(logn)`. Make
an in-order traversal of the BST and return the alphabetical ordering of the employee
names. 

### 5.7.8
In a max-heap, we have that the item with the largest key is stored 
in the root of the heap. Conversely, in a min heap, that same element
will be stored in one of the leaf nodes.

### 5.7.12
The sum{i to n} logi is \Omega(nlogn). 

### 5.7.20
Insertion in decreasing order requires \Omega(nlogn) time to process. For 
each insertion, swap element i to the top. For the last n/2 elements this 
occurs when heap.height = \Omega(logn) -> \Omega(nlogn) time in total.

### 5.7.27
We can use a BST! Insertion time is `O(logn)`.

### 6.6.2
The algorithm executes in \Omega(n^3) time. 

### 6.6.10
Base case: n=1 -> T(1) = 4 = 4n -> Base case stands.
We assume T(n-1) = 4 * n(-1) -> T(n) = T(n-1) + 4 = 4n - 4 + 4 = 4n
=> T(n) = 4n

### 6.6.38
Base case: n=0 -> T(0) = 1 -> Base case stands.
We assume T(n-1) = 2^n -> T(n) = T(n-1) + 2^n = 2^n + 2^n - 1 = 2^(n+1) -1 => T(n) = 2^(n+1)-1

### 6.6.57
```py
def count(A):
    sum = 0
    for row in A:
        i = row.index + 1
        if row[i + 1] == 0: 
            sum += i + 1

    iterate to 0, add val of index to sum 
    return sum

```

### 6.6.74
```py
def findMissing(A/n): 
    sum = 0 
    for i in A:
        sum += i 
    values = ((n (n + 1) / 2) - sum 
    if i ≥ values: A.pop(i)
    if i not in A: return (i, values-1)
        
```

### 7.7.2O
Notice O|E| = c * |V| -> (logm) = O(logn) 

### 7.7.25
With BFS, we have that any node at level l is l edges away from the root s. 
Any beath from s to v will have ≥ l edges.

### 7.7.35
Make use of DFS. Continue until repeated edge, then turn. Repeat until there are no
more unexplored edges.

### 7.7.38
```py
def find(T, s, v, T.root):
    if s and v on T.left:
        find(T,s,v,T.left)
    if s and v on T.right:
        find(T,s,v,T.right)
    else: 
        return s depth + v depth
```
### 8.5.10
Lemma 8.4.1: lower-bounds; lemma 8.4.2: exchange

### 8.5.11
12 mg of (2) -> $132

### 8.5.14
Run the algorithm chosing furthest possible within K mile radius, go
to the station; repeat. 

### 8.4.24
```py
def minPenality(W, L):
    for word in W:
        sum += word.chars
        if sum > L:
            add(line break at sum-word.chars)
                sum = word.chars
    return
```
### 8.5.25
Greedy and optimal are different so greedy is not opt. 

### 9.5.3
Store dist during calculation and add to it when traversing the nodes. 
Either store this value in an array or an addition to each not that will
store dist from s to v. Store tree, starting with s as the node. After every
instance of Dijkstra's, add to the tree. Ultimately, this should create
a tree with shortest paths from root.

### 9.5.12
No, it does not work.

### 9.5.17
Run Dijkstra's. Ensure moving left -> right. Then, the algorithm should
return a monotone, min-cost path for this game.

### 9.5.18
```py
def run():
    create G = (V, E) with |V| = n and |E| = m - k
    run shortestpath(s, t) 
    if exists, return path
    keep adding k edges until shortestpath(s, t) works, return path
```

### 9.5.20
```py
def connect_min(A, F, n, m):
    create G = (V, E) with |V| = n and |E| = m
    run dijkstra(G) return shortestpath(n, m)
```

### 10.6.8
MSTs have no cycles by definition. So negative edges do not cause 
issues like Dijkstra's.

### 10.6.11
If e is the minimum weight edge in G = (V, E) -> e is the smallest edge weight 
between any two connected components of G -> used to connect in MST.

### 10.6.22
Invert all the edges in G = (V, E); run mst(G), Same run time.

### 10.6.27
Run kruskal(G = (V, E)) -> O(n + m) 

### 12.6.1
(a): O(n), (b): O(n^3), (c): O(n^4logn), (d): O(n^2), (e): O(n^2logn)

### 12.6.9
T(n) = 2T(2n/3) + T(n/3) -> O(n^2) 

### 12.6.12
```py
def bound(S): # where S is a set of n numbers
    if |S| is 1:
        return S[0]
    a = bound(first half of S)
    b = bound(latter half of S)
    return(max(a, b)
```
### 12.6.16
```py
def better(S): # same S as 12.6.12
    if |S| < k: sort and return S 
    l1 = better(1st half of S)
    l2 = better(2nd half of S) 
    merge l1, l2 to A 
    return A

```
```py
def skyline(S):
    if |S| is 0: return S[0]
    pts_front = skline(0:S/2)
    pts_back = skuline(S/2:) 
    return max(pts_front, pts_back) 

```
### 13.4.8
We need to make a single change. Within the merge step, rather than creating
two arrays on any merge, use the first half of T for the first array and second
half of T for the latter half.

### 13.4.9
```py
def rem_dups(A):
    a = map()
    for i in A:
        if a.contains(i)
            A.remove(i)
        else:
            a.add(i)
    return A # O(n)
```

### 13.4.28
run with the following merge algorithm:
```py
merge(arr1, arr2, arr):
    A = []
    for i in arr:
        if arr1.firstletter.contains(i)
            A.add(arr1.remove(i))
        # and so on, result is O(mnlogn) 
```

### 14.5.6
We have three element groups: 3(n/6)-2 = 3n/6-2 
FAILS: T(n) ≤ T(n/3+1) + T(n/2+2) +bn
T(n) too small

### 14.5.8
Achieve stable sort by adjusting comparator to both x≥y x.pos > y.pos

### 14.5.24
```py
def find(A):
    map = defaultdict(int) 
    for elem in A:
        firstchar = elem.substring(0, 1) 
        map(firstchar) += 1
    if val in map ≥ |A|/2: let = val.key; else return False

```
### 15.8.10a
|
|
|
|
|
|
|
|
### 15.8.29
```py
def verify(S):
    prev = 0
    for i in |S|: 
        if valid(s.substring(prev, i)): prev = i
        return prev == |S| # O(n) runtime
```
### 15.8.34
```py

D = [[]] #2d array
D[0][0] = (1, 1)
D[i][j] = min(D(x, y, m+(i-1, j)), D(x, y, m + (i, j - 1)), D(x, y, m + (i, j)
return D[|x|][|y|]
```

### 15.8.35
M = []
M[0] = AliceOpt()
M[x] = AliceOpt(A) + min(BobOpt(A)) 
In O(n)

### 15.8.36
Iterate through all possible i, j combinations where i + j = end iof world series, return avg probability

### 16.6.8
|
|
|
|
|
|
|
|
### 16.6.18
from [0, n], i fsubstring of o:i is in P return last val of i where there was a substring.

### 16.6.28
use hashmap to enter new info; keys in map are length n to figure webpage w/ that length

### 19.7.2
Edges
    * Forward: s-v2, v2-v3, v1-v4, v4-8
    * Backward: v1-v3
3: 3->v3->t (capacity 3), s->v2->v3->t (capacity 3) 
Max flow of 14

### 19.7.6
Min cut s -> a -> b (4)

###  19.7.28
|
|
|
|
|
|
|
|
### 19.7.32
DFS on G for two paths. Start with two different nodes. If DFS can find
t without intersections, return True. Else, False. O((V+E)*P)

### 19.7.33
Least overlaps. 

### 19.7.34
For each lim find a value diff = closest - next closest. For The limo with
the largest distance, match the two vals together. 

### 20.8.1
No

### 20.8.3
SAT is in NP. You can verify in polynomial time the length of the boolean formula. This problem
can be redcued to 3SAT if we take all AND in the boolean formula and convert
them to clauses. We end up with an instance of 3SAT .

### 20.8.9
|
|
|
|
### 20.8.24
(a + b) -> !A -> b and !b -> a
Create an algorithm to do this, where we add edges corresponding to the clauses in the 
logical statement. Return true if DFS reaches !node from node, false otherwise.

### 20.8.35
Hamiltonian Path (HP) in np by O(|E + V|). It is NP complete as we can reduce Hamiltonian Cylce (HC).
If we remove w and change all edges into w to be leading into v, and all edges leading
into v leading from w, then the HC = HP.

### 20.8.39
CC is in NP as you run through G and find the smallest collection in polynomial time. Reduced to Vertex Cover.
See lecture for reduction.

### 20.8.41
The Russian Lit (RL) problem is in NP as a certificer could simply verify if the subsets contain
the same sum in O(n) time. The RL problem can be reduced to Set Cover. Convert book sets into sets.
If E covers ≥ n/2 with no overlaps then RL is True. Else, no. Therefore,
NP complete as reducible to SC which is NP Hard.

### 21.10.2
P(X > n/2) ≤ exp(-n/6) + (1/2 + 1/6)n

### 21.10.18
consider [1,2,3]. swapping 1,2; 1,3; 2,3 leads to [2,1,3], [3,2,1], [1,3, 2]. But this
cannot create [3,1, 2] -> each permtation does not have equal probability.

### 21.10.38
(a) 99999999/100000000
(b) We find it is bounded by 1-(m^2/2n), and 1 -x≤e^-x and if x = m^2/2n -> 1 - (m^2 / 2n) ≤ e ^ -(m^2/2n) -> p is bounded by e ^ -(m^2/2n) 
(c) 1/2 = e ^ -(m^2/2n)
n = log(2)/2

### 23.6.4
(77/3, 77/5) (8, 28)
Negative values of a result in no unique 

### 24.6.13
Minimize: Minimize: w = 5y1 + 3y2 + 24y3 + 9y4
y1 + 6y2 + 5y3 ≥ 1
y1 - 3y2 + 6y4 ≥ 2
y1, y2, y3, y3 ≥ 0

### 24.6.35
x1 = #water jugs
x2 = #tents
x3 = #first aid packs
x4 = #food rations
x5 = #personal supplies
x6 = #camels needed oh caml my caml

We want to minimize x6 in this case and produce a set which uses the minimal amount of caml boys

Subject to: 
We have that we need:
* x1 ≥ 2 * 15 (18 + .5 * 18)
* x2 ≥ 64
* x3 ≥ 15
* x4 = 13
* x5 = 300

300x6 ≥ 5x75+5x50+5x25
x1,x2,x3,x4,x5,x6 ≥ 0

Done!
