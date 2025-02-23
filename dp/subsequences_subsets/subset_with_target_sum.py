def subsetTargetSum(arr, target):
    n = len(arr)
    dp = [[False for _ in range(target+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = True

    for j in range(target+1):
        if arr[0] == j:
            dp[0][j] = True

    for i in range(1,n):
        for j in range(1, target+1):
            # not pick the element
            notpick = dp[i-1][j] # if the current element is not picked, then take the answer of the previous row

            # pick the element
            pick = 0
            if arr[i] <= j:
                pick = dp[i-1][j - arr[i]] # if the current element is picked, check if the remaining target was possible before 

            dp[i][j] = pick or notpick

    return dp[n-1][target]

def findSubset(idx, target, arr, dp):
    if target == 0:
        dp[idx][target] = True
        return dp[idx][target]
    
    if idx == 0:
        if arr[idx] == target:
            dp[idx][target] = True
        else:
            dp[idx][target] = False
        return dp[idx][target]
    
    if dp[idx][target] != -1:
        return dp[idx][target]
    
    # not pick the element
    notpick = findSubset(idx-1, target, arr, dp)

    # pick the element
    pick = 0
    if arr[idx] <= target:
        pick = findSubset(idx-1, target - arr[idx], arr, dp)

    dp[idx][target] = pick or notpick
    return dp[idx][target]

arr = [3, 34, 4, 12, 5, 2]
target = 9

print(subsetTargetSum(arr, target))