class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # Edge case: already at target loc
        if (x, y) == (0, 0):
            return 0
        
        def get_neighbors(row, col):
            # At most 8 neighbors
            return [(row+2, col+1), (row+2, col-1), (row+1, col+2), (row+1, col-2), \
                    (row-2, col+1), (row-2, col-1), (row-1, col+2), (row-1, col-2)]
        
        # Start a bidirectional BFS
        f_visited = {(0, 0): 0} # f_visited[(i, j)] := the min moves needed to reach (i, j) from (0, 0)
        b_visited = {(x, y): 0} # b_visited[(i, j)] := the min moves needed to reach (i, j) from (x, y)
        
        f_queue = deque()
        f_queue.append((0, 0))
        b_queue = deque()
        b_queue.append((x, y))
        
        while f_queue and b_queue:
            # Process forward queue
            (fi, fj) = f_queue.popleft()
            
            for (nfi, nfj) in get_neighbors(fi, fj):
                if (nfi, nfj) not in f_visited:
                    f_visited[(nfi, nfj)] = 1 + f_visited[(fi, fj)]
                    f_queue.append((nfi, nfj))
                    # Found answer
                    if (nfi, nfj) in b_visited:
                        return f_visited[(nfi, nfj)] + b_visited[(nfi, nfj)]
            
            # Process backward queue
            (bi, bj) = b_queue.popleft()
            
            for (nbi, nbj) in get_neighbors(bi, bj):
                if (nbi, nbj) not in b_visited:
                    b_visited[(nbi, nbj)] = 1 + b_visited[(bi, bj)]
                    b_queue.append((nbi, nbj))
                    # Found answer
                    if (nbi, nbj) in f_visited:
                        return f_visited[(nbi, nbj)] + b_visited[(nbi, nbj)]
            
        # Will never reach here -> return placeholder
        return math.inf