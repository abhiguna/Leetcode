class NumMatrix:
    # Time = O(1)
    # Space = O(M*N)
    def __init__(self, matrix: List[List[int]]):
        # Compute the prefix sums
        self.M = len(matrix)
        self.N = len(matrix[0])
        self.prefix_sums = [[0 for j in range(self.N)] for i in range(self.M)]
        
        # Base cases
        self.prefix_sums[0][0] = matrix[0][0]
        
        # Fill the first row
        for col in range(1, self.N):
            self.prefix_sums[0][col] = matrix[0][col] + self.prefix_sums[0][col-1]
        
        # Fill the first col
        for row in range(1, self.M):
            self.prefix_sums[row][0] = matrix[row][0] + self.prefix_sums[row-1][0]
            
        # Fill the remaining cells
        for row in range(1, self.M):
            for col in range(1, self.N):
                self.prefix_sums[row][col] = matrix[row][col] + \
                                            self.prefix_sums[row-1][col] + \
                                            self.prefix_sums[row][col-1] - \
                                            self.prefix_sums[row-1][col-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Base Cases
        if row1 == 0 and col1 == 0:
            return self.prefix_sums[row2][col2]
        elif col1 == 0:
            return self.prefix_sums[row2][col2] - self.prefix_sums[row1-1][col2]
        elif row1 == 0:
            return self.prefix_sums[row2][col2] - self.prefix_sums[row2][col1-1]
        
        # General Case
        else:
            return self.prefix_sums[row2][col2] - \
                    self.prefix_sums[row1-1][col2] - \
                    self.prefix_sums[row2][col1-1] + \
                    self.prefix_sums[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)