def shortestPath(n, graph, source):
    visited = [0 for _ in range(n)]
    stack = []
    
 
    # find the toposort
    # O(V+E)
    for i in range(n):
        if visited[i] == 0:
            dfs_toposort(i, visited, stack, graph)

    # find the distance
    dist = [float('inf') for _ in range(n)]
    dist[source] = 0 # dist is storing the minimum distance from the source to the node with index value

    # updating the dist matrix to store the min distance from between source and adj via node
    # O(V+E)
    while stack:
        node = stack.pop()
        for adj, weight in graph[node]:
            if dist[node] + weight < dist[adj]:
                dist[adj] = dist[node] + weight
    return dist 

def dfs_toposort(node, visited, stack, graph):
    visited[node] = 1
    for adj, weight in graph[node]:
        if visited[adj] == 0:
            dfs_toposort(adj, visited, stack, graph)
    stack.append(node)


graph = [[[1,2]], [[3,1]], [[3,3]], [], [[0,3],[2,1]], [[4,1]], [[4,2], [5,3]]]
n = 7
source = 6

print(shortestPath(n, graph, source))
