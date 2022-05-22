class Solution:
    # Time = O(log(x))
    # Space = O(1)
    def mySqrt(self, x: int) -> int:
        # Do binary search
        start = 0
        end = x
        while start <= end:
            mid = start + (end-start) // 2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                start = mid + 1
            else:
                end = mid - 1
        return end