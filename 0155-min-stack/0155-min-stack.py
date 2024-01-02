class MinStack:

    def __init__(self):
        self.stack=[]
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        popped = self.stack[len(self.stack)-1]
        self.stack.pop(len(self.stack)-1)
        if popped == self.min : 
            self.min = float('inf')
            for x in self.stack:
                if x < self.min:
                    self.min = x



    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()