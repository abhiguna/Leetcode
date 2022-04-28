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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        queue = deque([(root, 1)])
        
        while queue:
            num_nodes = len(queue)
            start_idx = None
            end_idx = None
            
            for _ in range(num_nodes):
                node, idx = queue.popleft()
                
                if not start_idx:
                    start_idx = idx
                
                end_idx = idx
                
                
                if node.left:
                    queue.append((node.left, 2*idx))
                
                if node.right:
                    queue.append((node.right, 2*idx + 1))
            
            if end_idx and start_idx:
                max_width = max(max_width, end_idx - start_idx + 1)
        
        return max_width