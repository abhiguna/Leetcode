# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Time = O(N)
    # Space = O(N)
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node):
            # Base case: leaf node
            if not node.left and not node.right:
                return (1, True)
            
            # Recursive case: internal node
            is_curr_unival = True
            num_unival = 0
            
            if node.left:
                (num_left_unival, is_left_unival) = dfs(node.left)
                
                if not is_left_unival or node.val != node.left.val:
                    is_curr_unival = False
                num_unival += num_left_unival
            
            if node.right:
                (num_right_unival, is_right_unival) = dfs(node.right)
                
                if not is_right_unival or node.val != node.right.val:
                    is_curr_unival = False
                
                num_unival += num_right_unival
            
            if is_curr_unival:
                num_unival += 1
            
            return (num_unival, is_curr_unival)
        
        (total_unival, is_root_unival) = dfs(root)
        return total_unival