# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(n), n: # of nodes in the tree
    # Space = O(n)
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        queue = deque()
        queue.append((root, 1))
        
        while queue:
            num_nodes = len(queue)
            leftmost_idx, rightmost_idx = 0, 0
            
            for i in range(num_nodes):
                (node, idx) = queue.popleft()
                
                # Update leftmost and rightmost idx
                if i == 0:
                    leftmost_idx = idx
                
                if i == num_nodes - 1:
                    rightmost_idx = idx
                
                if node.left:
                    queue.append((node.left, 2*idx))
                
                if node.right:
                    queue.append((node.right, (2*idx) + 1))
            
            curr_width = rightmost_idx - leftmost_idx + 1
            max_width = max(max_width, curr_width)
        
        return max_width
            