def exist(board, word):
    m, n = len(board), len(board[0])
    count = 0

    for i in range(m):
        flag = False
        for j in range(n):
            if board[i][j] == word[0]:
                if checkWord(i,j, board, word, count) == True:
                    return True
    return False



def checkWord(idx1, idx2, board, word, count):
    if count == len(word):
        return True
    
    if idx1 < 0 or idx1 >= len(board) or idx2 < 0 or idx2 >= len(board[0]) or board[idx1][idx2] == "." or board[idx1][idx2] != word[count]:
        return False
    
    c = board[idx1][idx2]
    board[idx1][idx2] = "."

    # self.checkWord(idx1, idx2, board, word, count)
    left = checkWord(idx1-1, idx2, board, word, count+1)
    top = checkWord(idx1, idx2-1, board, word, count+1)
    right = checkWord(idx1+1, idx2, board, word, count+1)
    bottom = checkWord(idx1, idx2+1, board, word, count+1)

    board[idx1][idx2] = c

    return left or top or right or bottom

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

print(exist(board, word))
