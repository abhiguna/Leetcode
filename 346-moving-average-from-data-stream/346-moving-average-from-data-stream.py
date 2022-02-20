class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MovingAverage:

    def __init__(self, size: int):
        self.cap = size
        self.count = 0
        self.stream = Node(0)
        self.tail = self.head = self.stream
        self.sum = 0
        
    def next(self, val: int) -> float:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.count += 1
        if self.count == 1:
            self.head = self.tail
        self.sum += val
        if self.count > self.cap:
            self.sum -= self.head.val
            self.head = self.head.next
            if self.count == 1:
                self.tail = self.head = self.stream
            self.count -= 1
        return self.sum / self.count


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)