class Solution:
    # Approach: DP
    
    # Time = O(M*N)
    # Space = O(M*N)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        table = [0 for j in range(N)]
        table[0] = 0 if obstacleGrid[0][0] == 1 else 1
        
        # First row
        for j in range(1, N):
            if obstacleGrid[0][j] == 1:
                # Obstacle exists
                table[j] = 0
            else:
                table[j] = table[j-1]
        
        # Fill the remaining cells
        for i in range(1, M):
            prev = table[:]
            
            if obstacleGrid[i][0] == 1:
                table[0] = 0
            else:
                table[0] = prev[0]
            
            temp = table[0]
            
            for j in range(1, N):
                # Check if obstacle exists at [i][j]
                if obstacleGrid[i][j] == 1:
                    temp = 0
                else:
                    temp = temp + prev[j]
                
                table[j] = temp
        
        return table[N-1]