from collections import *

class Solution:
    # Time = O(N)
    # Space = O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        res = [-1, -1]
        nums_seen = defaultdict(int)
        
        for i in range(N):
            if target - nums[i] in nums_seen:
                res[0], res[1] = nums_seen[target-nums[i]], i
                break
            
            nums_seen[nums[i]] = i
        
        return res