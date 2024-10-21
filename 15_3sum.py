class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                l, r = i+1, n-1
                while l < r:
                    if nums[l] + nums[r] + nums[i] == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif nums[l] + nums[r] + nums[i] < 0:
                        l += 1
                    else:
                        r -= 1

        return res

nums = [-1,0,1,2,-1,-4]
obj = Solution()
print(obj.threeSum(nums))