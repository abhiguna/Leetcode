# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Time = O(N + M)
    # Space = O(max(H1, H2))
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def dfs(node1, node2):
            # Base cases
            if not node1 and not node2:
                return None
            elif node1 and not node2:
                return node1
            elif not node1 and node2:
                return node2
            
            # Recursive case 
            root = TreeNode(node1.val + node2.val)
            root.left = dfs(node1.left, node2.left)
            root.right = dfs(node1.right, node2.right)
            
            return root
        
        merged = dfs(root1, root2)
        return merged
                