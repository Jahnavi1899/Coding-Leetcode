class Solution:
    def orangesRotting(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        minTime = 0
        freshOranges = 0
        queue = []

        # counting the number of fresh and adding the rotten oranges in the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append([r,c])
                if grid[r][c] == 1:
                    freshOranges += 1

        adj_nodes = [[1,0],[-1,0],[0,1],[0,-1]]

        while queue and freshOranges > 0:
            queue_len = len(queue)
            for _ in range(queue_len):
                front_r, front_c = queue.pop(0)

                for adj_r, adj_c in adj_nodes:
                    neigh_r, neigh_c = front_r + adj_r, front_c + adj_c

                    if (neigh_r >= 0 and neigh_r < rows) and (neigh_c >= 0 and neigh_c < cols) and (grid[neigh_r][neigh_c] == 1):
                       
                        queue.append([neigh_r, neigh_c])
                        grid[neigh_r][neigh_c] = 2
                        freshOranges -= 1

            minTime += 1
            
        if freshOranges == 0:
            return minTime
        return -1
        
        
grid = [[2,1,1],[1,1,0],[0,1,1]]
obj = Solution()
print(obj.orangesRotting(grid))