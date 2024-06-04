def merge(nums1, m, nums2, n):
    # for i in range(m):
    #     print('i :{0}, nums1:{1}'.format(i, nums1[i]))
    
    # for j in range(n):
    #     print('j :{0}, nums2:{1}'.format(j, nums2[j]))

    # for i in range(m):
    #     print('nums1',nums1[i])
    #     print('nums2',nums2[i])
    #     if nums1[i] > nums2[i]:
    #         temp = nums1[i]
    #         nums1[i] = nums2[i]
    #         nums2[i] = temp
    # print(nums1)
    l = 0
    while nums1[l] != 0:
        if nums1[l] > nums2[0]:
            temp = nums1[l]
            nums1[l] = nums2[0]
            nums2[0] = temp
            l += 1
    # print(nums1)
    nums2.sort()
    for j in range(n):
        nums1[j+m] = nums2[j]
    print(nums1)

nums1 = [2,3,4,0,0,0]
m = 3
nums2 = [1,5,6]
n = 3

merge(nums1, m, nums2, n)