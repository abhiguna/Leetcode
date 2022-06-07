# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import *

class Solution:
    # Time = O(N), N: # of node in the tree
    # Space = O(N)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case:
        if not root:
            return []
        
        res = []
        queue = deque()
        queue.append(root)
        
        while queue:
            num_nodes = len(queue)
            curr_level = []
            
            for i in range(num_nodes):
                node = queue.popleft()
                curr_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            res.append(curr_level)
        
        return res