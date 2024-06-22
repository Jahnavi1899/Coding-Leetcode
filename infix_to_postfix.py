def infixToPostfix(expression):
    stack = []
    order = {"+":1, "-":1 ,"*":2, "/":2, "^":3}
    res = []
    for ch in expression:
        if ch.isalnum():
            res.append(ch)
        if len(stack) == 0 or order[ch] > order[stack[-1]] or ch == "(":
            stack.append(ch)
        else:
            while len(stack) > 0 and order[ch] <= order[stack[-1]]:
                res.append(stack.pop())
        if len(stack) == 0 or order[ch] <= order[stack[-1]]:
            stack.append(ch)
        
        
        