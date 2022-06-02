# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Edge case: empty tree
        if not root:
            return None
        
        LCA = [None]
        
        def dfs(node):
            p_found, q_found = False, False
            
            if node.val == p.val:
                p_found = True
            
            if node.val == q.val:
                q_found = True
            
            # Base case: leaf node
            if not node.left and not node.right:
                return (p_found, q_found)
            
            # Recursive case: internal node
            if node.left:
                (p_in_left, q_in_left) = dfs(node.left)
                p_found = p_found or p_in_left
                q_found = q_found or q_in_left
            
            if node.right:
                (p_in_right, q_in_right) = dfs(node.right)
                p_found = p_found or p_in_right
                q_found = q_found or q_in_right
            
            if p_found and q_found and LCA[0] == None:
                LCA[0] = node
            
            return (p_found, q_found)
        
        (p_found, q_found) = dfs(root)
        return LCA[0]