class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return self.findLengthOfLIS(0, -1, nums, n, dp)


    def findLengthOfLIS(self, i, prev, nums, n, dp):
        if i == n:
            return 0

        if dp[i][prev] != -1:
            return dp[i][prev]

        # not pick
        notPick = self.findLengthOfLIS(i+1, prev, nums, n, dp)

        # pick
        pick = 0
        if prev == -1 or nums[i] > nums[prev]:
            pick = 1 + self.findLengthOfLIS(i+1, i, nums, n, dp)

        dp[i][prev] = max(pick, notPick)
        return dp[i][prev]
        

nums = [0,1,0,3,2,3]
obj = Solution()
print(obj.lengthOfLIS(nums))