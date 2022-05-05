class Solution:
    # Time = O(MlogN)
    # Space = O(M + N)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [math.inf for _ in range(n+1)]
        dist[k] = 0
        dist[0] = 0
        
        adj_list = [[] for _ in range(n+1)]
        
        def build_graph():
            for (u, v, weight) in times:
                adj_list[u].append((v, weight))
            return
        
        def dijkstra(src):
            pq = []
            captured = set([src])
            
            # Insert all the adj vertices from src to pq
            for (nei, weight) in adj_list[src]:
                dist[nei] = weight
                heappush(pq, (dist[nei], src, nei))
                
                
            while pq:
                weight, parent, curr = heappop(pq)
                if curr in captured:
                    continue
                    
                captured.add(curr)
                
                for (nei, weight) in adj_list[curr]:
                    if nei not in captured:
                        dist[nei] = min(dist[nei], dist[curr] + weight)
                        heappush(pq, (dist[nei], curr, nei))
                
            
        build_graph()
        dijkstra(k)
        max_dist = max(dist)
        
        # Edge case: not all nodes reachable -> no valid path from k to all nodes
        if max_dist == math.inf:
            return -1
        return max_dist