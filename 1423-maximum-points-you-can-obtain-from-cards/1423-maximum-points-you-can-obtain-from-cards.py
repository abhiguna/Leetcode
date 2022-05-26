class Solution:
    # Time = O(N)
    # Space = O(1)
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        # Edge cases
        if k == N:
            return sum(cardPoints)
        elif k == 1:
            return max(cardPoints[0], cardPoints[-1])
        
        # Picking k cards that a maximal sum is the same as finding the minimal sum for a sliding window of
        #.  size N - k
        L = N - k
        window_sum = 0
        
        for i in range(L):
            window_sum += cardPoints[i]
        
        min_sum = window_sum
            
        for i in range(L, N):
            window_sum += cardPoints[i] - cardPoints[i-L]
            min_sum = min(min_sum, window_sum)
        
        return sum(cardPoints) - min_sum