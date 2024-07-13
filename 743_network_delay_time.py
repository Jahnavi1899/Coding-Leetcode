import heapq

class Solution:
    def networkDelayTime(self, times, n: int, k: int):
        graph = [[] for _ in range(n+1)]
        for edge in times:
            u, v, w = edge[0], edge[1], edge[2]
            graph[u].append([v, w])

        # print(graph)
        times = [float('inf') for _ in range(n+1)]
        pq = []

        times[k] = 0
        heapq.heappush(pq, [0, k])

        while pq:
            time, node = heapq.heappop(pq)
            for adj, t in graph[node]:
                if times[adj] > time + t:
                    times[adj] = time + t
                    heapq.heappush(pq, [times[adj], adj])

        for i in range(1, n+1):
            if times[i] == float('inf'):
                return -1
        return max(times[1:])

        
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

obj = Solution()
print(obj.networkDelayTime(times, n, k))