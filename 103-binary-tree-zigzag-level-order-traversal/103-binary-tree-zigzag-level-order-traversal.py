# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    # node_queue --> main BFS queue
    # zig_zag --> maintain zigzag order
    # result --> output
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        zig_zag = deque()
        node_queue = deque([root, None])
        l2r = True
        
        while node_queue:
            curr_node = node_queue.popleft()
            if curr_node:
                if l2r:
                    zig_zag.append(curr_node.val)
                else:
                    zig_zag.appendleft(curr_node.val)
                
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                if node_queue:
                    node_queue.append(None)
                l2r = not l2r
                result.append(zig_zag)
                zig_zag = deque()

        return result