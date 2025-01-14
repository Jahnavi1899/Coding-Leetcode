class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        
        while l < r:
            if not s[l].isalpha():
                l += 1
                continue
            if not s[r].isalpha():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        