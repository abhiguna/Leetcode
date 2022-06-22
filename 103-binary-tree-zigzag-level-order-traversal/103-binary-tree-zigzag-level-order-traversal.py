# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(n), n: # nodes in the tree
    # Space = O(w), w: max-width of the tree ~ at most O(n)
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: empty tree
        if not root:
            return []
        
        res = []
        l_to_r = True
        
        # BFS traversal
        queue = deque()
        queue.append(root)
        
        while queue:
            num_nodes = len(queue)
            level = deque()
            
            for i in range(num_nodes):
                node = queue.popleft()
                
                if l_to_r:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            l_to_r = not l_to_r
            res.append(list(level))
        
        return res