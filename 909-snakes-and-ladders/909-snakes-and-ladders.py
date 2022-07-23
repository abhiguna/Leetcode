class Solution:
    # Time = O(n^2), n: dimension of board
    # Space = O(n^2)
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        goal = n*n
        
        def get_row_col(pos):
            row = (goal - pos) // n
            c = (pos-1) % (2*n)
            if c < n:
                col = c
            else:
                col = 2*n - 1 - c
            return (row, col)
        
        def min_moves(start):
            # Stores the min distance to a cell
            visited = {}
            
            # BFS
            queue = deque()
            queue.append(start)
            visited[start] = 0
            
            while queue:
                curr_pos = queue.popleft()
                
                for i in range(1, 7):
                    next_pos = i + curr_pos
                    
                    # Out of bounds
                    if next_pos > goal:
                        continue
                    
                    (r, c) = get_row_col(next_pos)
                    
                    # Snake / Ladder
                    if board[r][c] != -1:
                        next_pos = board[r][c]
                    
                    # Update queue
                    if next_pos not in visited:
                        visited[next_pos] = 1 + visited[curr_pos]
                        queue.append(next_pos)
                        if next_pos == goal:
                            return visited[next_pos]
        
            # Not possible to reach goal square
            return -1
        
        return min_moves(1)
        