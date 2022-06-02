# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Edge case: empty tree
        if not p and not q:
            return True
        elif (p and not q) or (not p and q):
            return False
        
        queue_p = deque([p])
        queue_q = deque([q])
        
        while queue_p and queue_q:
            num_nodes_p, num_nodes_q = len(queue_p), len(queue_q)
            
            # Structural check
            if num_nodes_p != num_nodes_q:
                return False
            
            for i in range(min(num_nodes_p, num_nodes_q)):
                node_p = queue_p.popleft()
                node_q = queue_q.popleft()
                
                # Check if values don't match
                if node_p.val != node_q.val:
                    return False
                
                # Check if structurally they don't match
                if (node_p.left and not node_q.left) or (not node_p.left and node_q.left):
                    return False
                if (node_p.right and not node_q.right) or (not node_p.right and node_q.right):
                    return False
                
                if node_p.left:
                    queue_p.append(node_p.left)
                    queue_q.append(node_q.left)
                
                if node_p.right:
                    queue_p.append(node_p.right)
                    queue_q.append(node_q.right)
        
        return True
                    