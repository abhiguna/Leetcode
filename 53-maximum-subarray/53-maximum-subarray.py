import math

class Solution:
    
    def max_sum_sub_rec(self, nums, start, end):
        # Base case:
        if end < start:
            return -math.inf

        mid = start + (end - start) // 2
        curr_sum = 0
        max_left_sum = 0
        max_right_sum = 0
        
        # Iterate from the middle to the beginning
        for i in range(mid - 1, start - 1, -1):
            curr_sum += nums[i]
            max_left_sum = max(max_left_sum, curr_sum)
        
        # Reset curr and iterate from the middle to the end
        curr_sum = 0
        for i in range(mid + 1, end + 1):
            curr_sum += nums[i]
            max_right_sum = max(max_right_sum, curr_sum)
        
        # The best combined sum uses the middle element and 
        # the best possible sum from each half
        best_combined_sum = max_left_sum + nums[mid] + max_right_sum
        
        # Find the best subarray possible from both halves.
        left_half = self.max_sum_sub_rec(nums, start, mid - 1)
        right_half = self.max_sum_sub_rec(nums, mid + 1, end)
        
        # The largest of the 3 is the answer for any given input array
        return max(best_combined_sum, left_half, right_half)
        
    
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        return self.max_sum_sub_rec(nums, 0, N - 1)