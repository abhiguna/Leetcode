# Date: 2/3/22
# 30m 3
class Solution:
    # Time = O(n)
    # Space = O(1)
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        M = N - k
        total_sum = sum(cardPoints)
        min_sum = sum(cardPoints[:M])
        curr_sum = min_sum
        for i in range(k):
            curr_sum -= cardPoints[i]
            curr_sum += cardPoints[i+M]
            min_sum = min(min_sum, curr_sum)
        return total_sum - min_sum