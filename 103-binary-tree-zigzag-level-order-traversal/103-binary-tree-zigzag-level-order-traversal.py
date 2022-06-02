# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: empty tree
        if not root:
            return []
        
        res = []
        queue = deque([root])
        l_to_r = True
        
        while queue:
            num_nodes = len(queue)
            curr_level = deque()
            
            for _ in range(num_nodes):
                node = queue.popleft()
                if l_to_r:
                    curr_level.append(node.val)
                else:
                    curr_level.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            l_to_r = not l_to_r
            res.append(list(curr_level))
        
        return res
        