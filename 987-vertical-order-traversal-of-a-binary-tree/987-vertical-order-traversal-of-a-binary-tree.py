# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: empty tree
        if not root:
            return []
        
        node_list = []
        
        def dfs(node, row, col):
            node_list.append((col, row, node.val))
            if node.left:
                dfs(node.left, row+1, col-1)
            if node.right:
                dfs(node.right, row+1, col+1)
                        
        dfs(root, 0, 0)
        
        # Sort by cols
        node_list.sort()
        
        # Retrieve the sorted list by cols
        res = []
        curr_col_idx = node_list[0][0]
        curr_col = []
        
        for col, row, num in node_list:
            if col == curr_col_idx:
                curr_col.append(num)
            else:
                res.append(curr_col)
                curr_col = [num]
                curr_col_idx = col
        
        res.append(curr_col)
        return res
            