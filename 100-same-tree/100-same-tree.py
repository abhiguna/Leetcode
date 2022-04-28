# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    
    # Time = O(N)
    # Space = O(N)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and not q:
            return False
        elif not p and q:
            return False
        
        queue = deque([(p, q)])
        
        while queue:
            num_nodes = len(queue)
            
            for _ in range(num_nodes):
                node_p, node_q = queue.popleft()
                
                if node_p.val != node_q.val:
                    return False
                
                # Both have left child
                if node_p.left and node_q.left:
                    queue.append((node_p.left, node_q.left))
                # One has left child while one doesn;t
                elif node_p.left or node_q.left:
                    return False
                
                if node_p.right and node_q.right:
                    queue.append((node_p.right, node_q.right))
                elif node_p.right or node_q.right:
                    return False
        
        return True
                
                
                
                
            