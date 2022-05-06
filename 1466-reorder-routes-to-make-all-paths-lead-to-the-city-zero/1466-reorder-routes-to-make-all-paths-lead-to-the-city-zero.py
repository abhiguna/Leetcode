class Solution:
    # Time = O(M + N)
    # Space = O(M + N)
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edge_set = {(u,v) for (u,v) in connections}
        adj_list = [[] for _ in range(n)]
        
        def build_graph():
            for (u,v) in connections:
                adj_list[u].append(v)
                adj_list[v].append(u)
            return
        
        visited = set()
        num_changes = [0]
        
        def dfs(src):
            visited.add(src)
            
            for nei in adj_list[src]:
                if nei in visited:
                    continue
                if (nei, src) not in edge_set:
                    num_changes[0] += 1
                dfs(nei)
            return
                
        
        build_graph()
        dfs(0)
        return num_changes[0]
        
        