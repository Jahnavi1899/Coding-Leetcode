def combinationSum(candidates, target):
    # try all the combinations using recursion
    result = []
    getCombinations(0, candidates, target, [], result, 0)
    return result


def getCombinations(index, candidates, target, temp, result, temp_sum):
    if temp_sum == target:
        result.append(temp.copy()) # because we are using a single temp variable which keeps changing
        return
    if index >= len(candidates) or temp_sum > target:
        return
    

    # pick the element
    temp.append(candidates[index])
    getCombinations(index, candidates, target, temp, result, temp_sum + candidates[index])
    # do not pick the element
    temp.pop()
    getCombinations(index+1, candidates, target, temp, result, temp_sum)


arr = [8, 7, 4, 3]
target = 11
print(combinationSum(arr, target))