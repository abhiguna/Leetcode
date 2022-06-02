class Solution:
    # Time = O(M + N), M: # of edges in the graph, N: # of vertices in the graph
    # Space = O(M + N)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for i in range(n)]
        visited = [-1] * n
        parent = [-1] * n
        
        # Build graph
        def build_graph():
            for (src, dest) in edges:
                adj_list[src].append(dest)
                adj_list[dest].append(src)
            return
        
        build_graph()
        
        # BFS for all unvisited nodes
        def bfs(src):
            queue = deque()
            queue.append(src)
            visited[src] = 1
            
            while queue:
                node = queue.popleft()
                
                for nei in adj_list[node]:
                    if visited[nei] == -1:
                        visited[nei] = 1
                        parent[nei] = node
                        queue.append(nei)
                    elif parent[node] != nei:
                        return True
            
            return False
        
        components = 0
        for i in range(n):
            if visited[i] == -1:
                components += 1
                if components > 1:
                    return False
                
                has_cycle = bfs(i)
                if has_cycle:
                    return False
        
        # Check validity
        return True