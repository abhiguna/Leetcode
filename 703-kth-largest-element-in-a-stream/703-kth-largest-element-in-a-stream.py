from heapq import *

# Time = O(logk), for the nth number
# Space = O(k)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.size = 0
        self.capacity = k
        
        for num in nums:
            heappush(self.min_heap, num)
            self.size += 1
            if self.size > self.capacity:
                heappop(self.min_heap)
                self.size -= 1
            

    def add(self, val: int) -> int:
        heappush(self.min_heap, val)
        self.size += 1
        if self.size > self.capacity:
            heappop(self.min_heap)
            self.size -= 1
        return self.min_heap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)