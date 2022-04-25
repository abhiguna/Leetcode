# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            level = []
            num_nodes = len(queue)
            
            # Process curr level
            for i in range(num_nodes):
                curr_node = queue.popleft()
                
                level.append(curr_node.val)
                
                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)
            
            # Append rightmost node in curr level to final result
            res.append(level[-1])
        
        return res
            
        