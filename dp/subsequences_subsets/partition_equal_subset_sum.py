class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        n = len(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        prev = [False for _ in range(target + 1)]
        curr = [False for _ in range(target + 1)]

        for j in range(target+1):
            if nums[0] == j:
                prev[j] = True

        for i in range(1, n):
            for j in range(1, target+1):
                notpick = prev[j]
                pick = False

                if nums[i] <= j:
                    pick = prev[j - nums[i]]

                curr[j] = pick or notpick

            prev = curr

        return prev[target]
    
nums = [1,5,11,3]
print(Solution().canPartition(nums)) # True