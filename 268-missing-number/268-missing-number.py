class Solution:
    
    # Time = O(N)
    # Space = O(1)
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = sum(range(len(nums) + 1))
        actual_sum = sum(nums)
        return total_sum - actual_sum
        