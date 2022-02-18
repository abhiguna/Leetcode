# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        output = []
        level_list = deque()
        node_queue = deque([root, None])
        
        
        while node_queue:
            curr_node = node_queue.popleft()
            
            if curr_node:
                level_list.append(curr_node.val)
                
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                output.append(level_list)
                
                if node_queue:
                    node_queue.append(None)
                
                level_list = deque()
        
        return output