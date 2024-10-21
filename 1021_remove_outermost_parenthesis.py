class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        primitive_strings = []
        stack = []
        temp = ""
        for p in s:
            if p == "(":
                stack.append(p)
            elif p == ")" :
                top = stack.pop()
            temp += p
            if len(stack) == 0:
                primitive_strings.append(temp)
                temp = ""

            
        print(stack)
        return ""



        
s = "(()())(())"
obj = Solution()
print(obj.removeOuterParentheses(s))