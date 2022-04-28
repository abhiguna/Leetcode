# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N)
    # Space = O(N)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        
        def dfs(node, slate, target):
            nonlocal res
            slate.append(node.val)
            target -= node.val
            
            # Base case: leaf node
            if not node.left and not node.right:
                if target == 0:
                    res.append(slate[:])
            
            # Recursive case: internal node
            if node.left:
                dfs(node.left, slate, target)
            
            if node.right:
                dfs(node.right, slate, target)
                
            slate.pop()
            return
        
        dfs(root, [], targetSum)
        return res
            