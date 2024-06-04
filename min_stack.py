class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.len = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.len == 0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStakc[-1]))
        self.min += 1

    def pop(self) -> None:
        self.stack.pop() 
        self.minStack.pop()
        self.len -= 1
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
# param_3 = obj.top()
# param_4 = obj.getMin()

# [[],[-2],[0],[-3],[],[],[],[]]