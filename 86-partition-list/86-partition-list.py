# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(N)
    # Space = O(1)
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # We will maintain two lists representing the list with elements < x and a list with elements >= x
        sentinel_s = ListNode(-math.inf)
        sentinel_l = ListNode(-math.inf)
        tail_s = sentinel_s
        tail_l = sentinel_l
        curr = head
        while curr:
            # Extract the curr node
            succ = curr.next 
            curr.next = None
            
            # Add the curr node to the respective lists
            if curr.val < x:
                tail_s.next = curr
                tail_s = tail_s.next 
            else:
                tail_l.next = curr
                tail_l = tail_l.next 
            
            # Move curr node forward
            curr = succ
        
        # If first partition not empty
        if sentinel_s.next:
            tail_s.next = sentinel_l.next 
            return sentinel_s.next 
        
        # Otherwise, returm the second partition
        return sentinel_l.next