class Solution:
    # Time = O(M*N)
    # Space = O(max(M, N))
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        # Populate queue with rotten oranges
        queue = deque()
        
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
        
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
            
        # Multi-source bfs
        min_time = 0
        while queue:
            (r, c, time) = queue.popleft()
            # Update min time
            min_time = max(min_time, time)
            
            for (nr, nc) in get_neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, time + 1))
                    
        # Check to make sure no fresh oranges still exist
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    return -1
        
        return min_time
        