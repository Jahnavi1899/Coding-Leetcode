def permute(nums):
    res = []
    nums_map = [False] * len(nums)
    getAllPermutations(nums, [], res, nums_map)
    return res

def getAllPermutations(nums, temp, res, nums_map):
    if len(temp) == len(nums):
        res.append(temp)
        return

    for i in range(len(nums)):
        if nums_map[i] != True:
            temp.append(nums[i])
            nums_map[i] = True

            getAllPermutations(nums, temp, res, nums_map)
            nums_map[i] = False
            temp.pop()


nums = [1,2,3]
print(permute(nums))