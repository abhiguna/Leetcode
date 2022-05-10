class Solution:
    # Approach: DP
    
    # Time = O(N)
    # Space = O(N)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        table = [0] * N
        # Base cases: start from step 0 or step 1
        table[0] = cost[0]
        table[1] = cost[1]
        
        # Compute the min cost for the remaining steps upto 1 step before the top floor
        for i in range(2, N):
            table[i] = cost[i] + min(table[i-1], table[i-2])
        
        # Min cost of the top floor would be either one floor below it or two floors below it
        return min(table[N-1], table[N-2])
            