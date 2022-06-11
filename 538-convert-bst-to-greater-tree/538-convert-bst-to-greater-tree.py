# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(h), h: height of the tree
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Edge case: empty tree
        if not root :
            return None
        
        prev_val = [0]
        
        def dfs(node):
            # Base case: leaf node
            if not root.left and not root.right:
                node.val = node.val + prev_val[0]
                prev_val[0] = node.val 
                return
            
            # General case: R-N-L
            if node.right:
                dfs(node.right)
            
            node.val = node.val + prev_val[0]
            prev_val[0] = node.val
            
            if node.left:
                dfs(node.left)
            
            return
            
        dfs(root)
        return root
        