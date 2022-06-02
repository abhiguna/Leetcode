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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # Edge case
        if not root:
            return []
        
        res = []
        queue = deque([root])
        while queue:
            num_nodes = len(queue)
            curr_level = []
            for _ in range(num_nodes):
                node = queue.popleft()
                curr_level.append(node.val)
                
                for child in node.children:
                    queue.append(child)
            
            res.append(curr_level)
        
        return res
        