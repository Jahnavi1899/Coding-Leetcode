def evalRPN(tokens):
    valid_operators = ["+", "-", "*", "/"]
    stack = []
    for t in tokens:
        if t not in valid_operators:
            stack.append(int(t))
        else:
            res = 0
            if t == "+":
                res = stack[-2] + stack[-1] 
            elif t == "-":
                res = stack[-2] - stack[-1] 
            elif t == "*":
                res = stack[-2] * stack[-1] 
            elif t == "/":
                res = int(stack[-2] / stack[-1]) 
            print(res)
            stack.pop()
            stack.pop()
            stack.append(res)
    return stack[-1]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))