# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Time = O(N), N: # of node in the tree
    # Space = O(N)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        LCA = [None]
        
        def helper(root):
            p_found = (root.val == p.val)
            q_found = (root.val == q.val)
            
            # Base case: leaf node
            if not root.left and not root.right:
                return (p_found, q_found)
            
            # Recursive case: internal_node
            (p_found_left, q_found_left) = (False, False)
            (p_found_right, q_found_right) = (False, False)
            
            if root.left:
                (p_found_left, q_found_left) = helper(root.left)
            
            if root.right:
                (p_found_right, q_found_right) = helper(root.right)
            
            p_found = p_found or p_found_left or p_found_right
            q_found = q_found or q_found_left or q_found_right
            
            if (p_found, q_found) == (True, True) and LCA[0] == None:
                LCA[0] = root
                
            return (p_found, q_found)
            
            
        helper(root)
        return LCA[0]