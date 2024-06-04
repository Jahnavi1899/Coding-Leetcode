def twoSumLessThanK(nums, k):
    nums.sort()
    l, r = 0, len(nums)-1
    max_sum = 0
    while l < r:
        num_sum = nums[l] + nums[r]
        if num_sum < k:
            if num_sum > max_sum:
                max_sum = num_sum
            l += 1
        else:
            r -= 1
    if max_sum == 0:
        return -1
    else:
        return max_sum
    
nums = [34,23,1,24,75,33,54,8]
print(twoSumLessThanK(nums, 60))