class Solution:
    def search(self, nums, target):
        l, h = 0, len(nums)-1

        while l <= h:
            mid = (l+h) // 2
            if nums[mid] == target:
                return target

            if nums[l] <= nums[mid]:
                if target >= nums[l] and target <= nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if target >= nums[mid] and target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
        return -1
    
nums = [4,5,6,7,0,1,2]
target = 0
obj = Solution()
print(obj.search(nums, target))
        
        
        
            