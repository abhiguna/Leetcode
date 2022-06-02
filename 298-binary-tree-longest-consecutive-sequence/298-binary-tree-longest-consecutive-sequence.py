# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # Edge case: empty tree
        if not root:
            return 0
        
        max_len = [0]
        
        def dfs(node, prev_val, curr_len):
            # Base case: leaf node
            if not node.left and not node.right:
                if node.val == prev_val + 1:
                    curr_len += 1
                else:
                    curr_len = 1
                max_len[0] = max(max_len[0], curr_len)
                return
            
            # Recursive case: internal node
            if node.val == prev_val + 1:
                curr_len += 1
            else:
                curr_len = 1
            max_len[0] = max(max_len[0], curr_len)
            
            if node.left:
                dfs(node.left, node.val, curr_len)
            
            if node.right:
                dfs(node.right, node.val, curr_len)
            
            return
            
        
        
        dfs(root, root.val-1, 0)
        return max_len[0]