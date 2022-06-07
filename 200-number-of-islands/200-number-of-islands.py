class Solution:
    # Time = O(M*N)
    # Space = O(max(M, N))
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        
        def get_neighbors(row, col):
            neighbors = []
            if row + 1 < M:
                neighbors.append((row+1, col))
            if col + 1 < N:
                neighbors.append((row, col+1))
            if row - 1 >= 0:
                neighbors.append((row-1, col))
            if col - 1 >= 0:
                neighbors.append((row, col-1))
            return neighbors
            
            
        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            grid[row][col] = "0"
            
            while queue:
                (curr_row, curr_col) = queue.popleft()
                
                for (nrow, ncol) in get_neighbors(curr_row, curr_col):
                    if grid[nrow][ncol] == "1":
                        grid[nrow][ncol] = "0"
                        queue.append((nrow, ncol))
            
            return
        
        
        # Outer loop
        islands = 0
        for r in range(M):
            for c in range(N):
                # If not visited -> BFS
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        
        return islands