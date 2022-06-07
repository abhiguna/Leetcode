class Solution:
    # Time = O(N)
    # Space = O(1)
    def climbStairs(self, n: int) -> int:
        # Edge case
        if n == 1:
            return 1
        
        # Define the base cases
        first = 1
        second = 2
        
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        
        return second