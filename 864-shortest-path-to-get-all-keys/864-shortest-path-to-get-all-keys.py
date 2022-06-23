class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        
        def get_non_walled_neighbors(row, col):
            neighbors = []
            if (row + 1 < m) and (grid[row+1][col] != '#'):
                neighbors.append((row+1, col))
            if (col + 1 < n) and (grid[row][col+1] != '#'):
                neighbors.append((row, col+1))
            if (row - 1 >= 0) and (grid[row-1][col] != '#'):
                neighbors.append((row-1, col))
            if (col - 1 >= 0) and (grid[row][col-1] != '#'):
                neighbors.append((row, col-1))
            return neighbors
            
        def bfs(row, col):
            visited = set()
            queue = deque() # (row, col, key_state, path_len)
            queue.append((row, col, -1, ""))
            visited.add((row, col, ""))
            
            while queue:
                (r, c, path_len, key_state) = queue.popleft()
                
                for (nr, nc) in get_non_walled_neighbors(r, c):
                    # Update key_state if new key found
                    if grid[nr][nc].islower():
                        if grid[nr][nc] not in key_state:
                            nkey_state = str(key_state) + grid[nr][nc]
                    else:
                        nkey_state = str(key_state)
                        
                    # Can only go through a lock if a corresponding key exists
                    if grid[nr][nc].isupper() and \
                        grid[nr][nc].lower() not in nkey_state:
                        continue
                        
                    if (nr, nc, nkey_state) not in visited:
                        visited.add((nr, nc, nkey_state))
                        queue.append((nr, nc, path_len+1, nkey_state))
                        if len(key_state) == num_keys:
                            return path_len + 1
                            
            return -1
        
        start_row, start_col = -1, -1
        num_keys = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "@":
                    start_row = r
                    start_col = c
                if grid[r][c].islower():
                    num_keys += 1
                    
        return bfs(start_row, start_col)
                    