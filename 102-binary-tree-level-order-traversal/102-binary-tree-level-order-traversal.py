from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Time = O(N)
    # Space = O(N)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            k = len(queue) # k: num of nodes at curr level
            curr_level = []
            
            for i in range(k):
                curr_node = queue.popleft() # FIFO
                curr_level.append(curr_node.val)
                
                # Add children to queue
                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)
            
            res.append(curr_level)
        
        return res
        