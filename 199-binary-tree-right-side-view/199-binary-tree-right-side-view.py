# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N)
    # Space = O(N)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Edge case: empty tree
        if not root:
            return []
        
        res = []
        
        # BFS traversal
        queue = deque()
        queue.append(root)
        
        while queue:
            num_nodes = len(queue)
            
            for i in range(num_nodes):
                node = queue.popleft()
                
                # Add to res if last node in the level
                if i == num_nodes - 1:
                    res.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res
            