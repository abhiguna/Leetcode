# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Edge case: empty tree
        if not root:
            return True
        
        queue = deque([(root, root)])
        
        while queue:
            num_nodes = len(queue)
            
            for _ in range(num_nodes):
                (nodeL, nodeR) = queue.popleft()
                
                # Check if values are different
                if nodeL.val != nodeR.val:
                    return False
                
                # Compare left child of left node and right node of right child
                if nodeL.left and nodeR.right:
                    queue.append((nodeL.left, nodeR.right))
                if (nodeL.left and not nodeR.right) or (not nodeL.left and nodeR.right):
                    return False
                
                # Compare right child of left node and left node of right child
                if nodeL.right and nodeR.left:
                    queue.append((nodeL.right, nodeR.left))
                if (nodeL.right and not nodeR.left) or (not nodeL.right and nodeR.left):
                    return False
        
        return True
                    