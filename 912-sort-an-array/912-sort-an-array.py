from heapq import *

class Solution:
    # Approach 3: Heapsort -> NOT stable, in-place
    
    # Time = O(NlogN)
    # Space = O(1)
    def sortArray(self, nums: List[int]) -> List[int]:
        heapify(nums)
        res = []
        while len(nums) != 0:
            res.append(heappop(nums))
        return res