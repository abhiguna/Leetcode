class Solution:
    # Time = O(M*N)
    # Space = O(M+N)
    def getFood(self, grid: List[List[str]]) -> int:
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
            queue.append((row, col, 0))
            grid[row][col] = "V"
            
            while queue:
                (curr_row, curr_col, level) = queue.popleft()

                for (nrow, ncol) in get_neighbors(curr_row, curr_col):
                    # Find if the next node is the food node
                    if grid[nrow][ncol] == "#":
                        return level+1
                    # Traverse unvisited and non-obstacle neighbors
                    if grid[nrow][ncol] != 'V' and grid[nrow][ncol] != 'X':
                        grid[nrow][ncol] = 'V'
                        queue.append((nrow, ncol, level+1))
            
            return -1
        
        
        for r in range(M):
            for c in range(N):
                # Found start location
                if grid[r][c] == "*":
                    return bfs(r, c)
        
        # Never get here
        return -1