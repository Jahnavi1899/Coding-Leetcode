class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.checkParenthesis(0, s, 0, 0)

    def checkParenthesis(self, idx, s, closedp, openp):
        if idx == len(s):
            if closedp == openp:
                return True
            return

        if closedp == 0 and openp == 0:
            if s[idx] == ")":
                return False
            else:
                if self.checkParenthesis(idx+1, s, closedp, openp+1):
                    return True

        if s[idx] == "*":
            if self.checkParenthesis(idx+1, s, closedp, openp+1):
                return True
            if self.checkParenthesis(idx+1, s, closedp, openp):
                return True
            if self.checkParenthesis(idx+1, s, closedp + 1, openp):
                return True

        elif s[idx] == ")":
            if self.checkParenthesis(idx+1, s, closedp+1, openp):
                return True
        
        else:
            if self.checkParenthesis(idx+1, s, closedp, openp+1):
                return True
            

        return False
        
s = "(**("
obj = Solution()
print(obj.checkValidString(s))  