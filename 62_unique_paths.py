class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # top-down approach
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                up, left = 0, 0
                if i > 0:
                    up = dp[i-1][j]
                if j > 0:
                    left = dp[i][j-1]
                dp[i][j] = up+left
        print(dp)
        return dp[m-1][n-1]
    
m = 3
n = 7
obj = Solution()
print(obj.uniquePaths(m, n))