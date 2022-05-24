class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        buy_price = prices[0]
        max_profit = 0
        
        for i in range(1, N):
            curr_profit = prices[i] - buy_price
            if curr_profit < 0:
                buy_price = prices[i]
            else:
                max_profit = max(max_profit, curr_profit)
        
        return max_profit