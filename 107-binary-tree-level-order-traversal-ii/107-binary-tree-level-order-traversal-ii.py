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
        # Edge case: empty tree
        if not root:
            return []
        
        res = deque()
        queue = deque([root])
        while queue:
            num_nodes = len(queue)
            curr_level = []
            
            for _ in range(num_nodes):
                node = queue.popleft()
                curr_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            res.appendleft(curr_level)
        
        return res