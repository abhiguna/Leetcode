class Solution:
    # Time = O(N)
    # Space = O(1)
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        max_profit = 0
        curr_profit = 0
        
        for i in range(1, N):
            curr_profit = prices[i] - prices[i-1] + max(0, curr_profit)
            max_profit = max(max_profit, curr_profit)
        
        return max_profit
            