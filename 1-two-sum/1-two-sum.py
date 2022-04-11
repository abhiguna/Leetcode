class Solution:
    
    # Time = O(N)
    # Space = O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        prev_seen = defaultdict(int)
        
        res = [-1, -1]
        
        for idx, num in enumerate(nums):
            if (target - num) in prev_seen:
                res = [prev_seen[target-num], idx]
                break
            else:
                prev_seen[num] = idx
        
        return res