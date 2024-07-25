import heapq
def MST(graph):
    n = len(graph)
    pq = []
    visited = [0 for _ in range(n)]
    mst = []
    min_sum = 0

    heapq.heappush(pq, [0, 0, -1])

    while pq:
        weight, node, source = heapq.heappop(pq)
        if visited[node] != 1:
            visited[node] = 1
            min_sum += weight
            if source != -1:
                mst.append([node, source])
            for adj_w, adj_n in graph[node]:
                if visited[adj_n] == 0:
                    # visited[adj_n] = 1
                    heapq.heappush(pq, [adj_w, adj_n, node])

    return min_sum, mst

graph = [[[2,1],[1,2]], [[2,0],[1,2]], [[1,0],[1,1],[2,4],[2,3]], [[2,2],[1,4]], [[2,2],[1,3]]]

mst_sum, mst = MST(graph)

print(mst_sum)
print(mst)
