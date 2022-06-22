class Solution:
    # Time = O(n*C)
    # Space = O(n)
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        C = len(coins)
        # Edge case
        if n == 0:
            return 0
        
        table = [math.inf] * (n+1)
        table[0] = 0
        
        for a in range(1, n+1):
            for c in coins:
                if c <= a:
                    table[a] = min(table[a], 1 + table[a-c])
        
        if table[n] == math.inf:
            return -1
        
        return table[n]