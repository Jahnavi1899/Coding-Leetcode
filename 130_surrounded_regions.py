class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        directions = [[1,0],[0,-1],[-1,0],[0,1]]

        for i in range(n):
            # for first row
            if board[0][i] == 'O' and visited[0][i] == 0:
                self.dfs(0, i, board, visited, directions, m, n)
            # for last row
            if board[m-1][i] == 'O' and visited[m-1][i] == 0:
                self.dfs(m-1, i, board, visited, directions, m, n)

        for j in range(m):
            # for first col
            if board[j][0] == 'O' and visited[j][0] == 0:
                self.dfs(j, 0, board, visited, directions, m, n)
            # for last col
            if board[j][n-1] == 'O' and visited[j][n-1] == 0:
                self.dfs(j, n-1, board, visited, directions, m, n)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and visited[i][j] == 0:
                    board[i][j] = 'X'

        return board

    def dfs(self, r, c, board, visited, directions, m, n):
        visited[r][c] = 1

        for dr, dc in directions:
            nrow = r + dr
            ncol = c + dc
            if(nrow in range(m) and 
               ncol in range(n) and 
               visited[nrow][ncol] == 0 and
               board[nrow][ncol] == 'O'):

               self.dfs(nrow, ncol, board, visited, directions, m, n)


        
board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]

obj = Solution()
obj.solve(board)
print(board)