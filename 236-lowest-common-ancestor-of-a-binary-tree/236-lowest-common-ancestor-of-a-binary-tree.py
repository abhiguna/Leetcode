# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Time = O(N)
    # Space = O(N)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        LCA = None
        
        def dfs(node):
            nonlocal LCA
            
            p_found = False
            q_found = False
            
            if node.val == p.val:
                p_found = True
            
            if node.val == q.val:
                q_found = True
            
            # Base Case: leaf node
            if not node.left and not node.right:
                return (p_found, q_found)
            
            # Recursive case: internal node
            if node.left:
                (p_found_left, q_found_left) = dfs(node.left)
                p_found = p_found or p_found_left
                q_found = q_found or q_found_left
            
            if node.right:
                (p_found_right, q_found_right) = dfs(node.right)
                p_found = p_found or p_found_right
                q_found = q_found or q_found_right
            
            if not LCA and p_found and q_found:
                LCA = node
            
            return (p_found, q_found)
    
        dfs(root)
        return LCA