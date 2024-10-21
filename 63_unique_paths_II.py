class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0 and obstacleGrid[i][j] != 1:
                    dp[i][j] = 1
                    continue
                top, left = 0, 0
                if i > 0:
                    top = dp[i-1][j]
                if j > 0:
                    left = dp[i][j-1]
                dp[i][j] = top + left
        return dp[m-1][n-1]

    def findUniquePathNoObstacle(self, i, j, obstacleGrid, dp):
        if i >= 0 and j >= 0 and obstacleGrid[i][j] == 1:
            return 0

        if i == 0 and j == 0:
            return 1

        if i < 0 or j < 0 :
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        up = self.findUniquePathNoObstacle(i-1, j, obstacleGrid, dp)
        left = self.findUniquePathNoObstacle(i, j-1, obstacleGrid, dp)
        dp[i][j] = up+left
        return dp[i][j]
        

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obj = Solution()
print(obj.uniquePathsWithObstacles(obstacleGrid))
