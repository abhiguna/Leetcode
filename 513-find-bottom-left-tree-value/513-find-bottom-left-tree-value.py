# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # nodes in the tree
    # Space = O(N)
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Top-down DFS
        leftmost_val = [root.val]
        max_depth = [0]
        
        def dfs(node, depth):
            # Base case: leaf node
            if not node.left and not node.right:
                if depth > max_depth[0]:
                    leftmost_val[0] = node.val 
                    max_depth[0] = max(max_depth[0], depth)
                return
            
            # Recursive case: internal node
            if node.left:
                dfs(node.left, 1 + depth)
            
            if node.right:
                dfs(node.right, 1 + depth)
            
            return
            
            
        
        dfs(root, 0)
        return leftmost_val[0]
        
        
        