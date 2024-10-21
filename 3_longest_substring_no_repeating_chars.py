class Solution:
    def lengthOfLongestSubstring(self, s):
        hashmap = {}
        l, r = 0, 0
        n = len(s)
        res = 0
        while l <= r and r < n:
            if s[r] in hashmap and hashmap[s[r]] > l:
                l = hashmap[s[r]] + 1
                hashmap[s[r]] = r
                res = max(res, r-l+1)
            else:
                hashmap[s[r]] = r
                res = max(res, r-l+1)
            r += 1
        return res
    

s = "abba"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))
