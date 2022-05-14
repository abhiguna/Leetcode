# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Approach 1: Memoization
    
    
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        
        def helper(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            
            if start > end:
                return [None]
            
            if start == end:
                return [TreeNode(0)]
            
            res = []
            for r in range(start+1, end):
                left_sub = helper(start, r - 1)
                right_sub = helper(r+1, end)
                for lst in left_sub:
                    for rst in right_sub:
                        root = TreeNode(0)
                        root.left = lst
                        root.right = rst
                        res.append(root)
            
            memo[(start, end)] = res
            return res
        
        return helper(1, n)