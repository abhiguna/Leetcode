# Optimal

# Date: 2/2/22
# 30m 2

class Solution:
    # Time: 
    # Space: 
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def less_than(val):
            count = 0
            for row in matrix:
                num_less = bisect.bisect_right(row, val)
                count += num_less
            return count
        
        low = matrix[0][0]
        high = matrix[-1][-1]
        n = len(matrix)
        while low < high:
            mid = (low+high) // 2
            if less_than(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low