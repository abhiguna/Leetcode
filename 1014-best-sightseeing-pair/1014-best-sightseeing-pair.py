class Solution:
    # Time = O(N)
    # Space = O(N) -> could be brought down to O(1)
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        N = len(values)
        f_table = [0] * N
        h_table = [0] * N
        for i in range(1, N):
            # Update h(i): max_score of a ss_pair ending at i
            h_table[i] = max(values[i]+values[i-1]-1, h_table[i-1] + (values[i]-values[i-1]) - 1)
            # Update f(i): max_score of a ss_pair when values upto idx i are considered
            f_table[i] = max(f_table[i-1], h_table[i])
        
        return f_table[N-1]