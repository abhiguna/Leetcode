# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    # Time = O(N)
    # Space = O(H), H: height of the tree ~ O(logN) for balanced tree, ~O(N) for unbalanced tree
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Edge case: empty tree
        if not root:
            return True
        
        is_balanced = True
        
        def find_height(node):
            nonlocal is_balanced
            
            # Base cases ~ leaf node/empty tree
            if not node.left and not node.right:
                return 0
            
            # Recursive case ~ Internal node
            left_height = 0
            if node.left:
                left_height = 1 + find_height(node.left)
            
            right_height = 0
            if node.right:
                right_height = 1 + find_height(node.right)
            
            if abs(left_height - right_height) > 1:
                is_balanced = False
                
            return max(left_height, right_height)
        
        find_height(root)
        return is_balanced