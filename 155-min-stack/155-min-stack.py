from collections import *

# Time = O(1) 
# Space = O(1)
class MinStack:

    def __init__(self):
        self.my_stack = deque()
        self.size = 0
        self.min_stack = deque()

    def push(self, val: int) -> None:
        # If the stack is empty, push the current value into the min_stack
        if self.size == 0:
            self.min_stack.append(val)
        else:
        # Otherwise, append the minimum of the current value and the minimum seen thus far
            self.min_stack.append(min(val, self.min_stack[-1]))
        self.my_stack.append(val)
        self.size += 1
        return
            
    def pop(self) -> None:
        self.min_stack.pop()
        self.my_stack.pop()
        self.size -= 1
        return

    def top(self) -> int:
        return self.my_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()