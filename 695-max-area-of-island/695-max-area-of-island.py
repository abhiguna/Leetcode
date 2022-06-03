class Solution:
    # Time = O(M*N)
    # Space = O(max(M, N))
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        max_area = [0]
        
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
        
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            curr_area = 1
            grid[r][c] = 0
            
            while queue:
                (row, col) = queue.popleft()
                
                for (nrow, ncol) in get_neighbors(row, col):
                    if grid[nrow][ncol] == 1:
                        grid[nrow][ncol] = 0
                        curr_area += 1
                        queue.append((nrow, ncol))

            max_area[0] = max(max_area[0], curr_area)
            return
        
        
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    bfs(i, j)
        
        return max_area[0]
        