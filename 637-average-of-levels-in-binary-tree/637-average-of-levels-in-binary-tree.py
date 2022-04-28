# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N)
    # Space = O(N)
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = deque([root])
        
        while queue:
            num_nodes = len(queue)
            level_sum = 0.0
            
            for _ in range(num_nodes):
                curr_node = queue.popleft()
                level_sum += curr_node.val
                
                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)
                
            res.append(level_sum / num_nodes)
        
        return res