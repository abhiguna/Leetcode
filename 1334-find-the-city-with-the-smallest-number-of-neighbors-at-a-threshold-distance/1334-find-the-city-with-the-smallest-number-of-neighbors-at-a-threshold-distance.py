class Solution:
    # Time = O(n^3)
    # Space = O(n^2)
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Allocate a 2D table of size nxn
        table = [[math.inf for j in range(n)] for i in range(n)]

        # Base case: no intermediate vertices
        # Fill diagonal with 0s since it takes 0 distance to go from a node to itself
        for row in range(n):
            table[row][row] = 0
        for (u, v, weight) in edges:
            # Have 2 copies if the graph is undirected
            table[u][v] = weight
            table[v][u] = weight

        # General case: consider every vertex from 0,...,n-1 to be the intermediate vertex
        # f(u, v, i) = f(u, i, i-1) + f(i, v, i-1), where i is the intermediate vertex & 
        # (u,v) is current pair of vertices.
        for i in range(n):
            for row in range(n):
                for col in range(n):
                    table[row][col] = min(table[row][col], table[row][i] + table[i][col])

        # The table contains the shortest distance considering all pairs of vertices
        cities_reached = math.inf 
        best_city = 0
        for row in range(n):
            count = 0
            for col in range(n):
                if table[row][col] <= distanceThreshold:
                    count += 1
            if count <= cities_reached:
                cities_reached = count
                best_city = row
        
        return best_city
	