class Solution:
    # Time = O(N)
    # Space = O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        window_sum = 0
        min_len = math.inf 
        left = 0
        
        # Use a sliding window of variable size
        # i <- right end of the sliding window, left <- left end of the sliding window
        for i in range(N):
            window_sum += nums[i]
            
            while left <= i and window_sum >= target:
                window_sum -= nums[left]
                min_len = min(min_len, i-left+1)
                left += 1
        
        return min_len if min_len != math.inf else 0
                