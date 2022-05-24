class Solution:
    # Time = O(M*N)
    # Space = O(M*N) -> could be brought down to O(M)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # D&C Approach
        M = len(matrix)
        N = len(matrix[0])
        
        # dp table
        table = [[0 for _ in range(N)] for _ in range(M)]
        
        # The global_max keeps track of the side len of the maximum square
        global_max = 0
        
        # Base cases
        # Fill first row
        for col in range(N):
            if matrix[0][col] == "1":
                table[0][col] = 1
                global_max = 1
        
        # Fill first column
        for row in range(M):
            if matrix[row][0] == "1":
                table[row][0] = 1
                global_max = 1
        
        # Fill in remaining cells
        for row in range(1, M):
            for col in range(1, N):
                if matrix[row][col] == "1":
                    table[row][col] = 1 + min(table[row-1][col], table[row-1][col-1], table[row][col-1])
                    global_max = max(global_max, table[row][col])
        
        # Return the area of the maximal square, whose side length is global_max
        return global_max ** 2