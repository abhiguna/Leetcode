class Solution:
    # Time = O(N)
    # Space = O(1)
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        # Edge case
        if N == 1:
            return nums[0]
        
        first = nums[0]
        second = max(nums[0], nums[1])
        
        for i in range(2, N):
            third = max(second, nums[i] + first)
            first = second 
            second = third
        
        return second