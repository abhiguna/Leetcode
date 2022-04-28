"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    # Time = O(N)
    # Space = O(W) ~ O(N) in worst case
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            num_nodes = len(queue)
            curr_level = []
            
            for _ in range(num_nodes):
                curr_node = queue.popleft()
                curr_level.append(curr_node.val)
                
                for child in curr_node.children:
                    queue.append(child)
            
            res.append(curr_level)
        
        return res