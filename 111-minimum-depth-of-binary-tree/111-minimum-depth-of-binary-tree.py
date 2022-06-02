# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Edge case: empty tree
        if not root:
            return 0
        
        queue = deque([root])
        level_num = 1
        
        while queue:
            num_nodes = len(queue)
            
            for _ in range(num_nodes):
                node = queue.popleft()
                
                # Check if min depth is reached -> leaf node
                if not node.left and not node.right:
                    return level_num
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            level_num += 1

    
        return level_num
                