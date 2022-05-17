class Solution:
    # Time = O(N)
    # Space = O(1)
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N == 0:
            return 0
        max_profit = 0
        min_so_far = prices[0]
        for i in range(N):
            if prices[i] < min_so_far:
                # Found a new min
                min_so_far = prices[i]
            if max_profit < prices[i] - min_so_far:
                max_profit = prices[i] - min_so_far
        return max_profit