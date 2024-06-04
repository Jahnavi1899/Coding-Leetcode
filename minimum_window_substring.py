from collections import Counter

def minWindow(s, t):
    if len(t) > len(s) or t == "":
            return ""
    #initialise the dictionaries for storing the frequency of the chars in s and t
    freq_t, freq_window = {}, {}
    #store all frequencies of chars in t
    for c in t:
        freq_t[c] = 1 + freq_t.get(c ,0)
    have, need = 0, len(freq_t)
    l, minLen = 0, float("infinity")
    res = [-1, -1]
    for r in range(len(s)):
        freq_window[s[r]] = 1 + freq_window.get(s[r], 0) 
        if s[r] in freq_t and freq_window[s[r]] == freq_t[s[r]]:
            have += 1
        while have == need:
            if r-l+1 < minLen:
                minLen = r-l+1
                res = [l, r]
            freq_window[s[l]] -= 1
            if s[l] in freq_t and freq_window[s[l]] < freq_t[s[l]]:
                have -= 1
            l += 1
    l, r = res
    if minLen == float("infinity"):
        return ""
    else:
        return s[l:r+1]

s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s,t))