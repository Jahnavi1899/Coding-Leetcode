def isIsomorphic(s, t):
    char_mapping = {}
    l = 0
    while l < len(s):
        if s[l] not in char_mapping:
            if t[l] not in char_mapping.values():
                char_mapping[s[l]] = t[l]
            else:
                return False
            print(char_mapping)
        elif char_mapping[s[l]] != t[l]:
            return False
        # else:
        #     return False
        
        # else:
        #     print(char_mapping[s[l]])
        #     print(t[l])
            
        #     if char_mapping[s[l]] != t[l]:
        #         return False
        l += 1
    return True

s = "badc"
t = "baba"
print(isIsomorphic(s,t))