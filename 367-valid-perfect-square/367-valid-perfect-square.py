class Solution:
    # Time = O(logN)
    # Space = O(1)
    def isPerfectSquare(self, num: int) -> bool:
        start = 0
        end = num
        while start <= end:
            mid = start + (end - start) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                end = mid - 1
            else:
                start = mid + 1
        return False