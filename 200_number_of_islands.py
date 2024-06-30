class Solution:
    def numIslands(self, grid) -> int:
        isVisited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in isVisited:
                    islands += 1
                    self.bfs(r, c, isVisited, grid)

        return islands

    def bfs(self, r, c, visited, grid):
        visited.add((r,c))
        queue = [[r,c]]
        while queue:
            row, col = queue.pop(0)
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for r1, c1 in directions:
                r2, c2 = r1+row, c1+col
                if r2 in range(len(grid)) and c2 in  range(len(grid[0])) and (r2, c2) not in visited and grid[r2][c2] == "1":
                    queue.append([r2, c2])
                    visited.add((r2, c2))

grid = [["1"]]

obj = Solution()
print(obj.numIslands(grid))

    
        