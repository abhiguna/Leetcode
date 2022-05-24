class Solution:
    # Time = O(N)
    # Space = O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # We compare the top-right element with the target to eliminate either a row or a column
        M, N = len(matrix), len(matrix[0])
        min_row = 0
        max_col = N - 1
        while min_row < M and max_col >= 0:
            # Target found
            if target == matrix[min_row][max_col]:
                return True
            elif target > matrix[min_row][max_col]:
                min_row += 1
            else:
                max_col -= 1
        # Target not found
        return False