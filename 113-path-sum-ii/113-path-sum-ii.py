# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Edge case: empty tree
        if not root:
            return []
        
        res = []
        
        def dfs(node, slate, path_sum):
            # Base case: leaf node
            if not node.left and not node.right:
                path_sum += node.val
                slate.append(node.val)
                if path_sum == targetSum:
                    res.append(slate[:])
                path_sum -= node.val
                slate.pop()
                return
            
            # Internal node: internal node
            path_sum += node.val
            slate.append(node.val)
            
            if node.left:
                dfs(node.left, slate, path_sum)
            if node.right:
                dfs(node.right, slate, path_sum)
            
            path_sum -= node.val
            slate.pop()
        
        dfs(root, [], 0)
        return res