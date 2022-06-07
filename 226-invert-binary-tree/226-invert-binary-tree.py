# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(H), H: height of the tree
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Edge case: empty tree
        if not root:
            return None
        
        def helper(root):
            # Base case: leaf node
            if not root.left and not root.right:
                return
            
            old_left, old_right = root.left, root.right
            root.left = old_right
            root.right = old_left
            
            if root.left:
                helper(root.left)
            
            if root.right:
                helper(root.right)
            
            return
            
        helper(root)
        return root