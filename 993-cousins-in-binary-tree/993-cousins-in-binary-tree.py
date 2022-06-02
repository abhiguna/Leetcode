# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # Edge case: empty tree
        if not root:
            return False
        
        curr_level = 0
        parent_x, level_x = -1, -1
        parent_y, level_y = -1, -1
        
        queue = deque([root])
        
        while queue:
            num_nodes = len(queue)
            
            for _ in range(num_nodes):
                node = queue.popleft()
                if node.val == x:
                    level_x = curr_level
                if node.val == y:
                    level_y = curr_level
                
                if node.left:
                    if node.left.val == x:
                        parent_x = node
                    elif node.left.val == y:
                        parent_y = node
                    queue.append(node.left)
                
                if node.right:
                    if node.right.val == x:
                        parent_x = node
                    elif node.right.val == y:
                        parent_y = node
                    queue.append(node.right)
            
            curr_level += 1
        
        return (level_x == level_y) and (parent_x != parent_y)
                