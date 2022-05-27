class Solution:
    # Time = O(N*k)
    # Space = O(N*k) => could be brought down to order O(k)
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        
        # Edge case: N == 0 or k == 0
        if N == 0 or k == 0:
            return 0
        
        # g(k, i) denotes the max profit achievable with <= k transactions upto day i
        # f(k, i) denotes the max profit achievable with <= k transactions when the last sell occurs on day i
        g_table = [[0 for j in range(N)] for i in range(k+1)] # size = (k+1) x N
        f_table = [[0 for j in range(N)] for i in range(k+1)] # size = (k+1) x N
        
        for t in range(1, k+1):
            for d in range(1, N):
                f_table[t][d] = prices[d] - prices[d-1] + max(g_table[t-1][d-1], f_table[t][d-1])
                g_table[t][d] = max(g_table[t][d-1], f_table[t][d])
        
        return g_table[k][N-1]