from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank) -> int:
        bankSet = set(bank)
        q = deque([startGene])
        genes = "ACGT"

        mutationLen = 0     

        while q:
            for _ in range(len(q)):
                top = q.popleft()
                print('top:', top)
                for i in range(8):
                    for ch in genes:
                        newMut = top[:i] + ch + top[i+1:] 
                        print(newMut)
                        if bankSet:
                            if newMut in bankSet:
                                if newMut == endGene:
                                    return mutationLen + 1
                                else:
                                    q.append(newMut)
                                    bankSet.remove(newMut)
            mutationLen += 1
        return -1
                            
startGene = "AACCGGTT"
endGene = "AAACGGTA"

bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
sol = Solution()
print(sol.minMutation(startGene, endGene, bank))