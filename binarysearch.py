class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums)-1
        # print(self.binarySearch(nums, target, l, r))
        return self.binarySearch(nums, target, l, r)
        
    def binarySearch(self, nums, target, l, r):
        if l < r:
            mid = (l+r)//2
            if target > nums[mid]:
                return self.binarySearch(nums, target, mid+1, r)
            else:
                return self.binarySearch(nums, target, l, mid-1)
            if nums[mid] == target:
            # print(mid)
                return mid
        
        elif target > nums[mid]:
            self.binarySearch(nums, target, mid+1, r)
        else:
            self.binarySearch(nums, target, l, mid-1)

nums = [-1,0,3,5,9,12]
target = 9
obj = Solution()
print(obj.search(nums, target))

        
        