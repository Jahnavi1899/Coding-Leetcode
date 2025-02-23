import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        pq = []

        for n1 in nums1:
            for n2 in nums2:
                numsum = n1 + n2
                if len(pq) < k:
                    heapq.heappush(pq, [-numsum, [n1, n2]])
                else:
                    heapq.heappush(pq, [-numsum, [n1, n2]])
                    heapq.heappop(pq)
                    

        print(pq)
        return []
    
nums1 = [1, 7, 11]
nums2 = [2, 4, 6]

sol = Solution()
sol.kSmallestPairs(nums1, nums2, 3)


        