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
        depth_x = None
        
        parent_y = None
        depth_y = None
        
        curr_depth = -1
        queue = deque([(root, None)])
        
        while queue:
            num_nodes = len(queue)
            curr_depth += 1
            
            for _ in range(num_nodes):
                curr_node, parent = queue.popleft()
                
                if curr_node.val == x:
                    parent_x = parent
                    depth_x = curr_depth
                elif curr_node.val == y:
                    parent_y = parent
                    depth_y = curr_depth
                
                if curr_node.left:
                    queue.append((curr_node.left, curr_node))
                
                if curr_node.right:
                    queue.append((curr_node.right, curr_node))
            
        if (depth_x == depth_y) and (parent_x != parent_y):
            return True
        
        return False