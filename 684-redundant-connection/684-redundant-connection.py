class Solution:
    # Time = O(N)
    # Space = O(N)
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = [i for i in range(N+1)]
        size = [i for i in range(N+1)]
        redundant = [None]
        
        def find(node):
            # Base case: root node
            if parent[node] == node:
                return node
            
            # Recursive case: internal node
            root = find(parent[node])
            parent[node] = root
            return root
            
        for (u,v) in edges:
            root_u = find(u)
            root_v = find(v)
            
            # Check for redundancy ~ a cycle
            if root_u == root_v:
                redundant[0] = [u,v]
            else:
                if size[root_u] < size[root_v]:
                    parent[root_u] = root_v
                    size[root_v] += size[root_u]
                else:
                    parent[root_v] = root_u
                    size[root_u] += size[root_v]
        
        return redundant[0]
            
        