class Solution:
    # Approach: Sliding window approach
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        N = len(prices)
        window_start = 0 
        for window_end in range(N):
            if prices[window_end] < prices[window_start]:
                window_start = window_end
            else:
                curr_profit = prices[window_end] - prices[window_start]
                max_profit = max(max_profit, curr_profit)
        
        return max_profit
            
        