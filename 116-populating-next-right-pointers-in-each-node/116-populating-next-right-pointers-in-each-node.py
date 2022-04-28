"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import *

class Solution:
    
    # Time = O(N)
    # Space = O(N)
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Edge case
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            num_nodes = len(queue)
            
            for i in range(num_nodes):
                curr_node = queue.popleft()
                
                if i != num_nodes - 1:
                    curr_node.next = queue[0]
                
                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)
        
        return root
        