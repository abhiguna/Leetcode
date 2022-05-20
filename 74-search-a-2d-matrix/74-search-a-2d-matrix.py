class Solution:
    # Time = O(logN)
    # Space = O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        # Edge case: if matrix is empty -> return False
        if M == 0:
            return False
        
        N = len(matrix[0])
        start = 0
        end = M*N - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            row = mid // N
            col = mid % N
            
            # < t | = t | > t
            # Target found
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        # Target not found
        return False