class Solution:
    # Time = O(N)
    # Space = O(1)
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Set the initial metrics for a sliding window of size k 
        window_sum = sum(nums[:k])
        max_sum = window_sum
        N = len(nums)
        
        for i in range(k, N):
            # Add the curr value to the sum and decrement the value at the start of the window
            window_sum += (nums[i] - nums[i-k])
            max_sum = max(max_sum, window_sum)
        
        return float(max_sum) / k