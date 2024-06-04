class Solution:
    def solveNQueens(self, n):
        res = []
        board = [['.'] * n for _ in range(n)]
        self.alloteQueens(n, 0, res, board)
        return res

    def alloteQueens(self, n, col, res, board):
        if col == n:
            res.append(board.copy())
            return

        for row in range(n):
            if self.canPlaceQ(row, col, board, n) == True:
                board[row][col] = 'Q'
                self.alloteQueens(n, col+1, res, board)
                board[row][col] = "."

        
    def canPlaceQ(self, row, col, board, n):
        r = row
        c = col

        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        r = row
        c = col

        while c >= 0:
            if board[r][c] == "Q":
                return False
            c -= 1

        r = row
        c = col

        while r < n and c >= 0:
            if board[r][c] == "Q":
                return False
            r += 1
            c -= 1

        return True
    
obj = Solution()
n = 4
print(obj.solveNQueens(n))

         

        