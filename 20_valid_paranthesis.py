class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis_map = {')': '(', ']':'[', '}':'{'}
        stack = []

        for p in s:
            if p not in paranthesis_map.keys():
                stack.append(p)
            elif paranthesis_map[p] == stack[-1]:
                stack.pop()

        if stack:
            return True
        else:
            return False        
        

s = "()"
obj = Solution()
print(obj.isValid(s))