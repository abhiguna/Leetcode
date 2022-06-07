class Solution:
    # Time = O(M*N)
    # Space = O(1)
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        dist = [[math.inf for j in range(N)] for i in range(M)]
        
        # First pass to update dist based on the top and left values
        for r in range(M):
            for c in range(N):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                else:
                    if r > 0:
                        dist[r][c] = min(dist[r][c], 1 + dist[r-1][c])
                    if c > 0:
                        dist[r][c] = min(dist[r][c], 1 + dist[r][c-1])
        
        # Second reverse pass to update dist based on the bottom and right values
        for r in range(M-1, -1, -1):
            for c in range(N-1, -1, -1):
                if mat[r][c] == 0:
                    dist[r][c] == 0
                else:
                    if r < M-1:
                        dist[r][c] = min(dist[r][c], 1 + dist[r+1][c])
                    if c < N-1:
                        dist[r][c] = min(dist[r][c], 1 + dist[r][c+1])
        
        return dist