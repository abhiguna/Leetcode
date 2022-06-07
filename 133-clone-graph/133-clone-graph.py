"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # Time = O(M+N)
    # Space = O(N)
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Edge case
        if not node:
            return None
        
        old_to_new = {}
        
        def dfs(src):
            if src in old_to_new:
                return old_to_new[src]
            else:
                old_to_new[src] = Node(src.val)
                for nei in src.neighbors:
                    nei_cpy = dfs(nei)
                    old_to_new[src].neighbors.append(nei_cpy)
                return old_to_new[src]
                
        dfs(node)
        return old_to_new[node]