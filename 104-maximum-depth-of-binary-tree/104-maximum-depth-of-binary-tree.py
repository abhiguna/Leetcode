# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(H), H: height of the tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Edge case
        if not root:
            return 0
        
        max_depth = [0]
        
        def dfs(node, depth):
            depth += 1
            
            # Base case: leaf node
            if not node.left and not node.right:
                max_depth[0] = max(max_depth[0], depth)
                return
            
            if node.left:
                dfs(node.left, depth)
            
            if node.right:
                dfs(node.right, depth)
            
            depth -= 1
            return
            
        dfs(root, 0)
        return max_depth[0]
        