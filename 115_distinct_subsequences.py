class Solution:
    def numDistinct(self, s: str, t: str):
        idx1, idx2 = len(s), len(t)
        return self.findSubsequences(idx1-1, idx2-1, s, t)

    def findSubsequences(self, idx1, idx2, s, t):
        if idx2 < 0:
            return 1
        if idx1 < 0:
            return 0

        if s[idx1] == t[idx2]:
            return self.findSubsequences(idx1-1, idx2-1, s, t) + self.findSubsequences(idx1-1, idx2, s, t)

        else:
            return self.findSubsequences(idx1-1, idx2, s, t)
        

s = "babgbag"
t = "bag"

obj = Solution()
print(obj.numDistinct(s, t))


        