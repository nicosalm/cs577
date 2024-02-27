# dijkstra.py

import heapq


class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def add_edge(self, frm, to, cost):
        self.edges.append((frm, to, cost))

    def dijkstra(self, start, end):
        q, seen = [(0, start, [])], set()
        while q:
            (cost, v, path) = heapq.heappop(q)
            if v not in seen:
                path = path + [v]
                seen.add(v)
                if v == end:
                    return (cost, path)
                for c, neighbour, w in self.edges:
                    if c == v and neighbour not in seen:
                        heapq.heappush(q, (cost + w, neighbour, path))
        return float("inf")


def main():
    g = Graph()
    g.add_vertex('A', ['B', 'C'])
    g.add_vertex('B', ['A', 'C', 'D'])
    g.add_vertex('C', ['A', 'B', 'D', 'E'])
    g.add_vertex('D', ['B', 'C', 'E', 'F'])
    g.add_vertex('E', ['C', 'D'])
    g.add_vertex('F', ['D'])

    for v in g.vertices:
        for neighbour in g.vertices[v]:
            g.add_edge(v, neighbour, 1)

    print("=== Dijkstra ===")
    print(g.dijkstra('A', 'F'))


if __name__ == "__main__":
    main()
