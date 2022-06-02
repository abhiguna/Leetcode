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
        # Edge case: empty tree
        if not root:
            return []
        
        res = []
        queue = deque([root])
        while queue:
            num_nodes = len(queue)
            total_sum = 0
            
            for _ in range(num_nodes):
                node = queue.popleft()
                total_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
            res.append(total_sum / num_nodes)
        
        return res
            