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
        
        res = [False]
        def dfs(node, target):
            nonlocal res
            target -= node.val
            
            # Base case: leaf node
            if not node.left and not node.right:
                if target == 0:
                    res[0] = True
            
            if node.left:
                dfs(node.left, target)
            
            if node.right:
                dfs(node.right, target)
            
            return
    
        dfs(root, targetSum)
        return res[0]
            