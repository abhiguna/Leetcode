# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Time = O(N)
    # Space = O(N)
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # Bottom-up DFS
        # return [p_with_root, p_without_root]
        def dfs(node):
            # Base case: leaf node
            if not node.left and not node.right:
                return [node.val, 0]
            
            # Recursive case: internal node
            left_profit = [0, 0]
            right_profit = [0, 0]
            
            if node.left:
                left_profit = dfs(node.left)
            
            if node.right:
                right_profit = dfs(node.right)
            
            p_with_root = node.val + left_profit[1] + right_profit[1]
            p_without_root = max(left_profit) + max(right_profit)
            
            return [p_with_root, p_without_root]
        
        return max(dfs(root))
            