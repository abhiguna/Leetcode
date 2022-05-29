class Solution:
    # Time = O(1)
    # Space = O(1)
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        return 3**19 % n == 0