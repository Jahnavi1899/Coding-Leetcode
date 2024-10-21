class Solution:
    def minFallingPathSum(self, matrix):
        row, col = len(matrix), len(matrix[0])
        dp = {}
        res = float('inf')
        for k in range(col):
            ans = self.minSum(matrix, row-1, k, row, col, dp)
            res = min(res, ans)
        print(dp)
        return res

    def minSum(self, matrix, i, j, row, col, dp):
        if j < 0 or j >= col:
            return float('inf')

        if i == 0:
            return matrix[0][j]
        

        if (i, j) in dp:
            return dp[(i,j)]

        up = matrix[i][j] + self.minSum(matrix, i-1, j, row, col, dp)
        l = matrix[i][j] + self.minSum(matrix, i-1, j-1, row, col, dp)
        r = matrix[i][j] + self.minSum(matrix, i-1, j+1, row, col, dp)

        dp[(i, j)] =  min(up, l, r)

        return dp[(i, j)]

class Solution:
    def minFallingPathSum(self, matrix):
        row, col = len(matrix), len(matrix[0])
        prev = [0 for _ in range(col)]
        curr = [0 for _ in range(col)]

        for j in range(col):
            prev[j] = matrix[0][j]
            
        for i in range(1, row):
            for j in range(col):
                l, r = float('inf'), float('inf')
                up = matrix[i][j] + prev[j]
                if j > 0:
                    l = matrix[i][j] + prev[j-1]
                if j < col-1:
                    r = matrix[i][j] + prev[j+1]
                curr[j] = min(up, l, r)
                prev = curr[:]

        return min(prev)

        

matrix = [[2,1,3],[6,5,4],[7,8,9]]
obj = Solution()
print(obj.minFallingPathSum(matrix))