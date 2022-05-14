class Solution:
    # Approach: DP
    
    # Time = O(N^2)
    # Space = O(N)
    def numTrees(self, n: int) -> int:
        # Edge case
        if n == 1: return 1
        
        table = [0 for _ in range(n+1)]
        # Base cases
        table[0], table[1] = 1, 1
        for i in range(2, n+1):
            for k in range(0, i):
                table[i] += table[k] * table[i-k-1]
        
        return table[n]