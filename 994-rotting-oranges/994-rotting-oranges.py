class Solution:
    # Time = O(M*N)
    # Space = O(M+N)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        total_minutes = 0
        queue = deque()
        
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
        
        def get_neighbors(i, j):
            neighbors = []
            if i + 1 < M:
                neighbors.append((i+1, j))
            if j + 1 < N:
                neighbors.append((i, j+1))
            if i - 1 >= 0:
                neighbors.append((i-1, j))
            if j - 1 >= 0:
                neighbors.append((i, j-1))
            return neighbors
            

        # Start a BFS
        while queue:
            (row, col, mins) = queue.popleft()
            total_minutes = max(total_minutes, mins)
            
            for (nrow, ncol) in get_neighbors(row, col):
                if grid[nrow][ncol] == 1:
                    grid[nrow][ncol] = 2
                    queue.append((nrow, ncol, mins+1))
        
        # Edge case: if impossible to make everything rotten
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    return -1
        
        return total_minutes
                    
        