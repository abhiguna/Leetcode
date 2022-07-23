class Solution:
    # Time = O(m+n), m: # of edges, n: # of vertices
    # Space = O(n)
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph) 
        visited = [-1] * n
        level = [-1] * n
        parent = [-1] * n
        
        # BFS -> check if component is bipartite
        def bfs(src):
            queue = deque()
            queue.append(src)
            visited[src] = 1
            level[src] = 0
            
            while queue:
                node = queue.popleft()
                
                for nei in graph[node]:
                    if visited[nei] == -1:
                        parent[nei] = node
                        level[nei] = 1 + level[node]
                        visited[nei] = 1
                        queue.append(nei)
                    else:
                        # Cross edge
                        if nei != parent[node]:
                            # Check for odd len cycle -> same level as node
                            if level[nei] == level[node]:
                                return False
            return True
        
        # Outer loop -> traverse through all the components
        for v in range(n):
            if visited[v] == -1:
                is_bipartite = bfs(v)
                if not is_bipartite:
                    return False
        
        return True
        