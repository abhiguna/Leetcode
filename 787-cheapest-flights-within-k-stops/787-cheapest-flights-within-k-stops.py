class Solution:
    # Time = O(m*k)
    # Space = O(n*k)
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        table = [[math.inf for j in range(k+2)] for i in range(n)]
        # Base case
        table[src][0] = 0
        
        for col in range(1, k+2):
            # Initialization
            for v in range(n):
                table[v][col] = table[v][col-1]
            for (u, v, w) in flights:
                    table[v][col] = min(table[v][col], table[u][col-1] + w)
        
        # Cannot reach dest within k stops
        if table[dst][k+1] == math.inf:
            return -1
        
        return table[dst][k+1]