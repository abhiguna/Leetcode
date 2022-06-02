# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N^2), N: # of nodes in the tree
    # Space = O(N)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Edge case: empty tree
        if not root:
            return 0
        
        total_paths = [0]
        
        def dfs(node, slate):
            # Compute all suffix sums ending at the current node
            slate.append(node.val)
            suffix_sum = 0
            for i in range(len(slate)-1, -1, -1):
                suffix_sum += slate[i]
                if suffix_sum == targetSum:
                    total_paths[0] += 1
            
            # Base case: leaf node
            if not node.left and not node.right:
                slate.pop()
                return
            
            if node.left:
                dfs(node.left, slate)
            
            if node.right:
                dfs(node.right, slate)
            
            slate.pop()
            
                
        dfs(root, [])
        return total_paths[0]
        
        