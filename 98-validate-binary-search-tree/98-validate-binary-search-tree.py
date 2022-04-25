# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, lower_bound, upper_bound):
            # Base case
            if not node:
                return True
            
            # Recursive case 
            if node.val <= lower_bound or node.val >= upper_bound:
                return False
            
            is_left_valid = True
            is_right_valid = True
            
            if node.left:
                is_left_valid = dfs(node.left, lower_bound, node.val)
            
            if node.right:
                is_right_valid = dfs(node.right, node.val, upper_bound)
            
            return is_left_valid and is_right_valid
        
        return dfs(root, -math.inf, math.inf)