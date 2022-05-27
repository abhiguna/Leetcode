class Solution:
    # Time = O(N)
    # Space = O(N) -> could be brought down to O(1)
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        f1_table = [0] * N
        g1_table = [0] * N
        f2_table = [0] * N
        g2_table = [0] * N
        
        for i in range(1, N):
            delta = prices[i] - prices[i-1]
            f1_table[i] = delta + max(0, f1_table[i-1])
            g1_table[i] = max(g1_table[i-1], f1_table[i])
            f2_table[i] = delta + max(g1_table[i-1], f2_table[i-1])
            g2_table[i] = max(g2_table[i-1], f2_table[i])
        
        return g2_table[N-1]