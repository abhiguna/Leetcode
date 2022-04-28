# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N)
    # Space = O(N)
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = deque()
        queue = deque([root])
        
        while queue:
            num_nodes = len(queue)
            curr_level = []
            
            for _ in range(num_nodes):
                curr_node = queue.popleft()
                
                curr_level.append(curr_node.val)
                
                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)
                
            
            res.appendleft(curr_level)
        
        return res
            