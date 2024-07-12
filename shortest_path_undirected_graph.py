def shortest_path(source, graph):
    n = len(graph)
    min_dist = [float('inf') for _ in range(n)]
    min_dist[source] = 0

    queue = [[source, 0]]
    while queue:
        node, dist = queue.pop(0)
        for adj in graph[node]:
            if min_dist[adj] > dist + 1:
                min_dist[adj] = dist + 1
                queue.append([adj, min_dist[adj]])

    return min_dist

graph = [[1,3], [0,2], [1,6], [0,4], [3,5], [4,6], [2,5,7,8], [6,8], [6,7]]
print(shortest_path(0, graph))

