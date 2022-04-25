# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(NlogN)
    # Space = O(N)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        in_list = []
        
        def inorder(node):
            nonlocal in_list
            
            # Base case ~ leaf node:
            if not node.left and not node.right:
                in_list.append(node.val)
                return
            
            # Recursive case ~ internal node
            if node.left:
                inorder(node.left)
            
            in_list.append(node.val)
            
            if node.right:
                inorder(node.right)
            
            return
        
        inorder(root)
        
        sorted_list = sorted(in_list)
        
        # Check duplicates
        for i in range(1, len(sorted_list)):
            if sorted_list[i] == sorted_list[i-1]:
                return False
            
        return in_list == sorted_list