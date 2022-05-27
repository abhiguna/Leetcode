class Solution:
    # Time = O(N)
    # Space = O(1)
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        max_profit = 0
        buy_price = prices[0]
        
        for i in range(1, N):
            max_profit = max(max_profit, prices[i] - buy_price)
            buy_price = min(buy_price, prices[i])
        
        return max_profit
            