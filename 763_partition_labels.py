class Solution:
    def partitionLabels(self, s: str):
        hashmap = {} # O(26)
        # store the last occurence of each unique character
        # O(n)
        for i in range(len(s)):
            hashmap[s[i]] = i

        lenOfPartition = 0
        partitionEnd = -1
        r = 0
        res = []

        while r < len(s):
            if r == partitionEnd:
                res.append(lenOfPartition+1)
                lenOfPartition = 0
            else:
                lenOfPartition += 1
                partitionEnd = max(partitionEnd, hashmap[s[r]])
            r += 1

        return res
    

s = "ababcbacadefegdehijhklij"
obj = Solution()
print(obj.partitionLabels(s))