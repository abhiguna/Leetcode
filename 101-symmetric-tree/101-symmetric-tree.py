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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([(root, root)])
        
        while queue:
            num_nodes = len(queue)
            
            for i in range(num_nodes):
                node_l, node_r = queue.popleft()
                
                if node_l.val != node_r.val:
                    return False
                
                if node_l.left and node_r.right:
                    queue.append((node_l.left, node_r.right))
                elif node_l.left or node_r.right:
                    return False
                
                if node_l.right and node_r.left:
                    queue.append((node_l.right, node_r.left))
                elif node_l.right or node_r.left:
                    return False
        
        return True