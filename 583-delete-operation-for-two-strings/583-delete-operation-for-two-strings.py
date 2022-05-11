class Solution:
    # Approach: DP
    
    # Time = O(M*N)
    # Space = O(M*N) -> could be brought down O(min(M, N))
    def minDistance(self, word1: str, word2: str) -> int:
        M = len(word1)
        N = len(word2)
        table = [[0 for j in range(N+1)] for i in range(M+1)]
        
        # Base cases
        # Fill the first row
        for j in range(1, N+1):
            table[0][j] = j
        
        # Fill the first column
        for i in range(1, M+1):
            table[i][0] = i
        
        # Fill remaining cells
        for i in range(1, M+1):
            for j in range(1, N+1):
                if word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1]
                else:
                    table[i][j] = 1 + min(table[i-1][j], table[i][j-1])
        
        return table[M][N]