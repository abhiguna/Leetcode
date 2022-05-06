# Approach 1: Prim's Algorithm
class Solution:
    # Time = O(N^2logN)
    # Space = O(N^2)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj_list = [[] for _ in range(N)]
        
        def compute_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        def build_graph():
            for i in range(N-1):
                for j in range(i+1, N):
                    dist = compute_dist(points[i], points[j])
                    adj_list[i].append((j, dist))
                    adj_list[j].append((i, dist))
            return
        
        min_cost = [0]
        visited = set()
        pq = []
        
        def prims():
            visited.add(0)
            for (nei, weight) in adj_list[0]:
                heappush(pq, (weight, nei))
            
            while pq:
                weight, curr = heappop(pq)
                if curr in visited:
                    continue
                visited.add(curr)
                min_cost[0] += weight
                
                # Graph connected when all nodes visited
                if len(visited) == N:
                    break
                
                for (nei, weight) in adj_list[curr]:
                    if nei not in visited:
                        heappush(pq, (weight, nei))
            return
        
        build_graph()
        prims()
        return min_cost[0]
        