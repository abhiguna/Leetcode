class Solution:
    # Time = O(M*N)
    # Space = O(min(M, N))
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        
        def get_adj_neighbors(row, col):
            res = []
            if row + 1 < len(grid):
                res.append([row+1, col])
            if row - 1 >= 0:
                res.append([row-1, col])
            if col + 1 < len(grid[0]):
                res.append([row, col+1])
            if col - 1 >= 0:
                res.append([row, col-1])
            
            return res
        
        def bfs(src_row, src_col):
            nonlocal max_area
            
            queue = deque([[src_row, src_col]])
            curr_area = 1
            grid[src_row][src_col] = 0
            
            while queue:
                (curr_row, curr_col) = queue.popleft()
                
                for (nrow, ncol) in get_adj_neighbors(curr_row, curr_col):
                    if grid[nrow][ncol] == 1:
                        curr_area += 1
                        grid[nrow][ncol] = 0
                        queue.append([nrow, ncol])
            
            max_area = max(max_area, curr_area)
            return
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    bfs(row, col)
        
        return max_area
        