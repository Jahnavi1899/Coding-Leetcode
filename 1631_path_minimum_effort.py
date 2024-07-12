import heapq
class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        dist_matrix = [[float('inf') for _ in range(n)] for _ in range(m)]

        dist_matrix[0][0] = 0
        queue = [[0, 0, 0]]
        directions = [[1,0], [0,-1], [-1,0], [0, 1]]

        while queue:
            effort, r, c = heapq.heappop(queue)
            if r == m-1 and c == n-1:
                return effort
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if row in range(m) and col in range(n):
                    new_effort = max(effort, abs(heights[r][c] - heights[row][col]))
                    if new_effort < dist_matrix[row][col]:
                        dist_matrix[row][col] = new_effort
                        heapq.heappush(queue, [new_effort, row, col])
                        print([new_effort, row, col])


heights = [[1,10,6,7,9,10,4,9]]
#[[1,2,2],[3,8,2],[5,3,5]]

obj = Solution()
print(obj.minimumEffortPath(heights))


        