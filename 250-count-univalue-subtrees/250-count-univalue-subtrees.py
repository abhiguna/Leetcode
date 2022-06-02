# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        # Edge case: empty tree
        if not root:
            return 0
        
        total_count = [0]
        
        def dfs(node):
            # Base case: leaf node
            if not node.left and not node.right:
                total_count[0] += 1
                return True
            
            # Recursive case: internal node
            unival_count = 1
            
            if node.left:
                is_univalue = dfs(node.left)
                if not is_univalue or node.val != node.left.val:
                    unival_count = 0
            
            if node.right:
                is_univalue = dfs(node.right)
                if not is_univalue or node.val != node.right.val:
                    unival_count = 0
            
            if unival_count == 0:
                return False
            
            total_count[0] += 1
            return True
                    
        is_univalue = dfs(root)
        return total_count[0]