class Solution:
    
    # Time = O(N)
    # Space = O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        
        curr_sum = 0
        max_sum = -math.inf
        
        for i in range(N):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum