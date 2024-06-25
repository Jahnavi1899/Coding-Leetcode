# this code exceeds the time complexity

import heapq 

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.length = 0

    def addNum(self, num: int) -> None:
        if not self.length:
            self.minHeap.append(num)
        else:
            heapq.heappush(self.minHeap, num)
        self.length += 1

    def findMedian(self) -> float:
        temp = self.minHeap.copy()
        res = []
        while temp:
            res.append(heapq.heappop(temp))
        median = 0
        mid = self.length // 2
        if self.length % 2 == 0:
            median = (res[mid-1] + res[mid])/2
        else:
            median = res[mid]
        return median
        


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(-1)
print(obj.findMedian())
obj.addNum(-2)
print(obj.findMedian())
obj.addNum(-3)
print(obj.findMedian())
obj.addNum(-4)
print(obj.findMedian())
obj.addNum(-5)
print(obj.findMedian())