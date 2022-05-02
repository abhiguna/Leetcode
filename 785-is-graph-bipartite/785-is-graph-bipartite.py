class Solution:
    # Time = O(N + M), N: num of nodes, M: num of edges
    # Space = O(N + M)
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        colored = [-1] * N
        inv_color = {
            "Y": "G",
            "G": "Y"
        }
        
        def dfs(src, color):
            nonlocal colored
            colored[src] = color
            
            for neighbor in graph[src]:
                if colored[neighbor] == -1:
                    is_bipartite = dfs(neighbor, inv_color[colored[src]])
                    if not is_bipartite:
                        return False
                elif colored[neighbor] == colored[src]:
                    return False # Not bipartite
            return True
        
        for src in range(N):
            if colored[src] == -1:
                is_bipartite = dfs(src, "Y")
                if not is_bipartite:
                    return False
        
        return True
                