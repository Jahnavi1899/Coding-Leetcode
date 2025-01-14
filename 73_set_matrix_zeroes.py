class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        ans = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    if ans[i][j] != 0:
                        ans[i][j] = matrix[i][j]
                    else:
                        continue
                else:
                    r, c = 0, 0
                    while r < m:
                        ans[r][j] = 0
                        r += 1

                    while c < n:
                        ans[i][c] = 0
                        c += 1

        print(ans)

sol = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(matrix)

        
                    