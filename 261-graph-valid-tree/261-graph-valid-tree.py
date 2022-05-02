class Solution:
    # Time = O(N + M)
    # Space = O(N + M)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = [-1] * n
        adj_list = [[] for i in range(n)]
        parent = [-1] * n
        
        def build_graph(n, edges):
            for (src, dest) in edges:
                # Add two copies of each edge to adj_list
                adj_list[src].append(dest)
                adj_list[dest].append(src)
            return
        
        def dfs(src):
            visited[src] = 1
            # Visite the first neighbor in a deep way
            for n in adj_list[src]:
                if visited[n] == -1:
                    parent[n] = src
                    has_cycle = dfs(n)
                    if has_cycle:
                        return True
                elif parent[src] != n:
                    # Found back edge
                    return True
            return False
            
        
        build_graph(n, edges)
        num_components = 0
        for src in range(n):
            if visited[src] == -1:
                # Not visited
                num_components += 1
                # Checks graph is connected
                if num_components > 1:
                    return False
                has_cycle = dfs(src)
                # Checks graph is acyclic
                if has_cycle:
                    return False
        
        return True
            