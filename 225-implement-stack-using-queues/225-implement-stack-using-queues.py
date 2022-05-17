from collections import *

# Time = O(N) ~ cannot overcome this barrier
# Space = O(1) ~ for each insertion
class MyStack:
    def __init__(self):
        self.queue = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(self.size):
            self.queue.append(self.queue.popleft())
        self.size += 1
        return
            
    def pop(self) -> int:
        # Queue is empty
        if self.size == 0:
            return None
        self.size -= 1
        return self.queue.popleft()

    def top(self) -> int:
        # Queue is empty
        if self.size == 0:
            return None
        return self.queue[0]
        
    def empty(self) -> bool:
        return (self.size == 0)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()