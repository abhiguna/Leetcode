class MedianFinder:
    # Time = O(logN) for the Nth number
    # Space = O(N)
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.size = 0

    def rebalance_heaps(self):
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))
        else:
            heappush(self.max_heap, -heappop(self.min_heap))
        
    def addNum(self, num: int) -> None:
        if self.size == 0 or num <= -self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        
        self.size += 1
        
        if abs(len(self.max_heap) - len(self.min_heap)) > 1:
            self.rebalance_heaps()
        

    def findMedian(self) -> float:
        # The number of elements is odd
        if self.size % 2 == 1:
            if len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
            else:
                return -self.max_heap[0]
                
        # The number of elements is even
        else:
            return (self.min_heap[0] + -self.max_heap[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()