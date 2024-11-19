import collections
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int):
        l, r, n = 0, 0, len(s)
        maxLen, maxFreq = 0, 0
        hashmap = defaultdict(int)

        while r < n:
            hashmap[s[r]] += 1
            print(hashmap.values())
            maxFreq = max(maxFreq, hashmap[s[r]])

            while (r-l+1) - maxFreq > k:
                hashmap[s[l]] -= 1
                maxFreq = 0
                maxFreq = max(maxFreq, max(hashmap.values()))
                l += 1

            if (r-l+1) - maxFreq <= k:
                maxLen = max(maxLen, r-l+1)
                r += 1

        return maxLen

        
s = "AABABBA"
k = 1

obj = Solution()
print(obj.characterReplacement(s, k))