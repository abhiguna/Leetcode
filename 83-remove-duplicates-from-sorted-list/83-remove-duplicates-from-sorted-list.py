# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(N)
    # Space = O(1)
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(-math.inf, head)
        prev, curr = sentinel, head
        
        while curr:
            # Found a duplicate -> must delete current node
            if curr.val == prev.val:
                prev.next = curr.next 
                curr = curr.next
            else:
                prev = curr
                curr = curr.next 
        
        return head