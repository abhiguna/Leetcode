class Solution:
    # Approach: DP
    
    # Time = O(N^2)
    # Space = O(N^2) -> could be brought down to O(N)
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        table = [[0 for j in range(N)] for i in range(N)]
        
        # Base case: substring of len 1 => LPS of 1
        for i in range(N):
            table[i][i] = 1
        
        # Fill in remaining cells
        for i in range(N-2, -1, -1):
            for j in range(i+1, N):
                if s[i] == s[j]:
                    table[i][j] = table[i+1][j-1] + 2
                else:
                    table[i][j] = max(table[i+1][j], table[i][j-1])
        
        return table[0][N-1]