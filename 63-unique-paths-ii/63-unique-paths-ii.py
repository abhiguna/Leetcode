class Solution:
    # Approach: Memoization
    
    # Time = O(M*N)
    # Space = O(max(N, M))
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        
        memo = {}
        
        def num_paths(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            
            # Base cases
            if r < 0 or c < 0 or r >= M or c >= N:
                return 0
            
            if obstacleGrid[r][c] == 1:
                return 0
            
            if r == M - 1 and c == N - 1:
                return 1
            
            memo[(r, c)] = num_paths(r, c+1) + num_paths(r+1, c)
            return memo[(r, c)]
        
        return num_paths(0, 0)