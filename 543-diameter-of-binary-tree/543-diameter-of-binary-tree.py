# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Edge case: empty tree
        if not root:
            return 0
        
        max_diameter = [0]
        
        def dfs(node):
            # Base case: leaf node
            if not node.left and not node.right:
                return 0
            
            # Recursive case: internal node
            left_height, right_height = 0, 0
            
            if node.left:
                left_height = max(left_height, 1 + dfs(node.left))
            
            if node.right:
                right_height = max(right_height, 1 + dfs(node.right))
            
            diameter = left_height + right_height
            max_diameter[0] = max(max_diameter[0], diameter)
            
            return max(left_height, right_height)
            
            
        dfs(root)
        return max_diameter[0]