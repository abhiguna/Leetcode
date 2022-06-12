class Solution:
    # Time = O(m+n), m: len(edges), n: # of nodes
    # Space = O(m+n)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for i in range(n)]
        parent = [-1] * n
        visited = set()
        
        def build_graph():
            for (src, dest) in edges:
                adj_list[src].append(dest)
                adj_list[dest].append(src)
        
        build_graph()
        
        def dfs(src):
            visited.add(src)
            
            for nei in adj_list[src]:
                # Tree edge
                if nei not in visited:
                    parent[nei] = src
                    has_cycle = dfs(nei)
                    if has_cycle:
                        return True
                # Back edge
                else:
                    if parent[src] != nei:
                        return True
            return False
        
        num_components = 0
        for v in range(n):
            if v not in visited:
                num_components += 1
                # Graph not connected
                if num_components > 1:
                    return False
                has_cycle = dfs(v)
                if has_cycle:
                    return False
        
        return True
        