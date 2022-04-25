# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N)
    # Space = O(H), H: height of the tree ~ O(logN) for balanced tree / O(N) for unbalanced tree
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Edge case
        if not root:
            return root
        
        def dfs(node):
            # Base case ~ leaf node
            if not node.left and not node.right:
                return
            
            # Recursive case ~ internal node
            if node.left:
                dfs(node.left)
            
            if node.right:
                dfs(node.right)
            
            # Swap
            temp = node.right
            node.right = node.left
            node.left = temp
            return
        
        dfs(root)
        return root
                