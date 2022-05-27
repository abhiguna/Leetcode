class Solution:
    # Time = O(N)
    # Space = O(N)
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        g_table = [0] * N
        f_table = [0] * N
        
        for i in range(1, N):
            f_table[i] = (prices[i] - prices[i-1]) + max(g_table[i-1], f_table[i-1])
            g_table[i] = max(g_table[i-1], f_table[i] - fee)
        
        return g_table[N-1]
        