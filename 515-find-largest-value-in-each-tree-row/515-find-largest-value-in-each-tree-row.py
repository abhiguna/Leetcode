# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import math

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            num_nodes = len(queue)
            level_max = -math.inf
            
            for _ in range(num_nodes):
                curr_node = queue.popleft() # FIFO
                level_max = max(level_max, curr_node.val)
                
                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)
                
            res.append(level_max)
        
        return res