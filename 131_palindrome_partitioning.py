def partition(s):
    res = []
    getSubstrings(0, s, [], res)
    return res
        

def getSubstrings(index, s, temp, res):
    if index == len(s):
        res.append(temp.copy())
        return
            
    for i in range(index, len(s)):
        if isPalindrome(s[index:i+1]):
            temp.append(s[index:i+1])
            getSubstrings(i+1, s, temp, res)
            temp.pop()


def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
        

s = "aab"
print(partition(s))