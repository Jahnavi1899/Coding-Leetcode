def repeatedSubstringPattern(s):
    substrings = []
    n = len(s)//2
    print(n)
    for i in range(n):
        for j in range(i+1, n+1):
            # print(i,j)
            substr = s[i:j]
            if len(s) % len(substr) == 0:
                num_repeat = len(s)//len(substr)
                repeat_str = ""
                while num_repeat != 0:
                    repeat_str += s[i:j]
                    num_repeat -= 1
                if repeat_str == s:
                    substrings.append(s[i:j])
                    return True
                    
    print(substrings)
    return False

print(repeatedSubstringPattern("abab"))

        