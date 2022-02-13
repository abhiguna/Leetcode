# Date: 2/13/22
# 15m 5

class MinStack:
    # Time = O(1)
    # Space = O(1)
    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        
    # Time = O(1)
    # Space = O(1)
    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.min_stack or self.min_stack[-1] > val:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    # Time = O(1)
    # Space = O(1)
    def pop(self) -> None:
        self.min_stack.pop()
        self.main_stack.pop()

    # Time = O(1)
    # Space = O(1)
    def top(self) -> int:
        return self.main_stack[-1]

    # Time = O(1)
    # Space = O(1)
    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()