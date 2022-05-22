class Solution:
    # Time = O(logN)
    # Space = O(1)
    def arrangeCoins(self, n: int) -> int:
        start = 0
        end = n
        while start <= end:
            mid = start + (end-start) // 2
            total_coins = (mid * (mid + 1) // 2)
            # Check if mid can form a complete a row in the staircase
            if total_coins == n:
                return mid
            elif total_coins < n:
                start = mid + 1
            else:
                end = mid - 1
        # Cannot form exactly n full rows, end points to the last row
        return end