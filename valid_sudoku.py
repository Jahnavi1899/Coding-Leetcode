def isValidSudoku(board):
    board_size = 9
        
    for i in range(board_size):
        row_digits = []
        for j in range(board_size):
            digit = board[i][j]
            if digit != ".":
                if digit not in row_digits:
                    row_digits.append(digit)
                else:
                    return False
            
    for i in range(board_size):
        column_digits = []
        for j in range(board_size):
            digit = board[j][i]
            if digit != ".":
                if digit not in column_digits:
                    column_digits.append(digit)
                else:
                    return False

    for i in [0 ,3, 6]:
        block_digits = []
        for j in range(3):
            for k in range(3):
                digit = board[i+j][i+k]
                if digit != ".":
                    if digit not in block_digits:
                        block_digits.append(digit)
                    else:
                        return False

    print(row_digits)
    print(column_digits)
    print(block_digits)
    return True

board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
print(isValidSudoku(board))