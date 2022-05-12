class Solution:
    # Approach: DP
    
    # Time = O(M*N)
    # Space = O(M*N)
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        M = len(str1)
        N = len(str2)
        table = [[0 for j in range(N+1)] for i in range(M+1)]
        
        def build_lcs_table():
            for i in range(1, M+1):
                for j in range(1, N+1):
                    # Match
                    if str1[i-1] == str2[j-1]:
                        table[i][j] = 1 + table[i-1][j-1]
                    # Mismatch
                    else:
                        table[i][j] = max(table[i-1][j], table[i][j-1], table[i-1][j-1])
        
        def get_supersequence():
            res = []
            row, col = M, N
            
            while row != 0 and col != 0:
                if table[row][col] == table[row-1][col]:
                    res.append(str1[row-1])
                    row -= 1
                elif table[row][col] == table[row][col-1]:
                    res.append(str2[col-1])
                    col -= 1
                else:
                    res.append(str1[row-1])
                    row -= 1
                    col -= 1
            
            while row != 0:
                res.append(str1[row-1])
                row -= 1
            
            while col != 0:
                res.append(str2[col-1])
                col -= 1
            
            res.reverse()
            return "".join(res)
        
        # Find LCS
        build_lcs_table()
        return get_supersequence()
        