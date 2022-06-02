# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Edge case: empty tree
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        max_width = 0
        
        while queue:
            num_nodes = len(queue)
            first = None
            last = None
            
            for _ in range(num_nodes):
                (node, id) = queue.popleft()
                
                if node.left:
                    queue.append((node.left, 2*id)) # If tree was complete this would be its id
                
                if node.right:
                    queue.append((node.right, 2*id + 1))
                
                last = id
                
                if not first:
                    first = id
            
            max_width = max(max_width, last-first+1)
        
        return max_width
                    
            