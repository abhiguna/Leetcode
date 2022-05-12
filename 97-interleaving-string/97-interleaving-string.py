class Solution:
    # Approach: DP
    
    # Time = O(M*N)
    # Space = O(M*N), could be brought down to O(min(M, N))
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M = len(s1)
        N = len(s2)
        
        # Edge case
        if len(s3) != M + N:
            return False
        
        table = [[False for j in range(N+1)] for i in range(M+1)]
        table[0][0] = True
        
        # Base cases
        # Fill first row
        for j in range(1, N+1):
            table[0][j] = table[0][j-1] and s2[j-1] == s3[j-1]
        
        # Fill first col
        for i in range(1, M+1):
            table[i][0] = table[i-1][0] and s1[i-1] == s3[i-1]
        
        # Fill remaining table
        for i in range(1, M+1):
            for j in range(1, N+1):
                table[i][j] = (s1[i-1] == s3[i+j-1] and table[i-1][j]) or (s2[j-1] == s3[i+j-1] and table[i][j-1])
        
        return table[M][N]