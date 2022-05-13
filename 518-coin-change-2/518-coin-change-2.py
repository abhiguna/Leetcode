class Solution:
    # Approach: DP
    
    # Time = O(A*N*C), C = max(max_copies), which in the worst case would be A if coin denomination is a 1
    # Space = O(A*N)
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        A = amount
        table = [[0 for j in range(A+1)] for i in range(N+1)]
        table[0][0] = 1
        
        # Base case
        # Fill first row
        for j in range(1, A+1):
            table[0][j] = 0
        
        # Fill first col
        for i in range(1, N+1):
            table[i][0] = 1
        
        # Fill remaining cells
        for i in range(1, N+1):
            for a in range(1, A+1):
                # Exclude choice
                table[i][a] = table[i-1][a]
                # Include choice
                if a - coins[i-1] >= 0:
                    table[i][a] += table[i][a-coins[i-1]]

        return table[N][A]