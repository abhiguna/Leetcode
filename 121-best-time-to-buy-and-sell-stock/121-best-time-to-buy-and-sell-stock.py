class Solution:
    # Time = O(N)
    # Space = O(1)
    def maxProfit(self, prices: List[int]) -> int:
        # D&C Approach
        N = len(prices)
        buy_price = prices[0]
        max_profit = 0
        for i in range(1, N):
            # Update max_profit
            max_profit = max(max_profit, prices[i] - buy_price)
            # Update buy_price
            buy_price = min(buy_price, prices[i])
        return max_profit