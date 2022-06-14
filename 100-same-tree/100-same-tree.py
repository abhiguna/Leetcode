# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Time = O(n+m)
        n: # of nodes in the tree rooted at p
        m: # of nodes in the tree rooted at q
    
    Space = O(max{h(p), h(q)})
        h(p): height of the tree rooted at p
        h(q): heights of the tree rooted at q
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base cases:
        if not p and not q:
            return True
        elif (p and not q) or (not p and q):
            return False
        elif p.val != q.val:
            return False
        
        # General case
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)
        return left_same and right_same