# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(N), N: # of nodes in the tree
    # Space = O(N)
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Edge case: empty tree
        if not root:
            return 0
        
        max_level_sum = -math.inf 
        min_level = 1
        curr_level = 1
        
        queue = deque([root])
        while queue:
            num_nodes = len(queue)
            total_sum = 0
            
            for _ in range(num_nodes):
                node = queue.popleft()
                total_sum += node.val 
                
                if node.left:
                    queue.append(node.left) 
                
                if node.right:
                    queue.append(node.right)
            
            if total_sum > max_level_sum:
                max_level_sum = total_sum
                min_level = curr_level
            
            curr_level += 1
        
        return min_level