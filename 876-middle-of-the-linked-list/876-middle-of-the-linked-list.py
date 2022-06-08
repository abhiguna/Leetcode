# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(N)
    # Space = O(1)
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hare, tortoise = head, head
        
        while hare.next and hare.next.next:
            hare = hare.next.next
            tortoise = tortoise.next 
        
        # Edge case: even number of nodes 
        if hare.next:
            return tortoise.next 
        
        return tortoise
            