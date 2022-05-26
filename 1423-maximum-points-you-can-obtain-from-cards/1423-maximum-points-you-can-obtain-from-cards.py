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
        min_sum = sum(cardPoints)
        left = 0
        window_sum = 0
        window_size = N - k
        
        for i in range(N):
            window_sum += cardPoints[i]
            
            # Shrink the window to window size
            while left <= i and (i-left+1) > window_size:
                window_sum -= cardPoints[left]
                left += 1
            
            if i-left+1 == window_size:
                min_sum = min(min_sum, window_sum)
        
        return sum(cardPoints) - min_sum