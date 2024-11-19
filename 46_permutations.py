class Solution:
    def permute(self, nums) :
        res, n = [], len(nums)
        idx_map = [False for _ in range(n)]

        self.findPermutations(nums, res, n, idx_map, [])
        return res

    def findPermutations(self, nums, res, n, idx_map, temp):
        if len(temp) == n:
            res.append(temp.copy())
            return

        for i in range(n):
            if not idx_map[i]:
                temp.append(nums[i])
                idx_map[i] = True
                self.findPermutations(nums, res, n, idx_map, temp)
                temp.pop()
                idx_map[i] = False

nums = [1,2,3]
obj = Solution()
print(obj.permute(nums))


