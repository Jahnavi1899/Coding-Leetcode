class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        operators = ("+", "-", "*", "/")

        for t in tokens:
            if t in operators:
                second = int(stack.pop())
                first = int(stack.pop())
                res = 0
                if t == "+":
                    res = first + second
                elif t == "-":
                    res = first - second
                elif t == "*":
                    res = first * second
                elif t == "/":
                    res = first // second
                stack.append(res) 
            else:
                stack.append(t)
        return stack.pop()
    
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
obj = Solution()
print(obj.evalRPN(tokens))


        