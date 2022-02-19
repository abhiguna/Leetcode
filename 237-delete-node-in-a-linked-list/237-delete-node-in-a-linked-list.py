# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 4->5->1->9
# 4->1->9
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node:
            return
        
        next_next_node = node.next.next
        node.next.next = None
        node.val = node.next.val
        node.next = next_next_node
        
        return
        