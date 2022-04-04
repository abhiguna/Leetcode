class Solution:
    
    # Time = O(N)
    # Space = O(1)
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        missing_num = N
        
        for idx, num in enumerate(nums):
            missing_num ^= idx ^ num
        
        return missing_num
        