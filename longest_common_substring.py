class Solution:
    def longestCommonSubstring(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        prev = [0 for _ in range(m+1)]
        curr = [0 for _ in range(m+1)]
        ans = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = 1 + prev[j-1]
                    ans = max(ans, curr[j])
                else:
                    curr[j] = 0
            prev = curr[:]
        return ans
    

s1, s2 = "abcd", "abkd"
obj = Solution()
print(obj.longestCommonSubstring(s1, s2))