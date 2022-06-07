# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(H), H: height of the tree
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        is_bst = [True]
        
        def dfs(node, lower, upper):
            # Preorder: N-L-R
            condition = lower < node.val < upper
            if not condition:
                is_bst[0] = False
            
            # Base case: leaf node
            if not node.left and not node.right:
                return
            
            if node.left:
                dfs(node.left, lower, node.val)
            if node.right:
                dfs(node.right, node.val, upper)
            return
        
        dfs(root, -math.inf, math.inf)
        return is_bst[0]