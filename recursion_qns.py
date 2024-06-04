def printName(n, N):
    if n == N:
        return
    else:
        print(n)
        printName(n+1, N)

N = 5
#printName(0,N)

def printLinear(i, N):
    if i >= N:
        return
    else:
        print(i+1)
        printLinear(i+1, N)

# printLinear(0,N)

# print from N to 1 without using i-1 in the function

def printLinear2(i, N):
    if i > N:
        return
    printLinear2(i+1, N)
    print(i)

#printLinear2(1,3)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

#print(factorial(5))

# swap an array using recursion
def arrSwap(arr, l, r):
    if l >= r:
        return arr
    arr[l], arr[r] = arr[r], arr[l]
    #print(arr)
    return arrSwap(arr, l+1, r-1)

arr = [1,3,5,7,9]
print(arrSwap(arr, 0, len(arr)-1))

def palindrome(string, l, r):
    if l >= r:
        return True
    if string[ l] != string[r]:
        return False
    return palindrome(string, l+1, r-1)

def merge(arr, low, mid, high):
    l = low
    r = mid + 1
    temp = []
    while l <= mid and r <= high:
        if arr[l] > arr[r]:
            temp.append(arr[r])
            r += 1

        else:
            temp.append(arr[l])
            l += 1
    while l <= mid:
        temp.append(arr[l])
        l += 1
    
    while r <= high:
        temp.append(arr[r])
        r += 1

    for i in range(low, high+1):
        arr[i] = temp[i-low]




def mergeSort(arr, low, high):
    if low == high:
        return
    mid = (low + high) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)


arr = [2, 4, 6, 1, 4, 3, 7]
# mergeSort(arr, 0, len(arr)-1)

# print(arr)

def quicksort(arr, low, high):
    if low < high:
        partition = partition_index(arr, low, high)
        quicksort(arr, low, partition-1)
        quicksort(arr, partition+1, high)

def partition_index(arr, low, high):
    pivot = low
    i, j = low, high
    while i < j:
        while arr[i] <= arr[pivot] and i <= high:
            i += 1
        while arr[j] > arr[pivot] and j >= low:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j

def quickSort(arr, low, high):
    if low < high:
        partition = partition_index(arr, low, high)
        quickSort(arr, low, partition-1)
        quickSort(arr, partition+1, high)

quickSort(arr, 0, len(arr)-1)
print(arr)

