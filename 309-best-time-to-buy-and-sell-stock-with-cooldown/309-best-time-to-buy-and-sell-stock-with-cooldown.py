class Solution:
    # Time = O(N)
    # Space = O(N)
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        # g(i) = max profit achieved with t transactions if upto i+1 days are considered
        # f(i) = max profit achieved with t transactions if a sell happens of day i
        
        gtable = [0] * N
        ftable = [0] * N
        
        for i in range(1, N):
            buy_previous = 0 if i < 3 else gtable[i-3]
            ftable[i] = (prices[i]-prices[i-1]) + max(buy_previous, ftable[i-1])
            gtable[i] = max(gtable[i-1], ftable[i])
        
        return gtable[N-1]