class Solution:
    def generateParenthesis(self, n: int):
        res = []
        self.getParanthesis(0, 0, n, [], res)
        return res

    def getParanthesis(self, openCnt, closeCnt, n, stack, res):
        if openCnt == closeCnt and openCnt == n and closeCnt == n:
            res.append("".join(stack))
            return

        if openCnt < n:
            stack.append("(")
            self.getParanthesis(openCnt + 1, closeCnt, n, stack, res)
            stack.pop()

        if closeCnt < openCnt:
            stack.append(")")
            self.getParanthesis(openCnt, closeCnt + 1, n, stack, res)

n = 3
obj = Solution()
print(obj.generateParenthesis(n))

        