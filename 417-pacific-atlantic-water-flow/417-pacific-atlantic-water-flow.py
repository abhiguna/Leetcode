class Solution:
    # Time = O(M*N)
    # Space = O(M*N)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M = len(heights)
        N = len(heights[0])
        
        pacific = set() # Maintains reachable cells from pacific
        atlantic = set() # Maintains reachable cells from atlantic
        
        
        def dfs(row, col, visit, prev_height):
            # Base case
            if row<0 or row>=M or col<0 or col>=N or ((row,col) in visit) or \
                heights[row][col]<prev_height:
                return
            
            visit.add((row, col))
            dfs(row+1, col, visit, heights[row][col])
            dfs(row-1, col, visit, heights[row][col])
            dfs(row, col+1, visit, heights[row][col])
            dfs(row, col-1, visit, heights[row][col])
            return
        
        # Run dfs from start row and end row
        for c in range(N):
            dfs(0, c, pacific, heights[0][c])
            dfs(M-1, c, atlantic, heights[M-1][c])
            
        # Run dfs from start col and end col
        for r in range(M):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, N-1, atlantic, heights[r][N-1])
        
        res = []
        for r in range(M):
            for c in range(N):
                if (r,c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res
        
        
        