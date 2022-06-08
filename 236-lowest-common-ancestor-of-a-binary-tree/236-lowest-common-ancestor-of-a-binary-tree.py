# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(H), H: height of the tree
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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
            
            # Recursive case: internal_node
            p_found_left, q_found_left = False, False
            p_found_right, q_found_right = False, False
            
            if node.left:
                (p_found_left, q_found_left) = dfs(node.left)
            
            if node.right:
                (p_found_right, q_found_right) = dfs(node.right)
            
            p_found = p_found or p_found_left or p_found_right
            q_found = q_found or q_found_left or q_found_right
            
            if (p_found, q_found) == (True, True) and LCA[0] == None:
                LCA[0] = node
            
            return (p_found, q_found)
             
        dfs(root)
        return LCA[0]