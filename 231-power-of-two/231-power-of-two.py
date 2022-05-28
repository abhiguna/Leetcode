class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Edge case: if n == 0
        if n == 0:
            return False
        return (n & (n-1)) == 0