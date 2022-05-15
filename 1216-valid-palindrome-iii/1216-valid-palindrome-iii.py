class Solution:
    # Approach: DP
    
    # Time = O(N^2)
    # Space = O(N^2) -> could be brought down to O(N)
    def isValidPalindrome(self, s: str, k: int) -> bool:
        N = len(s)
        table = [[0 for j in range(N)] for i in range(N)]
        
        def find_longest_palindromic_subsequence(s):
            # Base case: 
            for i in range(N):
                table[i][i] = 1
            
            # Fill in the remaining cells
            for i in range(N-1, -1, -1):
                for j in range(i+1, N):
                    # Case 1: first and last characters match up
                    if s[i] == s[j]:
                        table[i][j] = table[i+1][j-1] + 2
                    # Case 2: first and last characters DO NOT match
                    else:
                        table[i][j] = max(table[i+1][j], table[i][j-1])
            
            return table[0][N-1]
        
        LPS = find_longest_palindromic_subsequence(s)
        return N - LPS <= k
