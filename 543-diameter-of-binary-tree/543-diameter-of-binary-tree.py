# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def dfs(node):
            nonlocal diameter
            
            # Base cases
            if not node: # Cheeky ;) 
                return -1
            
            # Recursive case
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            diameter = max(diameter, left_height + right_height + 2)
            
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return diameter