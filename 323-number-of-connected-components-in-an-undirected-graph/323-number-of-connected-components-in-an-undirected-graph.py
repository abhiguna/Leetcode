class Solution:
    # Time = O(m+n), m: len(edges)
    # Space = O(m+n)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build the graph -> adj_list
        adj_list = [[] for v in range(n)]
        visited = [-1] * n
        
        def build_graph():
            for (src, dest) in edges:
                adj_list[src].append(dest)
                adj_list[dest].append(src)
            
        build_graph()
        
        # DFS
        def dfs(src):
            visited[src] = 1
            for nei in adj_list[src]:
                if visited[nei] == -1:
                    visited[nei] = 1
                    dfs(nei)
        
        # Explore all unvisited vertices
        num_components = 0
        for v in range(n):
            if visited[v] == -1:
                num_components += 1
                dfs(v)
        
        return num_components
        
        