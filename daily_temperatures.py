def dailyTemperatures(temperatures):
    #brute force 
    answer = [0] * len(temperatures)
    stack = [] # holding index and value
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            value, idx = stack.pop()
            answer[idx] = i - idx
        stack.append([t, i])
    return answer

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))