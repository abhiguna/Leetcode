class Solution:
    # Time = O(M*N)
    # Space = O(M*N)
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        
        visited = set()
        
        def dfs(row, col):
            # Base case
            if row < 0 or col < 0 or row >= M or col >= N or grid[row][col] == 0:
                return 1
            if (row, col) in visited:
                return 0
            
            # Recursive case
            visited.add((row, col))
            perimeter = dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)
            return perimeter
            
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    return dfs(r, c)
        
        return 0