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
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parent_x = None
        parent_y = None
        
        curr_depth = -1
        queue = deque([root])
        
        while queue:
            num_nodes = len(queue)
            curr_depth += 1
            
            for _ in range(num_nodes):
                curr_node = queue.popleft()
                
                if curr_node.left:
                    queue.append(curr_node.left)
                    if curr_node.left.val == x:
                        parent_x = curr_node.val
                    elif curr_node.left.val == y:
                        parent_y = curr_node.val
                
                if curr_node.right:
                    queue.append(curr_node.right)
                    if curr_node.right.val == x:
                        parent_x = curr_node.val
                    elif curr_node.right.val == y:
                        parent_y = curr_node.val
                
                # If either parent is found in the curr level check bool condition
            if parent_x or parent_y:
                return (parent_x and parent_y) and (parent_x != parent_y)
        
        return False