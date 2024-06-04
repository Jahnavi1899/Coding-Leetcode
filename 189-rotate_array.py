class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        nums_dup = [0] * n
        while k+i < n:
            nums_dup[k+i] = nums[i]
            i += 1
        for j in range(k):
            nums_dup[j] = nums[i+j]
        # for i in range(n):
        #     nums[i] = nums_dup[i]
        nums = nums_dup
        print(nums)

nums = [-1, -100, 3, 99]
k = 2
obj = Solution()
print(obj.rotate(nums, k))
        