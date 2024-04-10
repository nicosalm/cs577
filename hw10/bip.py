class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def match(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


def matching(m, n, q, graph):
    return m, n, q, graph


def main():
    instance = int(input())
    res = ""

    for _ in range(instance):
        """
        m - nodes in A
        n - nodes in B
        q - edges
        """
        m, n, q = map(int, input().split())
        nodes = m + n + 2

        matrix = [[0] * nodes for _ in range(nodes)]
        for _ in range(q):
            i, j = map(int, input().split())
            matrix[i][j + m] = 1

        # Connect all nodes in set A to the super source (0) and all nodes in
        # set B to the super sink (nodes - 1)

        matrix[0][1:m + 1] = [1] * m
        for i in range(m + 1, m + n + 1):
            matrix[i][-1] = 1

        flow = Graph(matrix)
        maxFlow = flow.match(0, nodes - 1)
        perfect_matching = "N"
        if maxFlow == n:
            perfect_matching = "Y"

        res += f"{maxFlow} {perfect_matching}\n"

    print(res.rstrip())

if __name__ == "__main__":
    main()
