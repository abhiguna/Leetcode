# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Date: 2/19/22
# Optimal
# 15m 5
class Solution:
    # Pattern: linked lists
    # Time = O(1)
    # Space = O(1)
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node:
            return
        
        next_next_node = node.next.next
        node.val = node.next.val
        node.next = next_next_node
        
        return
        