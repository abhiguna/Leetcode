"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Edge case: empty tree
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            num_nodes = len(queue)
            
            for i in range(num_nodes):
                node = queue.popleft()
                
                # Check if node is not the last node
                if i < num_nodes - 1:
                    node.next = queue[0]
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        
        return root
        