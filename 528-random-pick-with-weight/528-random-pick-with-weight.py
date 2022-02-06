import bisect
import random

class Solution:
    # Time = O(n)
    # Space = O(n)
    def __init__(self, w: List[int]):
        N = len(w)
        self.sum_list = [0]*N
        self.sum_list[0] = w[0]
        for i in range(1, N):
            self.sum_list[i] = self.sum_list[i-1] + w[i]
        
    # Time = O(logn)
    # Space = O(1) 
    def pickIndex(self) -> int:
        rand_sum = random.randint(1, self.sum_list[-1])
        return bisect.bisect_left(self.sum_list, rand_sum)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()