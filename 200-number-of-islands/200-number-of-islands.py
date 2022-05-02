from collections import deque

class Solution:
    # Time = O(M * N)
    # Space = O(min(M, N))
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])
        
        def get_adj_neighbors(row, col):
            res = []
            if row + 1 < M:
                res.append([row+1, col])
            if row - 1 >= 0:
                res.append([row-1, col])
            if col + 1 < N:
                res.append([row, col+1])
            if col - 1 >= 0:
                res.append([row, col-1])
            
            return res
        
        def bfs(start_row, start_col):
            nonlocal grid 
            
            queue = deque([[start_row, start_col]])
            grid[start_row][start_col] = "0"
            
            while queue:
                curr_row, curr_col = queue.popleft()
                for (row, col) in get_adj_neighbors(curr_row, curr_col):
                    if grid[row][col] == "1":
                        grid[row][col] = "0"
                        queue.append([row, col])
            return
        
        num_islands = 0
        for row in range(M):
            for col in range(N):
                # If curr cell is a land
                if grid[row][col] == "1":
                    bfs(row, col)
                    num_islands += 1
        
        return num_islands