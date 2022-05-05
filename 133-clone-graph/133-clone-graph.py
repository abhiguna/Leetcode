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
        
        def bfs(node):
            queue = deque([node])
            src_cpy = Node(node.val)
            old_to_new[node] = src_cpy
            
            while queue:
                curr = queue.popleft()
                curr_cpy = old_to_new[curr]
                
                for nei in curr.neighbors:
                    if nei in old_to_new:
                        curr_cpy.neighbors.append(old_to_new[nei])
                    else:
                        nei_cpy = Node(nei.val)
                        curr_cpy.neighbors.append(nei_cpy)
                        old_to_new[nei] = nei_cpy
                        queue.append(nei)
            
            return src_cpy
        
        
        return bfs(node)