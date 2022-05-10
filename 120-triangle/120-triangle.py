class Solution:
    # Time = O(N^2)
    # Space = O(N^2)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        table = [[0 for c in range(len(triangle[r]))] for r in range(N)]
        # Base cases
        table[0][0] = triangle[0][0]
        
        for r in range(1, N):
            table[r][0] = triangle[r][0] + table[r-1][0]
            table[r][r] = triangle[r][r] + table[r-1][r-1]
        
        for r in range(2, N):
            for c in range(1, r):
                table[r][c] = triangle[r][c] + min(table[r-1][c], table[r-1][c-1])
        
        return min(table[N-1])