import math
def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (l+r)//2
        total = 0
        for p in piles:
            total += math.ceil(p/k)
        if total <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1
    return res

piles = [3,6,7,11]
h = 8

print(minEatingSpeed(piles, h))