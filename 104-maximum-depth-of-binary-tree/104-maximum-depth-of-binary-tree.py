# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(H), H: height of the tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Edge case
        if not root:
            return 0
        
        queue = deque()
        queue.append(root)
        max_depth = 0
        
        while queue:
            num_nodes = len(queue)
            
            for i in range(num_nodes):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            max_depth += 1
        
        return max_depth
        