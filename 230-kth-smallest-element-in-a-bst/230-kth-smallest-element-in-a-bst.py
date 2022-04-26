# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N)
    # Space = O(N)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        stack = []
        curr = root
        
        while stack or curr:
            # Left subtree
            while curr:
                stack.append(curr)
                curr = curr.left 
            
            # Node
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val 
            
            curr = curr.right 
        
        return -1