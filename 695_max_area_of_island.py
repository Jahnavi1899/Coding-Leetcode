class Solution:
    def maxAreaOfIsland(self, grid):
        n, m = len(grid), len(grid[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]

        maxArea = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    area = 0
                    self.dfs(i, j, grid, visited, n, m, area)
                    maxArea = max(area, maxArea)

        return maxArea


    def dfs(self, i, j, grid, visited, n, m, area):
        visited[i][j] = 1
        edges = [[0, 1], [0, -1], [1, 0], [-1,0]]
        for dr, dc in edges:
            nr, nc = i+dr, j+dc
            if(
                nr in range(n) and
                nc in range(m) and
                grid[nr][nc] == 1 and
                visited[nr][nc] == 0
            ):
                self.dfs(nr, nc, grid, visited, n, m, area+1)


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
obj = Solution()
print(obj.maxAreaOfIsland(grid))


        