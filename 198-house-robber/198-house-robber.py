class Solution:
    # Time = O(N)
    # Space = O(1)
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        
        # Base case
        first = 0
        second = nums[0]
        
        for i in range(1, N):
            third = max(nums[i] + first, second)
            first = second
            second = third
        
        return second