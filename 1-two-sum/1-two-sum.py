from collections import *

class Solution:
    # Time = O(N)
    # Space = O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_seen = defaultdict(int)
        
        N = len(nums)
        for i in range(N):
            if target - nums[i] in prev_seen:
                return [prev_seen[target-nums[i]], i]
            
            prev_seen[nums[i]] = i
        
        return [-1, -1]