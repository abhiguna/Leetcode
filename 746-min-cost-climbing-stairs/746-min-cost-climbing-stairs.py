class Solution:
    # Approach: DP
    
    # Time = O(N)
    # Space = O(1)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        first = cost[0]
        second = cost[1]
        
        # Compute the min cost for the remaining steps upto 1 step before the top floor
        for i in range(2, N):
            third = cost[i] + min(first, second)
            first = second
            second = third
        
        # Min cost of the top floor would be either one floor below it or two floors below it
        return min(first, second)
            