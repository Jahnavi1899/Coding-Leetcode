class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n)]

        return self.findMaxAmount(0, nums, dp)

    def findMaxAmount(self, idx, nums, dp):
        # base case
        # cache
        # main logic
        # return statement
        if idx >= len(nums):
            return 0
            
        if dp[idx] != -1:
            return dp[idx]

        pick = nums[idx] + self.findMaxAmount(idx+2, nums, dp)
        notpick = self.findMaxAmount(idx+1, nums, dp)

        dp[idx] = max(pick, notpick)
        return dp[idx]

nums = [2,7,9,3,1]
sol = Solution()
print(sol.rob(nums)) # 12