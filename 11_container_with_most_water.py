class Solution:
    def maxArea(self, height) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            if height[l] <= height[r]: 
                ans = max(ans, (height[l] * (r-l)))
                l += 1
            
            elif height[l] > height[r]:
                ans = max(ans, (height[r] * (r-l)))
                r -= 1
        return ans
    
height = [1,8,6,2,5,4,8,3,7]
obj = Solution()
print(obj.maxArea(height))
             