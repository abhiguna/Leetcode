class Solution:
    # Approach: DP
    
    # Time = O(N*A)
    # Space = O(A)
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        
        # table[i] = number of different comb. of coin changes to achieve a target of amount
        
        table = [0 for _ in range(amount + 1)]
        table[0] = 1
        
        for i in range(1, N+1):
            for a in range(1, amount+1):
                if a - coins[i-1] >= 0:
                    table[a] += table[a-coins[i-1]]
        
        return table[amount]