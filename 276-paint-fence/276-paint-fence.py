class Solution:
    # Approach: DP
    
    # Time = O(N)
    # Space = O(N)
    def numWays(self, n: int, k: int) -> int:
        # Edge case
        if n == 1:
            return k
        
        # same[i] = different[i-1] since no 3 consecutive posts can have the same color
        # different[i] = (k-1) * [same[i-1] + different[i-1]]
        same = [0 for _ in range(n+1)]
        different = [0 for _ in range(n+1)]
        
        # Base cases
        same[1], same[2] = k, k
        different[1], different[2] = k, k*(k-1)
        
        for post in range(3, n+1):
            same[post] = different[post - 1]
            different[post] = (k-1) * (same[post-1] + different[post-1])
        
        return same[n] + different[n]