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
        idx_map = defaultdict(int)
        
        for idx, val in enumerate(inorder):
            idx_map[val] = idx
        
        preorder_idx = 0
        
        def dfs(start, end):
            nonlocal preorder_idx 
            
            # Base case
            if start > end:
                return None
            
            root = TreeNode(preorder[preorder_idx])
            preorder_idx += 1
            
            root.left = dfs(start, idx_map[root.val] - 1)
            root.right = dfs(idx_map[root.val] + 1, end)
            return root
        
        return dfs(0, len(preorder) - 1)