import math

class Solution:
    
    # Time = O(N * M)
    # Space = O(N)
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Base
        if amount == 0:
            return 0
        
        M = len(coins)
        N = amount
        
        dp = [math.inf] * (N + 1)
        dp[0] = 0
        
        for i in range(1, N + 1):
            for j in range(M):
                # Amount is smaller than coins or if diff not coverable
                if i < coins[j] or dp[i - coins[j]] == math.inf:
                    continue
                
                num_coins_req = 1 + dp[i - coins[j]]
                dp[i] = min(dp[i], num_coins_req)
        
        if dp[N] == math.inf:
            return -1
        
        return dp[N]