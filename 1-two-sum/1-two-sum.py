from collections import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        nums_seen = defaultdict(int)
        
        res = [-1, -1]
        
        for i in range(N):
            if (target - nums[i]) in nums_seen:
                res = [nums_seen[target-nums[i]], i]
                break
            
            nums_seen[nums[i]] = i
        
        return res