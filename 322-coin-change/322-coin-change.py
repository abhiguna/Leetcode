class Solution:
    # Approach: DP
    
    # Time = O(A*C)
    # Space = O(A)
    def coinChange(self, coins: List[int], amount: int) -> int:
        C = len(coins)
        A = amount
        table = [math.inf for _ in range(A+1)]
        # Base case
        table[0] = 0
        
        for a in range(1, A+1):
            for c in coins:
                if (a - c) >= 0:
                    table[a] = min(table[a], 1 + table[a-c])
        
        if table[A] == math.inf:
            return -1
        
        return table[A]