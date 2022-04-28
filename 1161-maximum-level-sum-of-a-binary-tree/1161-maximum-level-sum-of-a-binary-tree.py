# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import math

class Solution:
    
    # Time = O(N)
    # Space = O(N)
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -math.inf
        min_level = 0
        
        curr_level = 0
        queue = deque([root])
        
        while queue:
            num_nodes = len(queue)
            level_sum = 0
            
            curr_level += 1
            
            for _ in range(num_nodes):
                curr_node = queue.popleft()
                level_sum += curr_node.val
                
                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                min_level = curr_level
        
        return min_level