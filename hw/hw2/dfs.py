# dfs.py

import sys


def zoom():
    return sys.stdin.read().splitlines()


data = zoom()
iterator = iter(data)

count = int(next(iterator))

instances = []
for _ in range(count):
    instance = {}
    nodeCount = int(next(iterator))
    for _ in range(nodeCount):
        split = next(iterator).split()
        instance[split[0]] = split[1:]
    instances.append(instance)


def dfs(visited, traversal, instance, node):
    if node not in visited:
        visited.add(node)
        traversal.append(node)
        for neighbour in instance.get(node, []):
            dfs(visited, traversal, instance, neighbour)


for instance in instances:
    visited = set()
    traversal = []
    nodes = list(instance.keys())
    for node in nodes:
        if node not in visited:
            dfs(visited, traversal, instance, node)
    print(" ".join(traversal))
