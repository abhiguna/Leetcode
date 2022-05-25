class MovingAverage:
    # Time = O(1)
    # Space = O(k), k: size
    def __init__(self, size: int):
        self.queue = deque()
        self.capacity = size
        self.total = 0

    def next(self, val: int) -> float:
        # Add the current val to the end of the queue
        self.queue.append(val)
        self.total += val
        if len(self.queue) > self.capacity:
            self.total -= self.queue.popleft()
        return self.total / len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)