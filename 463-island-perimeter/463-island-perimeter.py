class Solution:
    # Time = O(M*N)
    # Space = O(max(M, N))
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        perimeter = [0]
        
        def get_num_sides(row, col):
            sides = 0
            # Top side
            if row == 0 or grid[row-1][col] == 0:
                sides += 1
            # Bottom side
            if row == M-1 or grid[row+1][col] == 0:
                sides += 1
            # Right side
            if col == N-1 or grid[row][col+1] == 0:
                sides += 1
            # Left side
            if col == 0 or grid[row][col-1] == 0:
                sides += 1
            return sides
        
        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]
        
        def bfs(row, col):
            queue = deque([(row, col)])
            visited = set([(row, col)])
        
            while queue:
                curr_row, curr_col = queue.popleft()
                perimeter[0] += get_num_sides(curr_row, curr_col)
                
                for i in range(4):
                    nrow = curr_row + dy[i]
                    ncol = curr_col + dx[i]
                    if nrow < 0 or ncol < 0 or nrow >= M or ncol >= N or \
                        ((nrow, ncol) in visited) or grid[nrow][ncol] == 0:
                        continue
                    visited.add((nrow, ncol))
                    queue.append((nrow, ncol))
            
            return perimeter
        
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    return bfs(r, c)[0]
        
        return 0