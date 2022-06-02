# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # Edge case: empty tree
        if not root:
            return True
        
        value = root.val 
        queue = deque([root])
        
        while queue:
            num_nodes = len(queue)
            
            for _ in range(num_nodes):
                node = queue.popleft()
                
                if node.val != value:
                    return False
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
        return True