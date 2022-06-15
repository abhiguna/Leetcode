class Solution:
    # Time = O(mlogm) -> O(nlogn) for sparse graphs, m: len(edges), n: # of nodes in the graph
    # Space = O(m + n)
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj_list = [[] for v in range(n)]
        
        def build_graph():
            for idx in range(len(edges)):
                (src, dest) = edges[idx]
                sp = succProb[idx]
                # Set the dist as the modified value => -log(sp) if sp is the success probability
                adj_list[src].append((dest, -log(sp)))
                adj_list[dest].append((src, -log(sp)))
        
        build_graph()
        
        captured = [-1] * n
        dist = [math.inf] * n
        
        def dijkstra(src):
            min_heap = []
            heappush(min_heap, (0, src))
            
            while min_heap:
                (shortest_dist, node) = heappop(min_heap)
                
                if captured[node] == -1:
                    captured[node] = 1
                    dist[node] = shortest_dist
                    
                    for (nei, ndist) in adj_list[node]:
                        if captured[nei] == -1:
                            heappush(min_heap, (dist[node] + ndist, nei))
            
            # Could not reach target
            if captured[end] == -1:
                return 0
            
            x = dist[end]
            return math.exp(-x)
        
        # We try to minimize the sum -log(sp) values 
        return dijkstra(start)