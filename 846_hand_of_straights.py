from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand, groupSize: int) -> bool:
        if len(hand) % groupSize == 0:
            freqMap = Counter(hand)
            minHeap = [k for k, v in freqMap.items()] # heap of unique elements from the input
            heapq.heapify(minHeap)

            while minHeap:
                minElement = minHeap[0]
                for i in range(minElement, minElement+groupSize):
                    if i not in freqMap:
                        return False
                    freqMap[i] -= 1
                    if freqMap[i] == 0:
                        if i != minHeap[0]:
                            return False
                        heapq.heappop(minHeap)
            return True
        

hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3

obj = Solution()
print(obj.isNStraightHand(hand, groupSize))
                

        