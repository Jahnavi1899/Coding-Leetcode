def combinationSum2(candidates, target):
        candidates.sort()
        result = []
        getCombinations(0, candidates, target, [], result)
        return result

def getCombinations(index, candidates, target, cur, result):
    if target == 0:
        result.append(cur.copy())
        return
    
    # pick the element
    for i in range(index, len(candidates)):
        if i > index and candidates[i] == candidates[i-1]:
            continue
        if candidates[i] > target:
            break

        cur.append(candidates[i])
        getCombinations(i+1, candidates, target - candidates[i], cur, result)
        cur.pop()
        

candidates = [10, 1, 2,7,6,1,5] 
target = 8

print(combinationSum2(candidates, target))


