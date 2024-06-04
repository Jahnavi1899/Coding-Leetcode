class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.solveGrid(board)
        return board


    def solveGrid(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    for val in "123456789":
                        if self.isValid(board, val, i, j):
                            board[i][j] = val
                            res = self.solveGrid(board)
                            if res:
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True

    def isValid(self, board, val, row, col):
        for i in range(9):
            # check for the row
            if board[row][i] == val:
                return False

            # check for col
            if board[i][col] == val:
                return False

            # check for 3X3 grid
            if board[3 * (row//3) + i // 3][3 * (col//3) + i%3] == val:
                return False

        return True
    
obj = Solution()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(obj.solveSudoku(board))
