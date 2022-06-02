# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: empty tree
        if not root:
            return []
        
        queue = deque()
        queue.append((root, 0))
        
        neg = []
        zero = [[]]
        pos = []
        
        while queue:
            (node, col) = queue.popleft()
            
            if col == 0:
                zero[0].append(node.val)
            
            elif col < 0:
                if abs(col) > len(neg):
                    neg.append([])
                neg[abs(col) - 1].append(node.val)
            
            elif col > 0:
                if col > len(pos):
                    pos.append([])
                pos[col-1].append(node.val)
            
            if node.left:
                queue.append((node.left, col-1))
            
            if node.right:
                queue.append((node.right, col+1))
        
        neg.reverse()
        res = neg + zero + pos
        
        return res
                