class Solution:
    # Time = O(n*P), n: # of nodes in the graph, P: the number of paths from s to d (exp.)
    # Space = O(n), the longest path could have n nodes in it
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # The src = node 0, dest = node n-1
        res = []
        n = len(graph)
        
        def helper(node, slate):
            # Base case: leaf node
            if node == n-1:
                slate.append(node)
                res.append(slate[:])
                slate.pop()
                return
            # General case: internal node
            slate.append(node)
            for nei in graph[node]:
                helper(nei, slate)
            slate.pop()
            return
            
        helper(0, [])
        return res