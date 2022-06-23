class Solution:
    # Time = O(1)
    # Space = O(1)
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        ((u, v, w), (x, y, z)) = board
        start = ((u, v, w), (x, y, z))
        goal = ((1, 2, 3), (4, 5, 0))
        
        # Edge case: already at goal state
        if start == goal:
            return 0
        
        def get_neighbors(state):
            ((a, b, c), (d, e, f)) = state        
            neighbors = []
            
            if a == 0:
                neighbors.append(((b, a, c), (d, e, f)))
                neighbors.append(((d, b, c), (a, e, f)))
            elif b == 0:
                neighbors.append(((b, a, c), (d, e, f)))
                neighbors.append(((a, c, b), (d, e, f)))
                neighbors.append(((a, e, c), (d, b, f)))
            elif c == 0:
                neighbors.append(((a, c, b), (d, e, f)))
                neighbors.append(((a, b, f), (d, e, c)))
            elif d == 0:
                neighbors.append(((d, b, c), (a, e, f)))
                neighbors.append(((a, b, c), (e, d, f)))
            elif e == 0:
                neighbors.append(((a, e, c), (d, b, f)))
                neighbors.append(((a, b, c), (e, d, f)))
                neighbors.append(((a, b, c), (d, f, e)))
            else:
                neighbors.append(((a, b, f), (d, e, c)))
                neighbors.append(((a, b, c), (d, f, e)))
            
            return neighbors

        visited = set()
        
        # BFS
        queue = deque()
        queue.append((start, 0))
        
        while queue:
            (curr, path_len) = queue.popleft()
            
            for nei in get_neighbors(curr):
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, path_len+1))
                    if nei == goal:
                        return path_len + 1
        
        return -1
        