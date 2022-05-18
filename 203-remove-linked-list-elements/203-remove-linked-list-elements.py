# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(N)
    # Space = O(1)
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Sentinel node
        sentinel = ListNode(-math.inf, head)
        
        # Prev node points to the leftmost node that has a value other than val
        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next 
                
        head = sentinel.next 
        return head