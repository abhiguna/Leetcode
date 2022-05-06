class Solution:
    # Time = O(N^2logN)
    # Space = O(N^2)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edge_list = []
        N = len(points)
        
        def compute_dist(p1, p2):
            return int(abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))
        
        def build_graph():
            for i in range(N-1):
                for j in range(i+1, N):
                    dist = compute_dist(points[i], points[j])
                    # Undirected graph -> Store two copies of each edge
                    edge_list.append([i, j, dist])
                    edge_list.append([j, i, dist])
            return
            
        min_cost = [0]
        num_components = [N]
        parent = [i for i in range(N)]
        size = [1]*N
        
        def find(node):
            # Base case: root node
            if parent[node] == node:
                return node
            # Recursive case: internal node
            root = find(parent[node])
            parent[node] = root
            return root
        
        def kruskals():
            # Sort by edge-weight
            edge_list.sort(key = lambda x: x[2])
            # print(edge_list)
            for (u, v, weight) in edge_list:
                root_u = find(u)
                root_v = find(v)
                if root_u != root_v:
                    if size[root_u] < size[root_v]:
                        parent[root_u] = root_v
                        size[root_v] += size[root_u]
                    else:
                        parent[root_v] = root_u
                        size[root_u] += size[root_v]
                        
                    min_cost[0] += weight
                    num_components[0] -= 1
                    if num_components[0] == 1:
                        break
            return
            
        build_graph()
        kruskals()
        return min_cost[0]
        