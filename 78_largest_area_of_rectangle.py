class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = []
        ans = 0

        for i in range(len(heights)):
            # found next smaller element for the element on top of the stack
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                nse = i
                pse = stack[-1] if stack else -1 # the element on top of that stack after popping the topmost element will be the prev smaller element
                print("idx:", idx)
                ans = max(ans, heights[idx] * (nse-pse-1))
                print('nse:', nse)
                print('pse:', pse)
                print(ans)
            stack.append(i)

        
        while stack:
            nse = len(heights)
            idx = stack.pop()
            pse = stack[-1] if stack else -1
            ans = max(ans, heights[idx] * (nse-pse-1))

        return ans
    
heights = [2,1,5,6,2,3]
obj = Solution()
print(obj.largestRectangleArea(heights))
