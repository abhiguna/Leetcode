class Solution:
    # Time = O(C*A), C: len(coins), A: amount
    # Space = O(A)
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Edge case
        if amount == 0:
            return 0
        
        # Initialize
        table = [math.inf] * (amount + 1)
        table[0] = 0
        
        for a in range(1, amount+1):
            for c in coins:
                if c <= a:
                    table[a] = min(table[a], 1 + table[a-c])
        
        # Not possible to form amount
        if table[amount] == math.inf:
            return -1
        
        return table[amount]