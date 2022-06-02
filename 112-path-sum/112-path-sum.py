# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Edge case: empty tree
        if not root:
            return False
        
        found_sum = [False]
        
        def dfs(node, path_sum):
            # Base case: leaf node
            if not node.left and not node.right:
                path_sum += node.val 
                if path_sum == targetSum:
                    found_sum[0] = True
                path_sum -= node.val
                return
            
            # Recursive case: internal node
            path_sum += node.val
            if node.left:
                dfs(node.left, path_sum)
            if node.right:
                dfs(node.right, path_sum)
            path_sum -= node.val 
            return
            
        
        dfs(root, 0)
        return found_sum[0]
            