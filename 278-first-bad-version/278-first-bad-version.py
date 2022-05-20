# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # Time = O(logN)
    # Space = O(1)
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start <= end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        
        # Let x be the boundary between the last good product and the first bad product
        # Then start will be the first element > x
        # And end will be the last element < x
        return start