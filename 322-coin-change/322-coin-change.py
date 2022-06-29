"""
f(a) = min coins needed to satisfy a
f(a) = 1 + min(f(a-c1), f(a-c2), f(a-c3)) 
"""
class Solution:
    # Time = O(A*C), A: amount, C: len(coins)
    # Space = O(A)
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Edge case: amount = 0
        if amount == 0:
            return 0
        
        table = [math.inf] * (amount+1)
        table[0] = 0
        
        for a in range(1, amount+1):
            for c in coins:
                if c <= a:
                    table[a] = min(table[a], 1 + table[a-c])
        
        # Edge case: unable to make amount
        if table[amount] == math.inf:
            return -1
        
        return table[amount]