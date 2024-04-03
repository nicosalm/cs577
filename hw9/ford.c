// ford-fulkerson algorithm

/** 
* Implement the Ford-Fulkerson algorithm in O(mF) time, where F is the max
* flow value and m is the number of edges in the graph.
* 
* Use BFS or DFS to find augmenting paths.
*
* The input begins with a positivei integer giving the # of instances
* which follow; for each instance, there will be two integers > 0, n and m,
* indicating the number of nodes and edges in the graph. Following this, there
* will be |m| additional lines describing the edges. Each edge line consists
* of a number indicating the src node, a number indicating the dest node, and
* a capacity c(0 <= c <= 100) for the edge. The nodes are not listed
* separately, but are numbered {1 ... n}.
*
**/

// sample input:
// 2
// 3 2
// 2 3 4
// 1 2 5
// 6 9
// 1 2 9
// 1 3 4
// 2 4 1
// 2 5 6
// 3 4 4
// 3 5 5
// 4 6 8
// 5 6 5
// 5 6 3

// sample output:
// 4
// 11

#include <stdio.h>
#include <string.h>
#include <limits.h>

#define MAX_NODES 101
#define MAX_EDGES 1000

int n, m;
int capacity[MAX_NODES][MAX_NODES];
int flow[MAX_NODES][MAX_NODES];
int residual[MAX_NODES][MAX_NODES];
int parent[MAX_NODES];
int visited[MAX_NODES];

int min(int a, int b) {
    return a < b ? a : b;
}

int bfs(int src, int sink) {
    memset(visited, 0, sizeof(visited));
    memset(parent, -1, sizeof(parent));
    
    int queue[MAX_NODES], front = 0, rear = 0;
    queue[rear++] = src;
    visited[src] = 1;
    
    while (front < rear) {
        int u = queue[front++];
        for (int v = 1; v <= n; v++) {
            if (!visited[v] && residual[u][v] > 0) {
                parent[v] = u;
                visited[v] = 1;
                queue[rear++] = v;
                if (v == sink) return 1; // found a path to the sink!
            }
        }
    }
    return 0; // no path found
}

int ford_fulkerson(int src, int sink) {
    int max_flow = 0;

    // init residual graph
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            residual[i][j] = capacity[i][j];
        }
    }

    // while there is a path from source to sink
    while (bfs(src, sink)) {
        int path_flow = INT_MAX;

        // find the maximum flow through the path found.
        for (int v = sink; v != src; v = parent[v]) {
            int u = parent[v];
            path_flow = min(path_flow, residual[u][v]);
        }

        // update residual capacities of the edges and reverse edges
        for (int v = sink; v != src; v = parent[v]) {
            int u = parent[v];
            residual[u][v] -= path_flow;
            residual[v][u] += path_flow;
        }
        max_flow += path_flow;
    }
    return max_flow;
}

int main() {
    int t, u, v, c;
    scanf("%d", &t);

    while (t--) {
        scanf("%d %d", &n, &m);
        memset(capacity, 0, sizeof(capacity));

        for (int i = 0; i < m; i++) {
            scanf("%d %d %d", &u, &v, &c);
            capacity[u][v] += c;
        }

        printf("%d\n", ford_fulkerson(1, n));
    }
    return 0;
}

// time complexity: O(mF)
