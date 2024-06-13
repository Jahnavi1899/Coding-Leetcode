
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        dq = deque()
        res = []
        for i in range(len(nums)):
            # check if there is any element in the deque that is out of bounds
            print(i)
            if dq and dq[0] == i - k:
                dq.popleft()

            # check and remove the elements from the end which violate the decreasing order of the deque
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)
            if i >= k-1:
                res.append(nums[dq[0]])

        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3

obj = Solution()
print(obj.maxSlidingWindow(nums, k))