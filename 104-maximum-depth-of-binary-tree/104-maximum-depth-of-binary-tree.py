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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_depth = 0
        curr_depth = 0
        
        queue = deque([root])
        
        while queue:
            num_nodes = len(queue)
            
            curr_depth += 1
            
            for _ in range(num_nodes):
                curr_node = queue.popleft()
                
                # Check if leaf node
                if not curr_node.left and not curr_node.right:
                    max_depth = max(max_depth, curr_depth)
                
                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)
            
        return max_depth