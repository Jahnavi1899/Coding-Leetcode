'''
Determine the shortest path from the source to all the nodes in the graph.
Implementation using priority queue.
Not applicable to the graphs with negative weight cycles.

TC - Elog(V)
'''
import heapq

def dijstra_algo(source, graph):
    n = len(graph)
    dist = [float('inf') for _ in range(n)]

    priority_queue = []
    heapq.heappush(priority_queue, (0, source))
    dist[source] = 0

    while priority_queue:
        min_dist, node = heapq.heappop(priority_queue)
        for adj_node, weight in graph[node]:
            if dist[adj_node] > min_dist + weight:
                dist[adj_node] = min_dist + weight
                heapq.heappush(priority_queue, (dist[adj_node], adj_node))

    return dist

graph = [[[1, 9]], [[0, 9]]]
source = 0

print(dijstra_algo(source, graph))
