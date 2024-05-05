
# mst greedy

'''
Note: MSTs are undirected

Optimal substructure for MST:
    if e = {u, v} is an edge of some MST
        - contract e: merge u, v

         \      /         \  /
          u -- v    ->     uv
         /      \         /  \
    
    could end up with duplicate edges a, b by this process 
    when merging, remove duplicates
    cost of remaining edge = min { cost(a), cost(b) }

    Theorem: if T' is a MST of G \ e -> T'U{e} is a MST of G

Dynamic program:
    - Guess edge e in an MST
    - constract e
    - recurse 
    - decontract
    - add e
        ... in exponential time :(
        ... but can make it polynomial by removing the guessing! :)

Proof: 
    Say MST T* of G contains e.
    => T*\{e} is a spanning tree of G\{e}
    w(T') ≤ w(T*\{e})
    w(T'u{e}) = w(T') + w(e)
    w(T'u{e}) ≤ w(T*\{e}) + w(e) = w(T*)
    => T'u{e} is MST.

Greedy choice property for MST:
    Let S ⊆ V
    Consider any cut (S, V \ S)
    Crossing edges are edges which cross the cut

    Suppose e is a least-weight edge crossing the cut:
        e = {u, v} u in S, v in V \ S

    Then e in some MST

Proof: cut & paste argument
    Let T* be a MST of G
    Say e not in T*
    Must be e' in T* crossing the cut
    T*\{e'}u{e} is a spanning tree
    w(T*\{e'}u{e}) = w(T*) - w(e') + w(e) ≤ w(T*) by w(e) ≤ w(e')
    => T*\{e'}u{e} just as good as T* but contains e
    => T*\{e'}u{e} is a MST

    Note:
        - Only modified edges crossing cut (S, V \ S)
'''



# Prim's 

'''
Prim's Algorithm
    - Maintain priority queue Q on V \ S 
        where v.key = min { w(u,v) | u in S }
    - Initially Q stores V
        - s.key = 0 for arbitary start vertex s in V
        - for v in V \ {s}; v.key = inf
    - Until Q empty:
        u = Extract-Min(Q) (<=> add u to S)
        for v in Adj[u]:
           - if v in Q (v not in S) & w(u,v) < v.key:
                - v.key = w(u, v) (<- Decrease-Key)
                - v.parent = u
    - Return {{v, v.parent} | v in V}
'''

'''
Correctness:
    tree T_s in S ⊆ MST of G
    - By induction: ∃ MST T* ⊇ T_s
    - T_s -> T_s' = T_s U {e} 
    - Greedy choice property:
        modify T* to include e & T_s

    Time: same as Dijkstra's (best: O(VlogV + E) with fibb heaps)
'''

import heapq

def prim(graph, start):
    # The graph is represented as a dictionary of dictionaries (adjacency list)
    # graph[u][v] = weight of edge u-v

    # Priority queue: elements are (key, vertex, parent)
    pq = []
    for v in graph:
        if v == start:
            heapq.heappush(pq, (0, v, None))
        else:
            heapq.heappush(pq, (float('inf'), v, None))
    in_queue = {v: True for v in graph}  # Track vertices in the priority queue

    mst = []  # To store the MST edges
    while pq:
        key, u, parent = heapq.heappop(pq)
        if not in_queue[u]:
            continue
        in_queue[u] = False  # Mark vertex as not in Q (added to S)
        if parent is not None:
            mst.append((parent, u))

        for v, weight in graph[u].items():
            if in_queue[v] and weight < next((x[0] for x in pq if x[1] == v), float('inf')):
                # Update the vertex key if a cheaper link is found
                heapq.heappush(pq, (weight, v, u))

    return mst

# Example usage:
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'E': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'C': 5, 'D': 1}
}
start_vertex = 'A'
print("MST using Prim's Algorithm:", prim(graph, start_vertex))
# The total weight of this MST would be:
# 2 (A-B) + 1 (B-C) + 1 (B-D) + 1 (D-E) = 5



# Kruskal's

'''
Kruskal's Algorithm
- Maintain connected components in MST-so-far T in Union-Find
- T = 0
- for v in V, Make-Set(v) # every vertice lives in it's own singleton set
- Sort E by weight
- For e = {u, v} in E (inc. order by weight):
    - if Find-Set(u) not Find-Set(v):
        - T = T U {e} 
        - Union(u, v)

O(Sort(E) * Ealpha(V)  + V)
'''

'''
Correctness:
    - Assume T ⊆ T*
    - T -> T' = T U {e}
    - use greedy-choice property
    - with S = Connected-Component(u)
    => T' ⊆ T*'
'''

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

def kruskal(vertices, edges):
    # Initialize Union-Find
    uf = UnionFind(len(vertices))
    # Sort all edges in non-decreasing order
    edges.sort(key=lambda x: x[2])

    mst = []
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))

    return mst

vertices = [0, 1, 2, 3, 4]
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4), (2, 4, 8), (3, 4, 3)]
mst = kruskal(vertices, edges)
print("Edges in MST:", mst)

