# print all contiguous and non-continguous subsequences of an array
# at max depth 4 functions are there in the stack, so how is the space complexity O(N)???
def printAllSubsequences(idx, arr, n, lst):
    if idx >= n:
        print(arr)
        return
    arr.append(lst[idx])
    printAllSubsequences(idx+1, arr, n, lst)
    arr.pop()
    printAllSubsequences(idx+1, arr, n, lst)

lst = [3, 1, 2]
#printAllSubsequences(0, [], len(lst), lst)

def printSubsequencesSumK(idx, arr, n, lst, k, s):
    if idx == n:
        if s == k:
            print(arr)
        return
    arr.append(lst[idx])
    s += lst[idx]
    printSubsequencesSumK(idx+1, arr, n, lst, k, s)
    s -= lst[idx]
    arr.pop()
    
    printSubsequencesSumK(idx+1, arr, n, lst, k, s)

lst = [1, 1, 2]
# printSubsequencesSumK(0, [], len(lst), lst, 2, 0)

def printOneSubsequencesSumK(idx, arr, n, lst, k, s):
    if idx == n:
        if s == k:
            print(arr)
            return True
        return False
    arr.append(lst[idx])
    s += lst[idx]
    if printOneSubsequencesSumK(idx+1, arr, n, lst, k, s) == True:
        return True
    
    s -= lst[idx]
    arr.pop()
    
    if printOneSubsequencesSumK(idx+1, arr, n, lst, k, s) == True:
        return True
    return False

lst = [1, 1, 2]
#printOneSubsequencesSumK(0, [], len(lst), lst, 2, 0)

def printCountSubsequencesSumK(idx, n, lst, k, s):
    if idx == n:
        if s == k:
            return 1
        return 0

    s += lst[idx]
    l = printCountSubsequencesSumK(idx+1, n, lst, k, s)
    s -= lst[idx]   
    r = printCountSubsequencesSumK(idx+1, n, lst, k, s)

    return l + r

lst = [1, 2, 2, 1]
print(printCountSubsequencesSumK(0,len(lst), lst, 2, 0))
