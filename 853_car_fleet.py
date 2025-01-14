class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append([position[i], speed[i]])
        
        pairs.sort(reverse = True)
        stack = []

        for p, s in pairs:
            val = (target - p) / s
            stack.append(val)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        
position = [4,2,0]
speed = [1,2,4]
target = 100

obj = Solution()
print(obj.carFleet(target, position, speed))