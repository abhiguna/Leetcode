class Solution:
    # Approach: DP
    
    # Time = O(M*N)
    # Space = O(M*N) -> could be broght down to min(M, N)
    def minDistance(self, word1: str, word2: str) -> int:
        M = len(word1)
        N = len(word2)
        
        # Edge cases
        if N == 0:
            return M
        if M == 0:
            return N
        
        table = [[0 for j in range(N+1)] for i in range(M+1)]
        table[0][0] = 0 # Empty string
        
        # Base cases
        # Fill first row: comparing empty string with each prefix of word2
        for j in range(1, N+1):
            table[0][j] = j
        
        # Fill first col: comparing empty string with each prefix of word1
        for i in range(1, M+1):
            table[i][0] = i
        
        # Fill in remaining cells
        # table[i][j] = min edit distance if the first i characters from word1 and the first j characters from word2 are examined
        for i in range(1, M+1):
            for j in range(1, N+1):
                # Match
                if word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1]
                # Mismatch
                else:
                    table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])
        
        return table[M][N]