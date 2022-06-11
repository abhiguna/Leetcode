class Solution:
    # Time = O(M*N)
    # Space = O(M*N)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prev_height):
            if ((r, c) in visit) or \
                (r < 0 or c < 0 or r == M or c == N) or \
                 (heights[r][c] < prev_height):
                return
            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c]) or \
            dfs(r, c+1, visit, heights[r][c]) or \
            dfs(r-1, c, visit, heights[r][c]) or \
            dfs(r, c-1, visit, heights[r][c])
            return
                 
        
        for c in range(N):
            dfs(0, c, pac, heights[0][c])
            dfs(M-1, c, atl, heights[M-1][c])
        
        for r in range(M):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, N-1, atl, heights[r][N-1])
        
        res = []
        for r in range(M):
            for c in range(N):
                 if ((r, c) in atl) and ((r, c) in pac):
                    res.append([r, c])
        return res