# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N)
    # Space = O(N)
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # Edge case
        if not root:
            return 0
        
        max_len = 0
        
        def dfs(node):
            nonlocal max_len
            
            # Base case: leaf node
            if not node.left and not node.right:
                return 0
            
            left_len = 0
            right_len = 0
            left_arrow = 0
            right_arrow = 0
            if node.left:
                left_len = dfs(node.left)
                if node.val == node.left.val:
                    left_arrow = 1 + left_len
            
            if node.right:
                right_len = dfs(node.right)
                if node.val == node.right.val:
                    right_arrow = 1 + right_len
            
            max_len = max(max_len, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)
        
        dfs(root)
        return max_len
            