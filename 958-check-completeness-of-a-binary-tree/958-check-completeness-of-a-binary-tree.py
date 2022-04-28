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
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # Edge case
        if not root.left and not root.right:
            return True
        
        queue = deque([(root, 1)])
        prev_idx = None
        
        while queue:
            num_nodes = len(queue)
            
            for _ in range(num_nodes):
                curr_node, curr_idx = queue.popleft()
                
                if prev_idx and curr_idx > prev_idx + 1:
                    return False
                
                prev_idx = curr_idx
                
                if curr_node.left:
                    queue.append((curr_node.left, 2*curr_idx))
                
                if curr_node.right:
                    queue.append((curr_node.right, 2*curr_idx + 1))
        
        return True
        