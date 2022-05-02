class Solution:
    # Time = O(M + N)
    # Space = O(N)
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        dist = [-1] * N
        
        def bfs(src):
            queue = deque([src])
            dist[src] = 0
            
            while queue:
                curr = queue.popleft()
                
                for neighbor in graph[curr]:
                    if dist[neighbor] == -1:
                        dist[neighbor] = dist[curr] + 1
                        queue.append(neighbor)
                    elif dist[curr] == dist[neighbor]:
                        # Cross edge && odd length cycle
                        return False
            return True
        
        for src in range(N):
            if dist[src] == -1:
                is_bipartite = bfs(src)
                if not is_bipartite:
                    return False
        
        return True
                    