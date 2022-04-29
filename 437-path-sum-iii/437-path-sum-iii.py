# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N^2)
    # Space = O(N)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        total_count = 0
        
        def dfs(node, slate):
            nonlocal total_count
            slate.append(node.val)
            
            # Compute suffix sum and increment total_count
            suffix_sum = 0
            for i in range(len(slate) - 1, -1, -1):
                suffix_sum += slate[i]
                if suffix_sum == targetSum:
                    total_count += 1
            
            # Recursive case
            if node.left:
                dfs(node.left, slate)
            
            if node.right:
                dfs(node.right, slate)
            
            slate.pop()
        
        dfs(root, [])
        return total_count