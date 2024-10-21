class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        rev_s = s[::-1]
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        ans = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == rev_s[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    ans = max(dp[i][j], ans)
                else:
                    dp[i][j] = 0
        ans_str = ""
        for _ in range(ans):
            ans_str += '#'
        index = ans-1
        while i > 0 or j > 0:
            if s[i-1] == rev_s[j-1]:
                ans_str = s[i-1] + ans_str[:-1]
                print(ans_str)
                index -= 1
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        return ans_str

s = "aacabdkacaa"
obj = Solution()
print(obj.longestPalindrome(s))