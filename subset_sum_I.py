'''
    Time complexity: O(2^N) + O((2^N)log(2^N))
    Space complexity : O(2^N)
'''
def subset_sum_I(arr):
    res = []
    getSubsetSum(0, arr,len(arr), 0, res)
    res.sort()
    return res


def getSubsetSum(idx, arr, n, subsetSum, res):
    if idx == n:
        res.append(subsetSum)
        return
    
    # pick element
    subsetSum += arr[idx]
    getSubsetSum(idx+1, arr, n, subsetSum, res)

    # not pick the element
    subsetSum -= arr[idx]
    getSubsetSum(idx+1, arr, n, subsetSum, res)


arr = [3, 1, 2]
print(subset_sum_I(arr))