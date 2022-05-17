# Time = O(1) ~ amortized time
# Space = O(1) ~ amortized space
class MyQueue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def push(self, x: int) -> None:
        self.enqueue_stack.append(x)
        return

    def pop(self) -> int:
        # If the dequeue_stack has elements in it => pop from it
        if len(self.dequeue_stack) > 0:
            return self.dequeue_stack.pop()
        # Otherwise, transfer all the elements from enqueue_stack to dequeue_stack and then pop
        for i in range(len(self.enqueue_stack)):
            self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def peek(self) -> int:
        # If the dequeue stack still has elements in it, return the top of it
        if len(self.dequeue_stack) > 0:
            return self.dequeue_stack[-1]
        # Otherwise, return the top of the dequeue stack
        return self.enqueue_stack[0]

    def empty(self) -> bool:
        return (len(self.enqueue_stack) == 0) and (len(self.dequeue_stack) == 0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()