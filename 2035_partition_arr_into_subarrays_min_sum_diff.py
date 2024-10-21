# class Solution:
#     def minimumDifference(self, nums):
#         target = sum(nums)
#         n = len(nums)
#         dp = [[-1 for _ in range(target+1)] for _ in range(n)]
#         self.findSubsets(n-1, target, nums, dp)
#         print(dp)
#         return 0

#     def findSubsets(self, idx, target, nums, dp):
#         if target == 0:
#             return True
#         if idx == 0:
#             return nums[0] == target
#         print(target)
#         if dp[idx][target] != -1:
#             return dp[idx][target]

#         notPick = self.findSubsets(idx-1, target, nums, dp)
#         pick = False
#         if nums[idx] <= target:
#             pick = self.findSubsets(idx-1, target-nums[idx], nums, dp)
        
#         dp[idx][target] = pick or notPick
#         return dp[idx][target]
    

# nums = [3,9,7,3]
# obj = Solution()

# print(obj.minimumDifference(nums))


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        res = []
        if root:
            queue = [root]
            while queue:
                n = len(queue)
                temp = []
                for i in range(n):
                    top = queue.pop()
                    temp.append(top.val)
                    if top.left:
                        queue.append(top.left)
                    if top.right:
                        queue.append(top.right)
                res.append(temp.copy())
        return res
    
root = [3,9,20,None,None,15,7]
obj = Solution().levelOrder(root)
print(obj)

        