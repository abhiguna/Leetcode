# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(h), h: height of the tree
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth_smallest = [-1]
        num_nodes = [0]
        
        def dfs(node):
            # Base case:
            if not node.left and not node.right:
                num_nodes[0] += 1
                if num_nodes[0] == k:
                    kth_smallest[0] = node.val
                return
            
            # General case: inorder traversal L-N-R
            if node.left:
                dfs(node.left)
            
            num_nodes[0] += 1
            if num_nodes[0] == k:
                kth_smallest[0] = node.val 
            
            if node.right:
                dfs(node.right)
            
            
        dfs(root)
        return kth_smallest[0]