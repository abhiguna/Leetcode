class Solution:
    # Time = O(m+n), m: len(edges)
    # Space = O(m+n)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Build the graph
        adj_list = [[] for v in range(n)]
        visited = [-1] * n
        parent = [-1] * n
        
        def build_graph():
            for (src, dest) in edges:
                adj_list[src].append(dest)
                adj_list[dest].append(src)
                
        build_graph()
        
        # DFS -> return True if cycle exists else False
        def dfs(node):
            visited[node] = 1
            for nei in adj_list[node]:
                if visited[nei] == -1:
                    parent[nei] = node
                    has_cycle = dfs(nei)
                    if has_cycle:
                        return True
                else:
                    # Back edge / cross edge
                    if parent[node] != nei:
                        return True
            return False
                    
        
        # Outer loop -> counts num components and checks if acyclic
        num_components = 0
        for v in range(n):
            if visited[v] == -1:
                num_components += 1
                # Edge case: check if graph not connected
                if num_components > 1:
                    return False
                has_cycle = dfs(v)
                if has_cycle:
                    return False
        
        return True
                
                
        