class Solution:
    # Time = O(mlog(m)) -> O(mlog(n)), m: len(times), n: # of nodes
    # Space = O(m)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for v in range(n+1)]
        
        def build_graph():
            for (src, dest, weight) in times:
                adj_list[src].append((dest, weight))
        
        # Build the graph
        build_graph()
        
        dist = [math.inf] * (n+1)
        dist[0] = 0
        
        captured = [-1] * (n+1) # Stores whether a given vertex has been captured
        captured[0] = 1
    
        
        def dijkstra(src):
            # Insert all the neighbors of the src node into a min heap
            min_heap = []
            heappush(min_heap, (0, src))
            
            while min_heap:
                (shortest_dist, node) = heappop(min_heap)
                # Only update the shortest dist value for a node only if not captured before
                if captured[node] == -1:
                    dist[node] = shortest_dist
                    captured[node] = 1

                    for (nei, nweight) in adj_list[node]:
                        if captured[nei] == -1:
                            heappush(min_heap, (dist[node] + nweight, nei))
                        
        
        dijkstra(k)

        
        min_time = max(dist)
        if min_time == math.inf:
            return -1
        
        return min_time
    