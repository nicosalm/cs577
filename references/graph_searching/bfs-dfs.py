# dfs-bfs.py

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None


# BFS, parameters: G, the graph, s, the starting node
# Runtime: O(V + E)
def bfs(G, s):
    queue = []
    queue.append(s)
    s.visited = True

    while queue:
        actualNode = queue.pop(0)
        print("%s " % actualNode.name)

        for n in actualNode.adjacencyList:
            if not n.visited:
                n.visited = True
                queue.append(n)


# DFS, parameters: G, the graph, s, the starting node
# Runtime: O(V + E)
def dfs(G, s):
    s.visited = True
    print("%s " % s.name)

    for n in s.adjacencyList:
        if not n.visited:
            dfs(G, n)


def test():

    # Create nodes
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    G = [node1, node2, node3, node4, node5]

    # Create edges
    node1.adjacencyList.append(node2)
    node1.adjacencyList.append(node3)
    node2.adjacencyList.append(node4)
    node4.adjacencyList.append(node5)

    # BFS
    print("BFS")
    bfs(G, node1)

    # Reset nodes
    for node in G:
        node.visited = False

    # DFS
    print("DFS")
    dfs(G, node1)


test()
