class Solution:
    # Approach: DP
    
    # Time = O(M*N)
    # Space = O(M)
    def minPathSum(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        table = [0 for j in range(N)]
        table[0] = grid[0][0]
        
        # First row
        for col in range(1, N):
            table[col] = grid[0][col] + table[col-1]
        
        # Fill remaining cells
        for row in range(1, M):
            prev = table[:]
            table[0] = grid[row][0] + prev[0]
            
            for col in range(1, N):
                table[col] = grid[row][col] + min(prev[col], table[col-1])
        
        return table[N-1]