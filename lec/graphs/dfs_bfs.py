# implement dfs and bfs

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return str(self.val)


def bfs(s):
    q = deque()
    q.append(s)
    visited = set()
    while q:
        node = q.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            for child in node.children:
                q.append(child)
    print()


def dfs(s):
    stack = []
    stack.append(s)
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            for child in node.children:
                stack.append(child)
    print()


if __name__ == '__main__':
    # build a tree
    root = Node(0)
    root.add_child(Node(1))
    root.add_child(Node(2))
    root.add_child(Node(3))
    root.children[0].add_child(Node(4))
    root.children[0].add_child(Node(5))
    root.children[1].add_child(Node(6))
    root.children[1].add_child(Node(7))
    root.children[2].add_child(Node(8))
    root.children[2].add_child(Node(9))
    root.children[2].add_child(Node(10))
    root.children[2].children[0].add_child(Node(11))
    root.children[2].children[0].add_child(Node(12))
    root.children[2].children[0].add_child(Node(13))
    root.children[2].children[0].add_child(Node(14))
    root.children[2].children[0].add_child(Node(15))
    root.children[2].children[0].children[0].add_child(Node(16))
    root.children[2].children[0].children[0].add_child(Node(17))

    print('bfs:')
    bfs(root)

    print('dfs:')
    dfs(root)
