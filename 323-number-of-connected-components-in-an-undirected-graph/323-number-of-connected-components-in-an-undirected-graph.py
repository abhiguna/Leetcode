class Solution:
    # Time = O(M+N)
    # Space = O(M+N)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for i in range(n)]
        
        def build_graph():
            for (u,v) in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)
            return
            
        def dfs(src):
            visited[src] = 1
            
            for nei in adj_list[src]:
                if visited[nei] == -1:
                    dfs(nei)
            return
        
        build_graph()
        visited = [-1] * n
        components = 0
        for i in range(n):
            if visited[i] == -1:
                components += 1
                dfs(i)
        return components
        