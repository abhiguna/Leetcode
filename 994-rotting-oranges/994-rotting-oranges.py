class Solution:
    # Time = O(M*N)
    # Space = O(max(M, N))
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        min_time = 0
        fresh_oranges = 0
        
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
            
        queue = deque()
        
        for r in range(M):
            for c in range(N):
                # Rotten orange
                if grid[r][c] == 2: 
                    queue.append((r, c))
                # Fresh orange
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        while queue and fresh_oranges > 0:
            num_rotten = len(queue)
            
            for i in range(num_rotten):
                (row, col) = queue.popleft()
                
                for (nrow, ncol) in get_neighbors(row, col):
                    if grid[nrow][ncol] == 1:
                        grid[nrow][ncol] = 2
                        fresh_oranges -= 1
                        queue.append((nrow, ncol))
            
            min_time += 1
        
        if fresh_oranges > 0:
            return -1
        
        return min_time