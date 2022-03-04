# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    # Inorder: L-N-R
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack = deque()
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
                continue
            
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result