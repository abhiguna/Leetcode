# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N)
    # Space = O(N)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Provides constant lookup
        inorder_map = {}
        for (idx, val) in enumerate(inorder):
            inorder_map[val] = idx
        
        preorder_idx = [0]
        
        def dfs(start, end):
            # Base case: empty or singleton array
            if start > end:
                return None

            # Recursive case: internal node
            rval = preorder[preorder_idx[0]]
            preorder_idx[0] += 1
            node = TreeNode(rval)
            
            root_idx = inorder_map[rval]
            
            node.left = dfs(start, root_idx-1)
            node.right = dfs(root_idx+1, end)
            return node
            
        root = dfs(0, len(preorder) - 1)
        return root