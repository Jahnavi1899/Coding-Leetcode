def findMin(nums):
    if nums[0] < nums[-1]:
        return nums[0]
    l, r = 0, len(nums)-1
    while l <= r:
        if nums[l] == nums[r]:
            return nums[l]
        mid = (l+r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        elif nums[mid] <= nums[l]:
            r = mid
    return nums[l]

nums = [3,4,5,1,2]
print(findMin(nums))
