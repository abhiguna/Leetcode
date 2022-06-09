class Solution:
    # Time = O(m*n)
    # Space = O(n)
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[1 for j in range(n)] for i in range(2)]
        
        for i in range(1, m):
            for j in range(1, n):
                table[i%2][j] = table[(i-1)%2][j] + table[(i%2)][j-1]
        
        return table[(m-1)%2][n-1]