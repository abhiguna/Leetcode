class Solution:
    # Time = O(N)
    # Space = O(1)
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        buy = 0
        max_profit = 0
        curr_profit = 0
        
        for sell in range(N):
            if prices[sell] - prices[buy] < 0:
                buy = sell
            else:
                curr_profit = max(curr_profit, prices[sell] - prices[buy])
                max_profit = max(max_profit, curr_profit)
        
        return max_profit