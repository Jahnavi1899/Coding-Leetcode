class Solution:
    def getLargestOutlier(self, nums) -> int:
        hashmap = {}
        maxOutlier = float('-inf')

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        total = sum(nums)

        for i in range(len(nums)):
            temp = total - nums[i]
            if temp % 2 == 0:
                specialSum = temp // 2
                print(specialSum)
                if specialSum in hashmap:
                    if specialSum == nums[i] and hashmap[specialSum] == 1:
                        continue
                    else:
                        maxOutlier = max(maxOutlier, nums[i])
                else:
                    continue
                    
                      
            else:
                continue

        return maxOutlier
    
nums = [6,-31,50,-35,41,37,-42,13]
sol = Solution()
print(sol.getLargestOutlier(nums)) # 3