# Time = O(logN) for addNum and O(1) for findMedian
# Space = O(1) for each element from the data stream

class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def rebalance_heaps(self):
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
        else:
            heappush(self.min_heap, -heappop(self.max_heap))

    
    def addNum(self, num: int) -> None:
        # Edge case: max heap is empty
        if len(self.max_heap) == 0:
            heappush(self.max_heap, -num)
            return
        
        if num <= abs(self.max_heap[0]):
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        
        if abs(len(self.max_heap) - len(self.min_heap)) > 1:
            self.rebalance_heaps()
        return
        

    def findMedian(self) -> float:
        # Even number of elements inserted
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -self.max_heap[0]) / 2.0
        
        # Odd number of elements inserted
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()