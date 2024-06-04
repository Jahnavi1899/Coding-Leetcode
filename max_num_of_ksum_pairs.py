def maxOperations(nums, k):
    nums.sort()
    l, r = 0, len(nums)-1
    count = 0
    while l < r:
        if nums[l] + nums[r] == k:
            count += 1
            nums.remove(nums[l])
            nums.remove(nums[r])
            l += 1
            r -= 1
        elif nums[l] + nums[r] > k:
            r -= 1
        else:
            l += 1
    return count

nums = [3,1,3,4,3]
k = 6
print(maxOperations(nums, k))