class MyQueue:
    # Time = O(1) amortized time for each push/pop operation
    # Space = O(N) for maintaining 2 stacks
    def __init__(self):
        self.size = 0
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)
        self.size += 1
        return
        
    def pop(self) -> int:
        if len(self.pop_stack) > 0:
            queue_top = self.pop_stack.pop()
        else:
            while len(self.push_stack) > 0:
                self.pop_stack.append(self.push_stack.pop())
            queue_top = self.pop_stack.pop()
        self.size -= 1
        return queue_top

    def peek(self) -> int:
        if len(self.pop_stack) > 0:
            return self.pop_stack[-1]
        else:
            while len(self.push_stack) > 0:
                self.pop_stack.append(self.push_stack.pop())
            return self.pop_stack[-1]

    def empty(self) -> bool:
        return (self.size == 0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()