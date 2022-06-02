# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # Edge case: empty tree
        if not root:
            return 0
        
        expected_id = 1 # Expected id of a node in a complete binary tree (i.e. a bin heap represented as an array)
        queue = deque([(root, 1)])
        
        while queue:
            num_nodes = len(queue)
            
            for _ in range(num_nodes):
                (node, id) = queue.popleft()
                
                if id == expected_id:
                    expected_id += 1
                else:
                    return False
                
                if node.left:
                    queue.append((node.left, 2*id))
                
                if node.right:
                    queue.append((node.right, 2*id + 1))
        
        return True
        