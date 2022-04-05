class Solution:
    
    # Time = O(N * M)
    # Space = O(N)
    def combinationSum4(self, nums: List[int], target: int) -> int:
        N = target
        M = len(nums)
        
        dp = [0 for i in range(N+1)]
        
        for i in range(1, N+1):
            combinations = 0
            
            for num in nums:
                if i > num:
                    combinations += dp[i - num]
                elif i == num:
                    combinations += 1
            
            dp[i] = combinations
        
        return dp[N]