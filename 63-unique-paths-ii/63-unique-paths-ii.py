class Solution:
    # Approach: DP
    
    # Time = O(M*N)
    # Space = O(M*N)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        table = [[0 for j in range(N)] for i in range(M)]
        table[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
        
        # First row
        for j in range(1, N):
            if obstacleGrid[0][j] == 1:
                # Obstacle exists
                table[0][j] = 0
            else:
                table[0][j] = table[0][j-1]
        
        # First col
        for i in range(1, M):
            if obstacleGrid[i][0] == 1:
                table[i][0] = 0
            else:
                table[i][0] = table[i-1][0]
        
        # Fill the remaining cells
        for i in range(1, M):
            for j in range(1, N):
                # Check if obstacle exists at [i][j]
                if obstacleGrid[i][j] == 1:
                    table[i][j] = 0
                else:
                    table[i][j] = table[i-1][j] + table[i][j-1]
        
        return table[M-1][N-1]