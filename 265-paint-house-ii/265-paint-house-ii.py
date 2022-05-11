class Solution:
    # Approach: DP
    
    # Time = O(N*k)
    # Space = O(N*K) -> could be brought down to O(k)
    def minCostII(self, costs: List[List[int]]) -> int:
        N = len(costs)
        # Edge case
        if N == 1:
            return min(costs[0])
        k = len(costs[0])
        table = [[0 for j in range(k)] for i in range(N)]
        
        def find_mins(house):
            fmin = min(table[house])
            fcol = table[house].index(fmin)
            smin = math.inf
            scol = -1
            for (color, cost) in enumerate(table[house]):
                if color != fcol and cost <= smin and cost >= fmin:
                    smin = cost
                    scol = color
            return (fmin, fcol, smin, scol)
        
        # Base case -> Fill first row
        for color in range(k):
            table[0][color] = costs[0][color]
        
        fmin, fcol, smin, scol = find_mins(0)
        
        # Fill in remaining cells
        for h in range(1, N):
            for c in range(k):
                if fcol == c:
                    table[h][c] = costs[h][c] + smin 
                else:
                    table[h][c] = costs[h][c] + fmin
            fmin, fcol, smin, scol = find_mins(h)
        
        return min(table[N-1])
        
        