class Solution:
    # Time = O(M+N), M: # of edges, N: # of nodes
    # Space = O(M+N)
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Goal: find the 2 centroid nodes that have the most neighbors
        
        # Edge case: 
        if n <= 2:
            return [v for v in range(n)]
        
        # Build the graph
        adj_list = [set() for i in range(n)]
        for (src, dest) in edges:
            adj_list[src].add(dest)
            adj_list[dest].add(src)
        
        # Find the first leaves -> leaf has only one connecting edge
        leaves = deque()
        for v in range(n):
            if len(adj_list[v]) == 1:
                leaves.append(v)
        
        # Keep removing the leaves until left with at most 2 elements
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            
            new_leaves = deque()
            while leaves:
                node = leaves.popleft()
                nei = adj_list[node].pop()
                adj_list[nei].remove(node)
                
                # Found a new leaf
                if len(adj_list[nei]) == 1:
                    new_leaves.append(nei)
            
            leaves = new_leaves
        
        return list(leaves)