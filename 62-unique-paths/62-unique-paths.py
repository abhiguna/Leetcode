class Solution:
    # Time = O(N*M)
    # Space = O(N*M)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        
        # Fill in the dp entries
        for i in range(1, n+1):
            for j in range(1, m+1):
                if i == 1 and j == 1:
                    dp[i][j] = 1
                    continue
            
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[n][m]
                
                