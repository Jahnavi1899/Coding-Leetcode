class Solution:
    def maxProfit(self, prices) -> int:
        stack, profit = [], 0
        for p in prices:
            if not stack:
                stack.append(p)
                print(stack)
            else:
                if p > stack[-1]:
                    profit += p - stack[-1]
                    stack.append(p)
                    print(profit)
                else:
                    while stack:
                        stack.pop()
                    stack.append(p)
                    print(stack)
        return profit

prices = [7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(prices)) # 7