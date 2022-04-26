# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N)
    # Space = O(N)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        
        def inorder(node):
            nonlocal res
            
            # Base case:
            if not node.left and not node.right:
                res.append(node.val)
                return
            
            # Recursive case
            if node.left:
                inorder(node.left)
            
            res.append(node.val)
            
            if node.right:
                inorder(node.right)
            
        inorder(root)
        return res[k-1]
                