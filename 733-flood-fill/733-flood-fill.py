class Solution:
    # Time = O(M*N)
    # Space = O(max(M, N))
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        M, N = len(image), len(image[0])
        
        # Edge case: the source pixel is already in the new color -> no modification required
        if image[sr][sc] == newColor:
            return image
        
        def get_neighbors(row, col):
            neighbors = []
            if row+1 < M:
                neighbors.append((row+1, col))
            if col+1 < N:
                neighbors.append((row, col+1))
            if row-1 >= 0:
                neighbors.append((row-1, col))
            if col-1 >= 0:
                neighbors.append((row, col-1))
            
            return neighbors
        
        queue = deque()
        queue.append((sr, sc))
        old_color = image[sr][sc]
        image[sr][sc] = newColor
        
        while queue:
            (row, col) = queue.popleft()
            
            for (nrow, ncol) in get_neighbors(row, col):
                if image[nrow][ncol] == old_color:
                    image[nrow][ncol] = newColor
                    queue.append((nrow, ncol))
        
        return image
        
        
        
        
        
        
        