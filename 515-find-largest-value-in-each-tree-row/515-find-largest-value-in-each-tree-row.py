# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # Edge case: empty tree
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            num_nodes = len(queue)
            largest_num = -math.inf 
            
            for _ in range(num_nodes):
                node = queue.popleft()
                largest_num = max(largest_num, node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            res.append(largest_num)
        
        return res