class Solution:
    # Time = O(N)
    # Space = O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        N = len(nums)
        curr_sum = nums[0]
        max_sum = max(nums)
        
        for i in range(1, N):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)
            
        return max_sum