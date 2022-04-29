# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N)
    # Space = O(N)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        def dfs(node):
            # Base case: leaf node
            if not node.left and not node.right:
                pass
            
            # Recursive case: internal node
            # Swap left and right child
            node.left, node.right = node.right, node.left
            
            if node.left:
                dfs(node.left)
            
            if node.right:
                dfs(node.right)
                
            return
        
        dfs(root)
        return root
            
            