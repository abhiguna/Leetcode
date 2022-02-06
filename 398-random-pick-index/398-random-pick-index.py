from collections import defaultdict
import random

class Solution:
    # Time = O(n)
    # Space = O(n)
    def __init__(self, nums: List[int]):
        self.idx_dict = defaultdict(list)
        N = len(nums)
        for i in range(N):
            self.idx_dict[nums[i]].append(i)
    
    # Time = O(1)
    # Space = O(1)
    def pick(self, target: int) -> int:
        N = len(self.idx_dict[target])
        return self.idx_dict[target][random.randint(0, N-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)