class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        size = len(board)
        maxsquare = size*size
        
        def numtorowcol(n):
            row = (maxsquare - n) // size
            c = (n-1) % (2*size) # c is in the range of 0 to 2*size - 1
            if c < size:
                col = c
            else:
                col = 2*size - 1 - c
            return (row, col)
            
        
        def minmoves(n):
            q = collections.deque([n])
            visited = {}
            visited[n] = 0 # Records the shortest path distance from the source to this vertex
            while len(q) != 0:
                curr = q.popleft()
                for i in range(1, 7):
                    nxt = curr + i
                    if nxt > maxsquare:
                        continue
                    (r, c) = numtorowcol(nxt)
                    if board[r][c] != -1:
                        nxt = board[r][c]
                    if nxt not in visited:
                        q.append(nxt)
                        visited[nxt] = visited[curr] + 1
                        if nxt == maxsquare:
                            return visited[nxt]
            return -1
        
        
        
        return minmoves(1)