# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Time = O(N)
    # Space = O(N)
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = deque([root])
        is_lr = True
        
        while q:
            num_nodes = len(q)
            curr_level = deque()
            
            for i in range(num_nodes):
                node = q.popleft()
                
                if is_lr:
                    curr_level.append(node.val)
                else:
                    curr_level.appendleft(node.val)
                    
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            res.append(curr_level)
            is_lr = not is_lr
        
        return res
        