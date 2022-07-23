class Solution:
    # Time = O(m+n), m: # of edges, n: # of nodes
    # Space = O(n)
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color_map = {
            "red": "black",
            "black": "red"
        }
        n = len(graph)
        visited = [-1] * n
        parent = [-1] * n
        colors = [None] * n
        
        # DFS -> check if valid coloring exists
        def dfs(node, color):
            visited[node] = 1
            colors[node] = color
            
            for nei in graph[node]:
                if visited[nei] == -1:
                    parent[nei] = node
                    is_bipartite = dfs(nei, color_map[color])
                    if not is_bipartite:
                        return False
                else:
                    # Back edge
                    if nei != parent[node]:
                        if colors[nei] == colors[node]:
                            return False
            return True
        
        # Outer Loop -> traverse through all components
        for v in range(n):
            if visited[v] == -1:
                is_bipartite = dfs(v, "red")
                if not is_bipartite:
                    return False
        
        return True