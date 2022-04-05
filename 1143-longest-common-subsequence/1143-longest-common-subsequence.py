class Solution:
    
    # Time = O(N*M)
    # Space = O(N*M)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N = len(text1)
        M = len(text2)
        dp = [[0 for j in range(N + 1)] for i in range(M + 1)]
        
        # Fill the remaining dp entries starting with the last character
        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                
                # Characters match
                if text1[j] == text2[i]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    
                # Characters do not match
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]