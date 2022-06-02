# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Edge case: empty tree
        if not root:
            return None
        
        def dfs(node):
            # Base case: leaf node
            if not node.left and not node.right:
                return
            
            prev_left = node.left 
            prev_right = node.right
            node.left = prev_right
            node.right = prev_left
            
            if node.left:
                dfs(node.left)
            
            if node.right:
                dfs(node.right)
            
            return
            
        dfs(root)
        return root