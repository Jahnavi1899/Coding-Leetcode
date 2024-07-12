import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int):
        adjList = [[] for _ in range(n)]
        min_price = [float('inf') for _ in range(n)]
        min_price[src] = 0
        pq = []
        heapq.heappush(pq, [0, src, 0])

        for source, dest, price in flights:
            adjList[source].append([dest, price])

        while pq:
            stops, node, price = heapq.heappop(pq)
            if stops > k:
                continue
            for adj, cost in adjList[node]:
                if min_price[adj] > price + cost and stops <= k:
                    min_price[adj] = price + cost
                    heapq.heappush(pq, [stops+1, adj, min_price[adj]])

        print(min_price)
        if min_price[dst] == float('inf'):
            return -1
        else:
            return min_price[dst]
        
n = 4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1

obj = Solution()
print(obj.findCheapestPrice(n, flights, src, dst, k))

