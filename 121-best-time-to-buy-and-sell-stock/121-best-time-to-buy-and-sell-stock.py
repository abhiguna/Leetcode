class Solution:
    # Time = O(N)
    # Space = O(1)
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        buy_price = prices[0]
        max_profit = 0
        
        for i in range(1, N):
            max_profit = max(max_profit, prices[i] - buy_price)
            
            if prices[i] - buy_price < 0:
                buy_price = prices[i]
        
        return max_profit
                