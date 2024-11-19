import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        matches = 0
        s1_map, s2_map = {ch: 0 for ch in string.ascii_lowercase}, {ch: 0 for ch in string.ascii_lowercase}

        for i in range(len(s1)):
            s1_map[s1[i]] = s1_map.get(s1[i], 0) + 1
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1

        for i in string.ascii_lowercase:
            if s1_map[i] == s2_map[i]:
                matches += 1
                
        l = 0
        for r in range(len(s1), len(s2)):
            s2_map[s2[r]] += 1
            if s2_map[s2[r]] == s1_map[s2[r]]:
                matches += 1
            elif s2_map[s2[r]] == s1_map[s2[r]] + 1:
                matches -= 1

            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == s1_map[s2[l]]:
                matches += 1
            elif s2_map[s2[l]] + 1 == s1_map[s2[l]]:
                matches -= 1
            l += 1

        print(s1_map)
        print(s2_map)
        if matches == 26:
            return True
        else:
            return False
        
s1 = "ab"
s2 = "eidbaooo"

obj = Solution()
print(obj.checkInclusion(s1, s2))



        


        

