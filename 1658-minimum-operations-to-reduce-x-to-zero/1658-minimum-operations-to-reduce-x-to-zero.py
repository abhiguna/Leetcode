class Solution:
    # Time = O(N)
    # Space = O(1)
    def minOperations(self, nums: List[int], x: int) -> int:
        # Rephrase the problem: finding the min modifications that sum up to k is the same as 
        #.   maximizing subarray that sums up to sum(nums) - x
        N = len(nums)
        k = sum(nums) - x
        left = 0
        window_sum = 0
        max_len = -1
        
        for i in range(N):
            window_sum += nums[i]
            
            while left <= i and window_sum > k:
                window_sum -= nums[left]
                left += 1
            
            # Verify window_sum == k before updating max len
            if window_sum == k:
                max_len = max(max_len, i-left+1)
        
        # Return the min modifications made to reach x
        return N - max_len if max_len != -1 else -1