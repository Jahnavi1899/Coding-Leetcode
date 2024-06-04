def findMin(nums):
    # binary search
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l + r) // 2
        if l == r:
            return nums[l]
        elif nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid - 1
        
nums = [3,4,5,1,2]
print(findMin(nums))


