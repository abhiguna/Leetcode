# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        curr_node = root
        while curr_node or stack:
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            visited = stack.pop()
            res.append(visited.val)
            curr_node = visited.right 
        return res
        
            