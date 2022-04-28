# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    # Time = O(N)
    # Space = O(N)
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        max_len = 0
        
        def dfs(node, prev_val, curr_len):
            nonlocal max_len
            
            if node.val == prev_val + 1:
                curr_len += 1
            else:
                curr_len = 1
            
            max_len = max(max_len, curr_len)
            
            if node.left:
                dfs(node.left, node.val, curr_len)
            
            if node.right:
                dfs(node.right, node.val, curr_len)
                
            max_len = max(max_len, curr_len)
            return
        
        
        dfs(root, root.val, 0)
        return max_len