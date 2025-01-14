from collections import defaultdict

def minWindow(s: str, t: str) -> str:
    m, n = len(s), len(t)
    l, r = 0, 0
    cnt, idx = 0, -1
    minlen = float('inf')
    countmap = defaultdict(int)

    for ch in t:
        countmap[ch] += 1

    while r < m:
        if countmap[s[r]] > 0:
            cnt += 1
        countmap[s[r]] -= 1
            
        while cnt == n:
            minlen = min(r-l+1, minlen)
            idx = l

            countmap[s[l]] += 1
            if countmap[s[l]] > 0:
                cnt -= 1
            l += 1
        print("l:", l)
        print("r:", r)
            
        r += 1
    if idx == -1:
        return ""
    
    return s[idx: idx+minlen]
    
s = "cabwefgewcwaefgcf"
t = "cae"

print(minWindow(s, t))
        