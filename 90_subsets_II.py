def subsets2(arr):
    res = []
    arr.sort()
    getAllSubsets(0, arr, [], res)
    return res

def getAllSubsets(idx, arr, subset, res):
    # since the getAllSubsets method is claeed for only those indices which will form a unique subset, there fpr the subset can be appended into the result
    res.append(subset.copy())
    for i in range(idx, len(arr)):
        if i != idx and arr[i] == arr[i-1]:
            continue # do not select this index

        subset.append(arr[i])
        getAllSubsets(i+1, arr, subset, res)
        subset.pop()