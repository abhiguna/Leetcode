# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Time = O(N)
    # Space = O(N)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(node, curr_sum):
            # Base case: leaf node
            if not node.left and not node.right:
                curr_sum += node.val
                if curr_sum == targetSum:
                    return True
                return False
            
            in_left_subtree = False
            in_right_subtree = False
            
            if node.left:
                in_left_subtree = dfs(node.left, curr_sum + node.val)
            
            if node.right:
                in_right_subtree = dfs(node.right, curr_sum + node.val)
            
            return in_left_subtree or in_right_subtree
    
        return dfs(root, 0)
            