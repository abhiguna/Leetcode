class Solution:
    # Time = O(sqrt(N))
    # Space = O(1)
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        k = 1
        while (n - (k*(k-1)/2)) > 0:
            # Check if the k value is legal such that n is reachable
            if (n - (k*(k-1))/2) % k == 0:
                count += 1
            k += 1
        
        return count
            