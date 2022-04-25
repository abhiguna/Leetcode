# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    
    # Time = O(N)
    # Space = O(H), H: height of the tree, ~ O(logN) for balanced tree, O(N) for unbalanced tree
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def dfs(node, max_val):
            nonlocal count
            
            # Base case ~ leaf node
            if not node.left and not node.right:
                if node.val >= max_val:
                    count += 1
                return
            
            # Recursive case ~ internal node
            if node.val >= max_val:
                count += 1
            
            if node.left:
                dfs(node.left, max(max_val, node.val))
            
            if node.right:
                dfs(node.right, max(max_val, node.val))
            
            return
        
        dfs(root, root.val)
        return count
            
        