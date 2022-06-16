class Solution:
    # Time = O(m*k)
    # Space = O(n)
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [math.inf] * n
        prices[src] = 0
        
        # Update prices array to hold min price for each stop from [0, k]
        for stops in range(0, k+1):
            tmp_prices = prices[:]
            for (u, v, weight) in flights:
                if prices[u] == math.inf:
                    continue
                if prices[u] + weight < tmp_prices[v]:
                    tmp_prices[v] = prices[u] + weight
            prices = tmp_prices
            
        if prices[dst] == math.inf:
            return -1
        
        return prices[dst]