# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def myInTraversal(node, res):
            if not node:
                return
            myInTraversal(node.left, res)
            res.append(node.val)
            myInTraversal(node.right, res)
        
        myInTraversal(root, res)
        return res
            