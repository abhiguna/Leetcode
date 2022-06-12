# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(n), n: # of nodes in the tree
    # Space = O(h), h: height of the tree
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Edge case: empty tree
        if not root:
            return []
        
        res = []
        
        def dfs(node, rem_sum, slate):
            slate.append(node.val)
            # Base case: leaf node
            if not node.left and not node.right:
                if node.val == rem_sum:
                    res.append(slate[:])
            # General case
            else:
                if node.left:
                    dfs(node.left, rem_sum - node.val, slate)
                
                if node.right:
                    dfs(node.right, rem_sum - node.val, slate)
            slate.pop()
        
        dfs(root, targetSum, [])
        return res