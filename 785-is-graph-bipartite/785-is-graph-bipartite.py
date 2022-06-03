class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        visited = [-1] * N
        parent = [-1] * N
        level = [-1] * N
        
        def bfs(src):
            queue = deque()
            queue.append(src)
            visited[src] = 1
            level[src] = 0
            
            while queue:
                node = queue.popleft()
                
                for nei in graph[node]:
                    if visited[nei] == -1:
                        visited[nei] = 1
                        parent[nei] = node
                        level[nei] = level[node] + 1
                        queue.append(nei)
                    else:
                        # Cross-edge
                        if parent[node] != nei:
                            # Check cross-edge at same level -> odd len cycle
                            if level[node] == level[nei]:
                                return True
                
            return False
                        
        
        for v in range(N):
            if visited[v] == -1:
                has_odd_len_cycle = bfs(v)
                if has_odd_len_cycle:
                    return False
        
        return True