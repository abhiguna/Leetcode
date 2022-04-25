# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N)
    # Space = O(logN)
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(start_idx, end_idx):
            # Base cases
            if start_idx > end_idx:
                return None
            
            if start_idx == end_idx:
                return TreeNode(nums[start_idx])
            
            # Recursive case
            mid = start_idx + (end_idx - start_idx) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(start_idx, mid - 1)
            root.right = dfs(mid + 1, end_idx)
            return root
        
        bst = dfs(0, len(nums) - 1)
        return bst