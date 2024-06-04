def searchMatrix(matrix, target):
    m,n = len(matrix), len(matrix[0])
    t, b = 0 , m-1
    while t <= b:
        mid_row = (t + b) // 2
        if target > matrix[mid_row][-1]:
            t = mid_row + 1
        elif target < matrix[mid_row][0]:
            b = mid_row - 1
        else:
            break
    l, r = 0, n-1
    while l <= r:
        mid_col = (l+r)//2
        if target == matrix[mid_row][mid_col]:
            return True
        elif target > matrix[mid_row][mid_col]:
            l = mid_col + 1
        else:
            r = mid_col - 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(searchMatrix(matrix, 13))
