class Solution:
    # Time = O(M+N)
    # Space = O(M+N)
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = [[] for i in range(n+1)]
        visited = [-1] * (n+1)
        parent = [-1] * (n+1)
        level = [-1] * (n+1)
        
        def build_graph():
            for (src, dest) in dislikes:
                adj_list[src].append(dest)
                adj_list[dest].append(src)
            return
        
        def bfs(src):
            queue = deque()
            queue.append(src)
            visited[src] = 1
            level[src] = 0
            
            while queue:
                node = queue.popleft()
                
                for nei in adj_list[node]:
                    if visited[nei] == -1:
                        visited[nei] = 1
                        parent[nei] = node
                        level[nei] = 1 + level[node]
                        queue.append(nei)
                    else:
                        # Cross edge
                        if parent[node] != nei:
                            # Has odd len cycle
                            if level[node] == level[nei]:
                                return True
            
            return False
            
        
        build_graph()
        
        for v in range(1, n+1):
            if visited[v] == -1:
                has_odd_len_cycle = bfs(v)
                if has_odd_len_cycle:
                    return False
        
        return True
        
        