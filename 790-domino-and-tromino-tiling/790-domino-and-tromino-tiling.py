class Solution:
    # Time = O(N)
    # Space = O(N) -> could be optimized further to use O(1) aux. space.
    def numTilings(self, n: int) -> int:
        # Edge case
        if n <= 2:
            return n
        
        MOD_VAL = (10**9) + 7
        
        # table[i] denotes the total number of tilings for a 2 x i board
        # table[i] = 2*table[i-1] + table[i-3]
        table = [0 for _ in range(n+1)]
        # Base cases: Need three base cases
        table[1] = 1
        table[2] = 2
        table[3] = 5
        
        for i in range(4, n+1):
            table[i] = 2*table[i-1] + table[i-3]
        
        return table[n] % MOD_VAL
        
        