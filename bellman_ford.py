# TC: O(V*E)
def bellman_ford(source, graph, n):
    dist = [float('inf') for _ in range(n)]
    dist[source] = 0

    for _ in range(n-1):
        for edge in graph:
            u, v, w = edge[0], edge[1], edge[2]
            # do relaxation operation
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
        
    for edge in graph:
        u, v, w = edge[0], edge[1], edge[2]
            # do relaxation operation
        if dist[v] != float('inf') and dist[v] > dist[u] + w:
                return -1
    return dist


graph = [[0, 1, 5], [1,2,-2],[1,5,-3],[5,3,1],[3,2,6],[4,3,-2],[2,4,3]]
print(bellman_ford(0, graph, 6))