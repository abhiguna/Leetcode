class Solution:
    # Time = O(N)
    # Space = O(1)
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        max_profit = 0
        for i in range(1, N):
            max_profit = max_profit + max(0, (prices[i] - prices[i-1]))
        
        return max_profit