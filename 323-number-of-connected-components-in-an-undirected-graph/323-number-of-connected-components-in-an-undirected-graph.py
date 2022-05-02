class Solution:
    # Time = O(N + M), N: num of vertices, M: num of edges
    # Space = O(N + M)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [-1] * n # -1 = unvisited
        adj_list = [[] for i in range(n)]
        
        # edge list -> adj list
        def build_graph(n, edges):
            for (src, dest) in edges:
                adj_list[src].append(dest)
                # Add another copy since undirected graph
                adj_list[dest].append(src)
            return
        
        def dfs(source):
            visited[source] = 1
            
            for n in adj_list[source]:
                if visited[n] == -1:
                    dfs(n)
            return
        
        build_graph(n, edges)
        num_components = 0
        
        for src in range(n):
            if visited[src] == -1:
                # Not visited
                num_components += 1
                dfs(src)
        
        return num_components
        
        
            
        