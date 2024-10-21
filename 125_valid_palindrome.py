class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s:
            if char.isalnum():
                new_str += char.lower()
        left, right = 0, len(new_str)-1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        
s = "A man, a plan, a canal: Panama"
obj = Solution().isPalindrome(s)