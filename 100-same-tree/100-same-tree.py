# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Time = O(min(M, N)), M: # of nodes in p, N: # of nodes in q
    # Space = O(min(Hp, Hq)), Hp: height of p, Hq: height of q
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base cases:
        if not p and not q:
            return True
        
        if (p and not q) or (not p and q) or (p.val != q.val):
            return False
        
        is_left_valid = self.isSameTree(p.left, q.left)
        if not is_left_valid:
            return False
        
        is_right_valid = self.isSameTree(p.right, q.right)
        if not is_right_valid:
            return False
        
        return p.val == q.val and is_left_valid and is_right_valid

    