# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    
    # Time = O(N)
    # Space = O(N)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            num_nodes = len(queue)
            
            for i in range(num_nodes):
                curr_node = queue.popleft() 
                
                # Last node of curr level
                if i == num_nodes - 1:
                    res.append(curr_node.val)
                
                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)
            
        return res
                    