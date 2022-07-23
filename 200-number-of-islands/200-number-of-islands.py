class Solution:
    # Time = O(m*n)
    # Space = O(m+n)
    def numIslands(self, grid: List[List[str]]) -> int:
        # Dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        def get_neighbors(row, col):
            neighbors = []
            if row-1>=0 and grid[row-1][col] == "1":
                neighbors.append((row-1, col))
            if col-1>=0 and grid[row][col-1] == "1":
                neighbors.append((row, col-1))
            if row+1<m and grid[row+1][col] == "1":
                neighbors.append((row+1, col))
            if col+1<n and grid[row][col+1] == "1":
                neighbors.append((row, col+1))
            
            return neighbors
                
        
        # BFS -> connect all islands
        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            grid[row][col] = "0"
            
            while queue:
                (curr_row, curr_col) = queue.popleft()
                
                for (nrow, ncol) in get_neighbors(curr_row, curr_col):
                    grid[nrow][ncol] = "0"
                    queue.append((nrow, ncol))
        
        # Outer loop -> traverses all unvisited islands
        num_islands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    num_islands += 1
                    bfs(r, c)
        
        return num_islands