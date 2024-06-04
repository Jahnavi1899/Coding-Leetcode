# def pattern1(n,m):
#     for _ in range(n):
#         for _ in range(m):
#             print("*", end=" ")
#         print("\n")

# pattern1(4,4)

def check(nums):
    count = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            count += 1
    if nums[len(nums)-1] > nums[0]:
        count += 1
        
    if count <= 1:
        return True
    else:
        return False
    
print(check([3,4,5,1,2]))
