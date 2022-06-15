class Solution:
    
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Objective: start state -> goal state
    
        # Store the start state
        ((i, j, k), (l, m, n)) = board
        start = ((i, j, k), (l, m, n))
        goal = ((1, 2, 3), (4, 5, 0))
        
        # Edge case: start state == goal state
        if start == goal:
            return 0
        
        
        f_visited = {}
        b_visited = {}
        # visited[s] = i implies it takes i moves to get to state s from start state
        
        def get_neighbors(state):
            ((a, b, c), (d, e, f)) = state
            neighbors = set()
            
            # The empty cell could be in any of the 6 positions
            if a == 0:
                # Could switch a with b or d
                neighbors.add(((b, a, c), (d, e, f)))
                neighbors.add(((d, b, c), (a, e, f)))
            elif b == 0:
                # Could switch b with a, c, or e
                neighbors.add(((b, a, c), (d, e, f)))
                neighbors.add(((a, c, b), (d, e, f)))
                neighbors.add(((a, e, c), (d, b, f)))
            elif c == 0:
                # Could switch c with b or f
                neighbors.add(((a, c, b), (d, e, f)))
                neighbors.add(((a, b, f), (d, e, c)))
                
            elif d == 0:
                # Could switch d with a or e
                neighbors.add(((d, b, c), (a, e, f)))
                neighbors.add(((a, b, c), (e, d, f)))
            elif e == 0:
                # Could switch e with b, d, or f
                neighbors.add(((a, e, c), (d, b, f)))
                neighbors.add(((a, b, c), (e, d, f)))
                neighbors.add(((a, b, c), (d, f, e)))
            else:
                # Could switch f with c or e
                neighbors.add(((a, b, f), (d, e, c)))
                neighbors.add(((a, b, c), (d, f, e)))
            
            return neighbors
        
        # Do a bfs starting from the start state
        f_queue = deque()
        f_queue.append(start)
        f_visited[start] = 0
        
        b_queue = deque()
        b_queue.append(goal)
        b_visited[goal] = 0
        
        
        while f_queue and b_queue:
            # Process f_queue
            f_node = f_queue.popleft()
            
            for f_nei in get_neighbors(f_node):
                if f_nei not in f_visited:
                    f_visited[f_nei] = 1 + f_visited[f_node]
                    f_queue.append(f_nei)
                    
                    if f_nei in b_visited:
                        return f_visited[f_nei] + b_visited[f_nei]
            
            # Process b_queue
            b_node = b_queue.popleft()
            
            for b_nei in get_neighbors(b_node):
                if b_nei not in b_visited:
                    b_visited[b_nei] = 1 + b_visited[b_node]
                    b_queue.append(b_nei)
                    
                    if b_nei in f_visited:
                        return b_visited[b_nei] + f_visited[b_nei]
        
        # Impossible to reach goal state
        return -1
                    
                    
                    
        
        