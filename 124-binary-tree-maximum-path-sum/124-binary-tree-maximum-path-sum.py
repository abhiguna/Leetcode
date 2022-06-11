# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # nodes in the tree
    # Space = O(h), h: height of the tree
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = [-math.inf]
        
        def dfs(node):
            # Base case: leaf node
            if not node.left and not node.right:
                max_path_sum[0] = max(max_path_sum[0], node.val)
                return node.val 
            
            # General case: internal node
            left_sum, right_sum = 0, 0
            
            if node.left:
                left_sum = dfs(node.left)
            
            if node.right:
                right_sum = dfs(node.right)
            
            # Update max_path_sum
            curr_sum = node.val + max(0, left_sum, right_sum, left_sum + right_sum)
            max_path_sum[0] = max(max_path_sum[0], curr_sum)
            return node.val + max(0, left_sum, right_sum)
        
        dfs(root)
        return max_path_sum[0]