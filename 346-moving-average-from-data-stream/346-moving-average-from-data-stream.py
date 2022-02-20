
# Pattern: circular-queue
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.head = 0
        self.window_sum = 0
        self.queue = [0] * self.size
        self.count = 0
        
    def next(self, val: int) -> float:
        self.count += 1
        self.tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[self.tail] + val
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.count, self.size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)