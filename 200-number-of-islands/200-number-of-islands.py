class Solution:
    # Time = O(M*N)
    # Space = O(max(M, N))
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        
        def get_neighbors(curr_row, curr_col):
            neighbors = []
            if curr_row + 1 < M:
                neighbors.append((curr_row+1, curr_col))
            if curr_row - 1 >= 0:
                neighbors.append((curr_row-1, curr_col))
            if curr_col - 1 >= 0:
                neighbors.append((curr_row, curr_col-1))
            if curr_col + 1 < N:
                neighbors.append((curr_row, curr_col+1))
            
            return neighbors
            
            
        
        def bfs(src_row, src_col):
            queue = deque()
            queue.append((src_row, src_col))
            grid[src_row][src_col] = "0"
            
            while queue:
                (curr_row, curr_col) = queue.popleft()
                
                for (nei_row, nei_col) in get_neighbors(curr_row, curr_col):
                    if grid[nei_row][nei_col] == "1":
                        grid[nei_row][nei_col] = "0"
                        queue.append((nei_row, nei_col))
                
            return
            
            
        
        # Find the number of connected components in the graph
        components = 0
        for row in range(M):
            for col in range(N):
                if grid[row][col] == "1":
                    components += 1
                    bfs(row, col)
        
        return components
            
            