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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # Edge case
        if depth == 1:
            old_root = root
            new_root = TreeNode(val)
            new_root.left = old_root
            return new_root
        
        queue = deque([root])
        curr_depth = 0
        
        while queue:
            num_nodes = len(queue)
            curr_depth += 1
            
            for _ in range(num_nodes):
                curr_node = queue.popleft()

                if curr_depth == depth - 1:
                    old_left = curr_node.left
                    old_right = curr_node.right

                    curr_node.left = TreeNode(val)
                    curr_node.left.left = old_left
                    curr_node.right = TreeNode(val)
                    curr_node.right.right = old_right
                
                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)
        
        return root
            
            
        