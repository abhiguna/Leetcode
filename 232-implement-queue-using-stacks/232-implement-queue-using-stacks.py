# Time = O(1) ~ amortized time
# Space = O(1) ~ amortized space
class MyQueue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
        self.size = 0

    def push(self, x: int) -> None:
        self.enqueue_stack.append(x)
        self.size += 1
        return

    def pop(self) -> int:
        # Edge case: check if queue is empty
        if self.size == 0:
            return None
        
        self.size -= 1
        # If the dequeue_stack has elements in it => pop from it
        if len(self.dequeue_stack) > 0:
            return self.dequeue_stack.pop()
        # Otherwise, transfer all the elements from enqueue_stack to dequeue_stack and then pop
        while len(self.enqueue_stack) != 0:
            self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def peek(self) -> int:
        if self.size == 0:
            return None
        # If the dequeue stack still has elements in it, return the top of it
        if len(self.dequeue_stack) > 0:
            return self.dequeue_stack[-1]
        # Otherwise, transfer all the elements to the dequeue_stack and return the top of it
        while len(self.enqueue_stack) != 0:
            self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack[-1]

    def empty(self) -> bool:
        return (self.size == 0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()