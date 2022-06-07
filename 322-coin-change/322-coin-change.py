class Solution:
    # Time = O(A*C), C: len(coins), A: amount
    # Space = O(A)
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Edge case:
        if amount == 0:
            return 0
        
        C = len(coins)
        A = amount
        
        table = [math.inf] * (A+1)
        table[0] = 0
        
        for a in range(1, A+1):
            for c in coins:
                if c <= a:
                    table[a] = min(table[a], 1 + table[a-c])
        
        if table[A] == math.inf:
            return -1
        
        return table[A]
        
        
        