class Solution:
    def searchMatrix(self, matrix, target):

        m, n = len(matrix), len(matrix[0])
        lr, lc = 0, 0
        rr, rc = m-1, n-1

        while lr <= rr and lc <= rc:
            mid_r, mid_c = (lr+rr)//2, (lc+rc)//2

            if matrix[mid_r][mid_c] == target:
                return True

            elif matrix[mid_r][mid_c] < target:
                if mid_c == n-1:
                    lr = mid_r + 1
                    lc = 0
                else:
                    lc = mid_c + 1

            else:
                if mid_c == 0:
                    rr = mid_r - 1
                    rc = n-1
                else:
                    rc = mid_c - 1

        return False
    
matrix = [[1,1]]
target = 2

sol = Solution()
print(sol.searchMatrix(matrix, target))

        