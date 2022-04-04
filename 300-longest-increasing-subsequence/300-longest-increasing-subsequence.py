class Solution:
    
    # Time = O(N^2)
    # Space = O(N)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        
        dp = [1] * N
        max_len = 1
        
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    max_len = max(max_len, dp[i])
        
        return max_len