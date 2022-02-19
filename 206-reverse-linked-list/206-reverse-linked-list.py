# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseRecursive(prev, curr):
            if not curr:
                return prev
            next_node = curr.next
            curr.next = prev
            return reverseRecursive(curr, next_node)
        head = reverseRecursive(None, head)
        return head