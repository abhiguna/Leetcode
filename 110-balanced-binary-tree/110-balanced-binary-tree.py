# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(H), H: height of the call stack
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Edge case: empty tree
        if not root:
            return True
        
        is_balanced = [True]
        
        def helper(node):
            # Base case: leaf node
            if not node.left and not node.right:
                return 0
            
            l_height, r_height = 0, 0
            if node.left:
                l_height = 1 + helper(node.left)
            if node.right:
                r_height = 1 + helper(node.right)
            
            if abs(l_height - r_height) > 1:
                is_balanced[0] = False
            
            return max(l_height, r_height)
        
        helper(root)
        return is_balanced[0]