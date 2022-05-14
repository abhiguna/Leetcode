# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Approach: Memoization
    
    # Time = O(Catalan Number) => O(C(2n, n) / (n+1))
    # Space = O(Catalan Number) => O(C(2n, n) / (n+1))
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        
        def helper(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            
            # Base cases
            # Empty subtree
            if start > end:
                return [None]
            # Single element subtree
            if start == end:
                return [TreeNode(start)]
            
            # Recursive case --> make every element from [start, end] as the root
            res = [] # res stores the list of trees from [start, end]
            for r in range(start, end+1):
                # Get the left and right subtree
                left_sub = helper(start, r-1)
                right_sub = helper(r+1, end)
                for lst in left_sub:
                    for rst in right_sub:
                        root = TreeNode(r)
                        root.left, root.right = lst, rst
                        res.append(root)
        
            memo[(start, end)] = res
            return res
        
        return helper(1, n)