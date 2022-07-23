class Solution:
    # Time = O(m+n), m: len(dislikes), n: # of people
    # Space = O(m+n)
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        group_map = {
            "A": "B",
            "B": "A"
        }
        adj_list = [[] for v in range(n+1)]
        visited = [-1] * (n+1)
        parent = [-1] * (n+1)
        group = [-1] * (n+1)
        
        def build_graph():
            for (src, dest) in dislikes:
                adj_list[src].append(dest)
                adj_list[dest].append(src)
            
        build_graph()
        
        # DFS -> check group separation in a component
        def dfs(node, g):
            visited[node] = 1
            group[node] = g
            
            for nei in adj_list[node]:
                if visited[nei] == -1:
                    can_split = dfs(nei, group_map[g])
                    if not can_split:
                        return False
                else:
                    # Back edge
                    if nei != parent[node]:
                        if group[nei] == group[node]:
                            return False
            
            return True
        
        # Outer Loop -> check all components
        for v in range(n):
            if visited[v] == -1:
                can_split = dfs(v, "A")
                if not can_split:
                    return False
        
        return True