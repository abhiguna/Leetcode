class Solution:
    # Approach: DP
    
    # Time = O(N)
    # Space = O(N)
    def minCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        # Edge case
        if N == 1:
            return min(costs[0])
        
        table = [[0 for j in range(3)] for i in range(N)]
        # Base case
        for color in range(3):
            table[0][color] = costs[0][color]
        
        for house in range(1, N):
            table[house][0] = costs[house][0] + min(table[house-1][1], table[house-1][2])
            table[house][1] = costs[house][1] + min(table[house-1][0], table[house-1][2])
            table[house][2] = costs[house][2] + min(table[house-1][0], table[house-1][1])
        
        return min(table[N-1])
                