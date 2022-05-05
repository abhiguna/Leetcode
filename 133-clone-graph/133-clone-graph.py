"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import *

# Time = O(M + N)
# Space = O(M + N)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Empty graph
        if not node:
            return None
        
        old_to_new = defaultdict(Node)
        
        def dfs(node):
            # Base case
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        
        return dfs(node)