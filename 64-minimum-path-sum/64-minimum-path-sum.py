class Solution:
    # Approach: DP
    
    # Time = O(M*N)
    # Space = O(M*N)
    def minPathSum(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        table = [[0 for j in range(N)] for i in range(M)]
        table[0][0] = grid[0][0]
        
        # First row
        for col in range(1, N):
            table[0][col] = grid[0][col] + table[0][col-1]
        
        # First col
        for row in range(1, M):
            table[row][0] = grid[row][0] + table[row-1][0]
        
        # Fill remaining cells
        for row in range(1, M):
            for col in range(1, N):
                table[row][col] = grid[row][col] + min(table[row-1][col], table[row][col-1])
        
        return table[M-1][N-1]