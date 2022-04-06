class Solution:
    
    # Time = O(target*N), N = len(nums)
    # Space = O(N)
    def combinationSum4(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = [0] * (target + 1)
        # Base
        dp[0] = 1
        
        for target in range(1, target+1):
            for num in nums:
                if target >= num:
                    dp[target] += dp[target-num]
        
        return dp[target]
                    