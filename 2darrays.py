def findMatrix(nums):
    res = []

    for i in nums:
        flag = False
        if len(res) == 0:
            res.append([i])
        else:
            for j in res:
                if i not in j:
                    flag = True
                    j.append(i)
                    break
            if flag == False:
                res.append([i])
        print(res)
    return res

findMatrix([1,3,4,1,2,3,1])