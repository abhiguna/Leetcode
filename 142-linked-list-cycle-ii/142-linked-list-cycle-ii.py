# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time = O(N)
    # Space = O(1)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: empty list
        if not head: return None
        
        hare, tortoise = head, head
        
        # While the hare can move 2 steps forward
        while hare.next and hare.next.next:
            hare = hare.next.next
            tortoise = tortoise.next
            # Cycle found
            if hare == tortoise:
                # Start third pointer from the head and move it forward until it meets with
                #.  the tortoise
                third = head
                while third != tortoise:
                    third = third.next
                    tortoise = tortoise.next 
                return third
        
        # No cycle found
        return None