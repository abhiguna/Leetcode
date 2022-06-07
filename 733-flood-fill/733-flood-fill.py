class Solution:
    # Time = O(M*N)
    # Space = O(max(M, N))
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        M, N = len(image), len(image[0])
        
        # Edge case:
        if image[sr][sc] == newColor:
            return image
        
        def getNeighbors(r, c):
            neighbors = []
            if r + 1 < M:
                neighbors.append((r+1, c))
            if c + 1 < N:
                neighbors.append((r, c+1))
            if r - 1 >= 0:
                neighbors.append((r-1, c))
            if c - 1 >= 0:
                neighbors.append((r, c-1))
            return neighbors
            
        def bfs():
            queue = deque()
            queue.append((sr, sc))
            old_color = image[sr][sc]
            image[sr][sc] = newColor
            
            
            while queue:
                (r, c) = queue.popleft()
                
                for (nr, nc) in getNeighbors(r, c):
                    if image[nr][nc] == old_color:
                        image[nr][nc] = newColor
                        queue.append((nr, nc))
            
            return
            
            
        
        
        bfs()
        return image