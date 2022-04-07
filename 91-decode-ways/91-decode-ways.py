from collections import *

class Solution:
    
    # Time = O(N)
    # Space = O(N)
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = defaultdict(int)
        dp[N] = 1
        
        for i in range(N-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                # Take one character
                dp[i] = dp[i+1]
            
            # Take two characters if possible
            if (i < N-1) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                dp[i] += dp[i+2]
        
        return dp[0]
                