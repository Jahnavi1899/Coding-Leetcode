def nextGreaterElement(height):
    n = len(height)
    stack = []
    ans = [-1 for _ in range(n)]

    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= height[i]:
            stack.pop()
        if stack and stack[-1] > height[i]:
            ans[i] = stack[-1]
        stack.append(height[i])
    return ans
            


height = [1,8,6,2,5,4,8,3,7]
print(nextGreaterElement(height))