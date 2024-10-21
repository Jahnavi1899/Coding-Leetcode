# TC : O(2^n)
# SC : O(N)
def all_subsequences(idx, nums, temp, res):
    if idx == len(nums):
        res.append(temp.copy())
        return
    
    # pick the index value
    temp.append(nums[idx])
    all_subsequences(idx+1, nums, temp, res)

    # do not pick the index
    temp.pop()
    all_subsequences(idx+1, nums, temp, res)

def subsequences_sum(idx, nums, temp, res, k, sum_val):
    if sum_val == k:
        res.append(temp.copy())
        return
    if sum_val > k:
        return
    
    # pick the index value
    sum_val += nums[idx]
    temp.append(nums[idx])
    all_subsequences(idx+1, nums, temp, res)

    # do not pick the index
    temp.pop()
    all_subsequences(idx+1, nums, temp, res)


nums = [3,1,2]
res = []
all_subsequences(0, nums, [], res)
print(res)