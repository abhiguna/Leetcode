# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



"""
root = [3,9,20,null,null,15,7]

[[3],[20,9],[15,7]]

"""
class Solution:
    # Time = O(n), n: # of nodes in the tree
    # Space = O(w), w: max-width of the tree ~ at most O(n)
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: empty tree
        if not root:
            return []
        
        res = []
        
        # BFS
        is_lr = True
        queue = deque()
        queue.append(root)
        
        while queue:
            num_nodes = len(queue)
            level = deque()
            
            for _ in range(num_nodes):
                node = queue.popleft()
                
                if is_lr:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(list(level))
            is_lr = not is_lr
        
        return res