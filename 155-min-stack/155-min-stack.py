# Time = O(1)
# Space = O(1)
class MinStack:
    def __init__(self):
        self.push_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.push_stack.append(val)
        
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))
        return
        

    def pop(self) -> None:
        self.min_stack.pop()
        self.push_stack.pop()
        return

    def top(self) -> int:
        return self.push_stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()