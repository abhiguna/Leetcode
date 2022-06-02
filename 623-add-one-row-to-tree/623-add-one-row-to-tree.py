# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # Edge case: given depth is 1
        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            root = new_node
            return root
        
        # General case
        queue = deque([root])
        curr_depth = 1
        
        while queue:
            num_nodes = len(queue)
            
            for _ in range(num_nodes):
                node = queue.popleft()
                
                if curr_depth == depth - 1:
                    prev_left = node.left
                    node.left = TreeNode(val)
                    node.left.left = prev_left
                    prev_right = node.right
                    node.right = TreeNode(val)
                    node.right.right = prev_right
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
            curr_depth += 1
            
            if curr_depth >= depth:
                    break
        
        return root