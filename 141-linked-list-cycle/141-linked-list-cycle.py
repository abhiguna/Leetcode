# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time = O(N)
    # Space = O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Edge case: the list is empty
        if not head: return False
        
        hare, tortoise = head, head
        # While the hare can move two steps forward
        while hare.next and hare.next.next:
            hare = hare.next.next
            tortoise = tortoise.next 
            # Check if they meet at some point
            while hare == tortoise:
                return True
        
        # Reached the end of the linked list
        return False