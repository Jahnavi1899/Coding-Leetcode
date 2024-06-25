from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap) # heap with tasks count
        # a queue is required to identify when should the next task be appended in the heap and follows the interval constraint

        q = []
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                task = heapq.heappop(maxHeap)
                # since the current task has been processed, decrement its count
                cnt = 1 + task # adding 1 because the values in the heap are negative
                if cnt: 
                    q.append([cnt, time + n])
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.pop()[0])
        return time
    
n = 1
tasks = ["A","A","A", "B","B","B"]

obj = Solution()

print(obj.leastInterval(tasks, n))

