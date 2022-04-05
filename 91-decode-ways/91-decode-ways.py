class Solution:
    # Time = O(N)
    # Space = O(N)
    def numDecodings(self, s: str) -> int:
        # Memoized results
        N = len(s)
        dp = {N : 1}
        
        for i in range(N-1, -1 , -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                # Only one character taken
                dp[i] = dp[i+1]
            
            # Check if possible to take two characters
            if i+1 < N and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
        
        return dp[0]
            