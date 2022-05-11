class Solution:
    # Approach: DP
    
    # Time = O(N^2)
    # Space = O(1)
    def generate(self, numRows: int) -> List[List[int]]:
        N = numRows
        if N == 1:
            return [[1]]
        if N == 2:
            return [[1], [1, 1]]
        
        table = [[1 for j in range(i)] for i in range(1, N+1)]
        
        for i in range(2, N):
            for j in range(1, i):
                table[i][j] = table[i-1][j] + table[i-1][j-1]
        
        return table