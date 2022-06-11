class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        
        # table[r][c] stores nearest dist to a 0
        table = [[math.inf for j in range(N)] for i in range(M)]
        
        # First pass
        for r in range(M):
            for c in range(N):
                if mat[r][c] == 0:
                    table[r][c] = 0
                else:
                    if r > 0:
                        table[r][c] = min(table[r][c], 1 + table[r-1][c])
                    if c > 0:
                        table[r][c] = min(table[r][c], 1 + table[r][c-1])
        
        # Second pass
        for r in range(M-1, -1, -1):
            for c in range(N-1, -1, -1):
                if mat[r][c] == 0:
                    table[r][c] = 0
                else:
                    if r < M-1:
                        table[r][c] = min(table[r][c], 1 + table[r+1][c])
                    if c < N-1:
                        table[r][c] = min(table[r][c], 1 + table[r][c+1])
        
        return table