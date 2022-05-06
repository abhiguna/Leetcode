class Solution:
    # Time = O(M + N)
    # Space = O(M + N)
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        M = len(edges)
        adj_list = [[] for _ in range(n)]
        
        def build_graph():
            for (u,v) in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)
            return
        
        visited = set()
        parent = [-1] * n
        timestamp = [0]
        
        def dfs(src):
            visited.add(src)
            
            for nei in adj_list[src]:
                # Neighbor not visited
                if nei not in visited:
                    parent[nei] = src
                    has_cycle = dfs(nei)
                    if has_cycle: return True
                else:
                    # Check for back edge -> cycle!
                    # For undirected graphs -> compare parents of src and neighbor
                    if parent[src] != nei:
                        return True
                    
            return False
            
        
        build_graph()
        num_components = 0
        for v in range(n):
            if v not in visited:
                num_components += 1
                # A tree must be connected!
                if num_components > 1:
                    return False
                has_cycle = dfs(v)
                if has_cycle: return False
        
        return True