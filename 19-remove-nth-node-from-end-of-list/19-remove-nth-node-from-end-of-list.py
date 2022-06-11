# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(N)
    # Space = O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        hare, tortoise = head, head
        
        for _ in range(n-1):
            hare = hare.next 
        
        prev = None
        while hare.next:
            prev = tortoise
            tortoise = tortoise.next
            hare = hare.next 
        
        # Edge case: Removing head
        if not prev:
            head = head.next 
        else:
            prev.next = tortoise.next 
        
        return head