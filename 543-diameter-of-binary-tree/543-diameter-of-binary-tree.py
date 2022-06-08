# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(H), H: height of the tree
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        
        def dfs(node):
            # Base case: leaf node
            if not node.left and not node.right:
                return 0
            
            left_height, right_height = 0, 0
            
            if node.left:
                left_height = 1 + dfs(node.left)
            if node.right:
                right_height = 1 + dfs(node.right)
            
            longest_path_len = left_height + right_height
            diameter[0] = max(diameter[0], longest_path_len)
            
            # Return the height of the current node to the parent
            return max(left_height, right_height)
            
            
        
        dfs(root)
        return diameter[0]