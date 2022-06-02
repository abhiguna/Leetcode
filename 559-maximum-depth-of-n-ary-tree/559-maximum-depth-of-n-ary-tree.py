"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def maxDepth(self, root: 'Node') -> int:
        # Edge case: empty tree
        if not root:
            return 0
        
        level_num = 0
        queue = deque([root])
        
        while queue:
            num_nodes = len(queue)
            
            for _ in range(num_nodes):
                node = queue.popleft()
                
                for child in node.children:
                    queue.append(child)
            
            level_num += 1
        
        return level_num