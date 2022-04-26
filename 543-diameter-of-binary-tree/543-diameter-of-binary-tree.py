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
            
            # Base case
            if not node.left and not node.right:
                return 0
            
            # Recursive case
            left_height = 0
            right_height = 0
            longest_path = 0
            
            if node.left:
                left_height = 1 + dfs(node.left)
            
            if node.right:
                right_height = 1 + dfs(node.right)
            
            longest_path = left_height + right_height
            diameter = max(diameter, longest_path)
            
            return max(left_height, right_height)
        
        dfs(root)
        return diameter