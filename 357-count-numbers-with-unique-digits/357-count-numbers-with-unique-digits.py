class Solution:
    # Time = O(N)
    # Space = O(1)
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # n: represents the number of digits
        # f(n) denotes the number of values with distinct digits if upto n digits are considered(i.e. no digit should appear more than once)
        
        # Edge case: n == 0
        if n == 0:
            return 1
        
        # If n == 1, 0...9 digits can be used
        if n == 1:
            return 10
        
        # Base case:
        # If n > 2, 0 cannot be used in a 2-digit number
        total = 10
        curr = 9
        for i in range(2, n+1):
            # Compute f(i) and add it to the total
            curr = curr * (10-(i-1))
            total += curr
        
        return total