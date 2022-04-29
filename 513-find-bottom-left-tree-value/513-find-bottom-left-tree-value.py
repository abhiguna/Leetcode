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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        bottom_left = -1
        
        while queue:
            num_nodes = len(queue)
            
            for i in range(num_nodes):
                curr_node = queue.popleft()
                if i == 0:
                    bottom_left = curr_node.val
                
                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)
        
        return bottom_left