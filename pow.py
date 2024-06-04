def myPow(x, n):
    res = helper(x, abs(n))
    if n >= 0:
        return res
    else:
        return 1/res


def helper(x, n):
    if n == 0:
        return 1
    if x == 0:
        return 0

    res = helper(x, n//2)
    res = res * res
    if n % 2 == 0:
        return res
    else:
        return x * res
    
x = 2.00000
n = 10
print(myPow(x,n))