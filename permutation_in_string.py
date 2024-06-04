from collections import Counter

def checkInclusion(s1, s2):
    s1_char_freq = Counter(s1)
    s2_char_freq = {}
    l, r = 0, len(s1)-1
    while r < len(s2):
        cnt = Counter(s2[l:r+1])
        s2_char_freq = {k:v for k,v in cnt.items() if k in s1}

        print(cnt)
        print(s2_char_freq)
        if s2_char_freq == s1_char_freq:
            return True
        else:
            l += 1
            r += 1
    return False

s1 = "ab" 
s2 = "eidboaoo"
print(checkInclusion(s1, s2))