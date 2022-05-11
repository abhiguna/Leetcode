class Solution:
    # Approach: DP
    
    # Time = O(N*M)
    # Space = O(N*M), could be brought down to O(min(N, M))
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # table[i][j] = len of the LCS if upto i chars in text1 and j chars in text2 are 
        #    examined.
        M = len(text1)
        N = len(text2)
        table = [[0 for j in range(N+1)] for i in range(M+1)]
        
        for i in range(1, M+1):
            for j in range(1, N+1):
                if text1[i-1] == text2[j-1]: 
                    matches = 1
                else: 
                    matches = 0
                table[i][j] = max(table[i-1][j], table[i][j-1], table[i-1][j-1] + matches)
        
        return table[M][N]