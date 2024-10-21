import heapq

class Solution:
    def swimInWater(self, grid) -> int:
        n = len(grid)
        pq = [[0,0,0]]
        visited = set()
        visited.add((0,0))
        directions = [[1,0], [0, -1], [-1, 0], [0, 1]]

        while pq:
            elevation, r, c = heapq.heappop(pq)
            if r == n-1 and c == n-1:
                return elevation
            for dr, dc in directions:
                n_r, n_c = r+dr, c+dc
                if(
                    n_r >= 0 and n_r < n and
                    n_c >= 0 and n_c < n and
                    (n_r, n_c) not in visited
                ):
                    heapq.heappush(pq, [max(elevation, grid[n_r][n_c]), n_r, n_c])
                    visited.add((n_r, n_c))

        return 0

grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
obj = Solution()
print(obj.swimInWater(grid))
        