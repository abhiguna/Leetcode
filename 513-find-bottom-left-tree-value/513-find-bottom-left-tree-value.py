# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        # BFS
        queue = deque([root])
        leftmost_val = root.val
        
        while queue:
            num_nodes = len(queue)
            
            for i in range(num_nodes):
                node = queue.popleft()
                
                if i == 0:
                    leftmost_val = node.val 
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
        return leftmost_val